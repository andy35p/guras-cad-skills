# 本机原生执行

## 环境发现
本机曾验证 AutoCAD 2026 的 D:/AUTOCAD2026/AutoCAD 2026/accoreconsole.exe、PS 2024 的 D:/pspps/Adobe Photoshop 2024/Photoshop.exe、SU 2026 的 D:/su/SketchUp/SketchUp.exe。路径及版本可能变化，执行前用进程、注册信息及文件存在性重新确认。安装器或解压目录不等于已安装应用。

## AutoCAD
- 使用当前原文件的工作副本，英文命令前加下划线。毫米制与 WCS 的设置仅作用于确认过的工作图。
- 后台脚本使用无中文的工作路径，末尾加空行。DXFOUT 精度为数字 16，不是关键字 _16。
- SAVEAS 后显式 QUIT，避免等待进程退出导致队列挂起。既有会话需要保留时不要关闭其用户文档。
- 查看 UTF-16LE 日志，检查命令取消与等待输入，不能仅以进程返回码认定成功。
- 转换后重新读取实体、块、文字、尺寸和单位，DWG 再次原生打开及 AUDIT。
- 中文字体替换需要验证字形；打印轮廓不见时核查实体 TrueColor、图层打印状态及视口冻结。

## Photoshop
- Python win32com 的 Photoshop.Application 能执行 DoJavaScriptFile，使用 JSX 创建文档、LayerSet、素材图层、文字并保存带 layers=true 的 PhotoshopSaveOptions。
- 先确定最终画布、地面线与图组尺寸；反复整体缩放会影响字号，完成排版后再统一文字。
- 复制素材图层后按可见 bounds 等比缩放并定位底部，不把带透明留白的画布宽高直接当作树冠尺寸。
- 图组拆分导出时逐图隐藏其他组及标题，在副本上 crop，保存 PNG 后关闭副本而保留主文件。
- 重新打开 PSD 验证组、文字及独立素材；导出 PNG 与参考图逐项比较，不能只验证文件大小。
- 若素材原图保留为链接对象，随最终成果一并保存依赖或改为嵌入对象。

## SketchUp
- 应用首次启动条款、登录由用户处理；进入建模界面后再操作。使用 UI 时按已安装 computer-use 技能的状态读取与输入规则执行。
- Ruby 控制台没有执行回显时，先核查焦点和窗口状态。不要不断向同一未知控件盲输，也不能把失败的 RubyStartup 启动当作建模完成。
- 本机 SketchUpAPI.dll 可离线创建及读取原生 SKP，Python ctypes 的结构体和参数类型必须与官方 C API 对应。避免凭记忆猜测 API。
- SU 实际长度使用英寸，输入毫米需除 25.4。创建面时剔除连续重复点并校对绕向。
- Group 加入 model 后再追加实体；各建筑、植被、道路分组，SUGroupToDrawingElement 的 ctypes restype 为 Ref 结构体。
- SUMaterialSetColor、SUModelAddMaterials、SUDrawingElementSetMaterial 可设置群组材质。树、草坪、建筑材质分开。
- SUEntitiesAddSectionPlanes 接收数组；SUSceneCreate 后先命名并加入模型，再设置 camera。正交高度用 SUCameraSetOrthographicFrustumHeight。
- 保存采用新的临时路径，避免覆盖正在被 SU 占用的模型。SUModelCreateFromFile 成功只能证明可读取，还要目视检查模型和视图。

官方接口 https://extensions.sketchup.com/developers/sketchup_c_api/sketchup/index.html
