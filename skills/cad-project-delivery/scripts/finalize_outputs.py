import argparse
import hashlib
import json
import stat
from pathlib import Path


def digest(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(chunk)
    return value.hexdigest()


def contained_file(root, relative):
    relative = Path(relative)
    if relative.is_absolute() or relative.drive or '..' in relative.parts:
        raise ValueError(f'Unsafe relative path: {relative}')
    path = root / relative
    for parent in [root, *path.relative_to(root).parents]:
        candidate = parent if parent == root else root / parent
        if candidate.exists():
            flags = candidate.lstat()
            if candidate.is_symlink() or getattr(flags, 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                raise ValueError(f'Linked directory: {candidate}')
    if path.is_symlink() or not path.is_file():
        raise ValueError(f'Not a regular file: {path}')
    if not path.resolve().is_relative_to(root):
        raise ValueError(f'Path escapes root: {path}')
    if getattr(path.lstat(), 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
        raise ValueError(f'Linked file: {path}')
    return path


def finalize(plan, apply=False):
    reviewed = []
    for project in plan['projects']:
        root = Path(project['root']).absolute()
        if root.name.lower() != 'outputs' or not root.is_dir():
            raise ValueError(f'Expected an existing outputs directory: {root}')
        keep = set(project['keep'])
        files = project['files']
        if not keep or not keep.issubset(files):
            raise ValueError(f'Invalid keep list: {root}')
        for relative, expected in files.items():
            path = contained_file(root, relative)
            if digest(path) != expected:
                raise ValueError(f'Changed since review: {path}')
            reviewed.append((path, relative in keep))
    results = []
    for path, keep in reviewed:
        status = 'keep' if keep else 'would_delete'
        if apply and not keep:
            try:
                path.unlink()
                status = 'deleted'
            except OSError as error:
                status = f'blocked: {error}'
        results.append({'path': str(path), 'status': status})
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('plan', type=Path)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text(encoding='utf-8-sig'))
    results = finalize(plan, apply=args.apply)
    args.report.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf8')
    counts = {}
    for row in results:
        counts[row['status'].split(':')[0]] = counts.get(row['status'].split(':')[0], 0) + 1
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == '__main__':
    main()
