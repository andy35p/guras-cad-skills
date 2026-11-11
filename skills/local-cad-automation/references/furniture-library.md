# CAD家具素材检索与复用

## 已缓存来源（2026-11-07）

- [GSStnb/dxfBlocks](https://github.com/GSStnb/dxfBlocks)：建筑DXF图块，含家具、厨卫、柜体、门窗。固定提交：`65c95bbff7580a6162812c3e82b91b4705057afa`。
- 本地：`assets/furniture/dxfBlocks/Architecture/`；机器索引：`assets/furniture/dxfBlocks/catalog.json`。索引含路径、哈希、图元数、源包围盒、按英寸换算后的毫米大小、审计结果、视图候选类别。
- 上游README声明原尺寸英寸、1:1；换算毫米使用25.4，先核对已知床宽/柜深，不能仅相信INSUNITS。家具多数为平面候选，未逐张认定为立面。Windows/Elevations是窗立面，不是家具立面库。
- **授权冲突**：保留的LICENSE写CC0，README写CC BY-NC-SA 4.0。未解决前不标为可自由商用，不自动用于客户交付；保留为待核验素材和索引，优先换用权利清晰的来源或用户有权使用的素材。

## 其他已查来源与适用性

- [PacktPublishing家具DWG](https://github.com/PacktPublishing/AutoCAD-2023-Masterclass---Produce-Amazing-Site-Plans-Quickly/blob/main/Furniture%20Blocks.dwg)：确有家具DWG候选，许可证、视图及尺寸尚未核验，未缓存为可用资产。
- [growdigital/blocks-furniture](https://github.com/growdigital/blocks-furniture)：户外家具DXF候选，无明确授权信息，未默认纳入交付素材。
- [LibreCAD/Resources](https://github.com/LibreCAD/Resources)：项目资源集合，授权可能逐子目录不同，不能把软件GPL或图标CC0套用于全部家具。
- [steiza/open_source_furniture](https://github.com/steiza/open_source_furniture)：README声明SCAD为MIT；偏家具制造及CAM展开，不等于室内立面成品图块。

## 使用方法

1. 查本地索引和预览，找真实家具图块，再决定是否需要手绘。按平面、正立面、侧立面分别分类；平面符号不能缩放后冒充立面。
2. 新GitHub来源先读README及文件/目录级许可，记录仓库URL、提交、文件路径、作者、许可证和修改方式；下载数据文件，不执行仓库附带代码。
3. ezdxf读DXF；DWG用本地AutoCAD后台转换工作副本。预览核查轮廓完整、单位、比例、朝向、插入点、嵌套块、外参和图像依赖。有问题标隔离，不凭文件名认定可用。
4. 导入为命名BLOCK/INSERT，保留家具可编辑性。统一毫米和基点；按等比缩放，不能为挤入图面拉伸椅子或床。家具层用ByLayer，填色独立置底，尺寸保留原生DIMENSION。
5. 替换前删除旧占位家具及重复轮廓；重新标关键尺寸，不能沿用与新图块不一致的标注。检查块的实际可见宽高与尺寸定义。
6. 各房间是否分文件、是否需要局部平面，遵照当次用户要求。不要因素材带平面而擅自添加分离的小图。
7. 输出保存来源说明ATTRIBUTION.md，重开DWG、审计与彩色/黑白PDF目视检查。只有原生几何和填充才能声称为可编辑CAD素材，贴图及PDF截图不算。

## 2026-11-07 许可历史复核
README修改早于2019-12-20素材提交，不能假定初始CC0根许可证已无歧义地覆盖后加入图块。本次交付采用删除GH_PLAN_及自绘PROJECT_图块替代。缓存仍标待核验，不将此处理描述为作者授权澄清。

## 已验证的CC0三维家具与立面投影（2026-11-07）

优先候选：`assets/furniture/cc0-openhome/`，内含模型、原始许可、来源索引及可直接插入的二维立面DXF（CC0_前缀）。

- 分发仓库：https://github.com/yuyou-dev/OpenHome3D ，固定提交 cb52afc00201b4b7ed90b24631e977112ba07869。
- Kenney Furniture Kit 2.0 和 KayKit Furniture Bits 1.0 各目录LICENSE均明确CC0、允许商业项目。不能用仓库软件MIT代替模型许可；这里核对的是模型自己的LICENSE。
- 缓存了单椅、床、台灯、水槽柜、马桶，已投影成毫米制可编辑HATCH、LWPOLYLINE和图块；与仅嵌入平面块定义不同，这批正立面已实际显示在本次图纸和PDF中。
- GLB为Y向上，投影到XY平面；先预览正负Z朝向，做遮挡裁切和同色区域合并，避免网格三角线满屏。模型为简化风格，先验证其表现是否适合当前项目，不能因授权清楚就默认视觉质量达标。
- 导出的高度由原模型等比投影决定，禁止拉伸凑尺寸；柜体台面高度需与周边台面再核对，不能只按模型宽度盲目插入。需要更写实的家具时继续选择有独立许可的高细节模型。

## 精细成品立面选型补充
客户要求网上常见的精细家具图块时，优先检查实际预览中的软包曲线、床品褶皱、扶手与椅脚，不能用低多边形3D投影替代高细节CAD图块。NASJI提供免费项目使用的CAD立面候选（https://nasji.com/cad-blocks/furniture），应逐页复核使用条款，不标成CC0；素材本身不得作为独立素材库转售。本项目已用座椅、灯具、龙头及花洒立面，裁取局部时需检查完整轮廓，避免按包围盒过滤丢失跨边界曲线。
