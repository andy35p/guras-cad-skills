---
name: rhino-modeling
description: 使用 Rhino（犀牛）建立、修复和检查曲线、NURBS 曲面与实体，处理可编辑 3DM 交付及 STEP、DWG、DXF 交换。适用于 Rhino 命令操作及 Rhino 8 Python 自动化。
---

# Rhino 建模与交付

## 建模与修复

- 导入前确认目标文档单位和绝对公差。导入后用 Distance 复测一处已知尺寸，并检查模型包围盒。遇到单位差异时确认来源单位和是否需要缩放几何，避免二次缩放。
- 用实际工作平面画轮廓。做平面挤出实体前检查轮廓闭合、共面且无自交。布尔运算前确认输入符合预期的封闭状态，并检查实体确有相交体积。
- Join 失败时用 ShowEdges 定位裸边，检查缝隙、重叠、短边与修剪边界。先修复局部几何，再重新连接。保留有意开放的曲面，按任务要求判断是否需要封闭。
- 用 Check 或 SelBadObjects 查找无效对象，再用 ShowEdges 检查目标实体的裸边和非流形边。对象有效性与实体封闭性需要分别检查。

[单位和公差](https://docs.mcneel.com/rhino/8/help/en-us/documentproperties/units.htm) · [Check 命令](https://docs.mcneel.com/rhino/8/help/en-us/commands/check.htm)

## 自动化

- Rhino 8 优先通过 ScriptEditor 运行 Python 3 脚本。需要兼容既有 IronPython 代码时明确选择 Python 2，并核对依赖和调用签名。
- RhinoCommon 可处理几何和文档对象。根据运行环境明确目标文档，先核对输入对象 ID、单位和公差，再修改文档。批处理可在 Rhino 环境用 RhinoDoc.OpenHeadless 读取 3DM，处理完释放文档。
- 使用版本支持的 RhinoCommon 文件接口和格式选项。需要调用命令时，先在目标 Rhino 版本验证命令及选项顺序，再用脚本运行。对每个输入记录输出路径及实际成功或失败状态。

[Rhino Python](https://developer.rhino3d.com/guides/scripting/scripting-python/) · [RhinoCommon 文件读写](https://developer.rhino3d.com/en/guides/rhinocommon/code-driven-file-io/)

## 文件交付

- 用 3DM 保存原生可编辑模型，并保留相关图层、对象属性和块。需要面向旧版本交付时，确认接收端版本并测试另存文件。
- 交付 STEP 时确认接收端支持的方案。重新打开导出件，复测代表尺寸，检查对象数量和目标实体的有效性及封闭性。
- 交付 DWG 或 DXF 时明确接收版本、二维或三维用途和导出方案。二维图纸先确认投影视图与所需线型。重新打开导出件，核对尺寸、图层、块和曲线转换结果。

[STEP 交换](https://docs.mcneel.com/rhino/8/help/en-us/fileio/step_stp_import_export.htm) · [DWG 和 DXF 交换](https://docs.mcneel.com/rhino/8/help/en-us/fileio/autocad_dwg_dxf_import_export.htm)
