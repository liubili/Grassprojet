# 本项目用到了PySimpleGUI模块
用于创建一个简单的GUI界面，包括文本、输入框、文件选择器、下拉列表和按钮等元素
使用subprocess模块调用ffmpeg命令进行视频转换，根据用户选择的文件名和格式生成输出文件名和命令参数。
使用sg.popup()方法弹出对话框提示用户转换的进度和结果。
参考：https://www.pysimplegui.org/en/latest/（pysimpleGUI)
https://ffmpeg.org(ffmepg)

st=>start: 开始
op1=>operation: 导入PySimpleGUI和subprocess模块
op2=>operation: 定义窗口布局
op3=>operation: 创建窗口对象
op4=>operation: 读取窗口事件和值
cond1=>condition: 事件是"开始转换"吗？
op5=>operation: 获取用户选择的文件名和格式
cond2=>condition: 文件名和格式是否有效？
op6=>operation: 生成输出文件名
op7=>operation: 调用ffmpeg进行视频转换
op8=>operation: 弹出对话框提示转换完成
op9=>operation: 弹出对话框提示输入错误
cond3=>condition: 事件是"退出"或窗口关闭吗？
e=>end: 结束

st->op1->op2->op3->op4
op4(yes)->cond1
cond1(yes)->op5->cond2
cond2(yes)->op6->op7->op8->op4
cond2(no)->op9->op4
cond1(no)->cond3
cond3(yes)->e
cond3(no)->op4
