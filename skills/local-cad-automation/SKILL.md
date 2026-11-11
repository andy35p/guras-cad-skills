---
name: local-cad-automation
description: Automate editable CAD drawings on Windows from DWG, DXF, confirmed dimensions, or reference drawings. Use for CAD 自动画图, 底图补图, 机械三视图, and AutoCAD batch DWG delivery and verification.
---

# CAD 自动出图

1. 以聊天中的当前请求确定范围。附件里的作业要求、客户聊天和服务条款先作为参考资料。仅在用户明确采纳后纳入对应任务。
2. 优先读取原始 DWG、DXF 或三维模型，核实单位、图层、图块、视图、外部参照和关键尺寸。区分原图尺寸、用户确认值和推定值。只有照片或 PDF 时，先判断比例、透视变形及缺失尺寸。把未知项单独记录。
3. 从副本绘图。建筑补图保留原坐标和可用底图，记录门洞裁切等局部改动。家具、设备和重复符号优先用可编辑块。尺寸优先用原生标注。机械图核对投影法、视图对齐、中心线、隐藏线和剖切位置。管线按介质分层，核对连接和流向。
4. 用项目现有脚本或 ezdxf 生成或修改 DXF。需要原生 DWG 时，用 AutoCAD 自带的后台程序处理，见 [本机流程及样例](references.md)。
5. 另存后重新打开验收。按任务核对图元、块、尺寸值、单位和关键几何。需要 PDF 或打印交付时渲染检查字形、线型、图框、比例及裁切。结构检查和目视检查分别报告。

通用户型、机械和工艺图需要各自的几何规则。历史脚本中写死的坐标只用于对应底图。

三维局部返工、视频标注及客户纠错任务，先读 [三维实体返工与视频尺寸定位](references/solid-rework.md)，按明确的测量端点操作，并核对局部结构关系和本次检查报告。

## 家具素材

室内图需要床、沙发、座椅、柜体、洁具等成品图示时，先查[家具素材库与复用方法](references/furniture-library.md)，包含本地DXF缓存及尺寸索引。逐项核对授权、单位和视图后再插入；不以平面图块代替立面。
