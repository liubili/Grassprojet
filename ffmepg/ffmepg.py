import PySimpleGUI as sg
import subprocess

# 布局
layout = [
    [sg.Text("请选择要转换的视频文件：")],
    [sg.Input(key="-FILE-"), sg.FileBrowse()],
    [sg.Text("请选择要转换的目标格式：")],
    [sg.Combo(["mp4", "avi", "mkv", "webm"], key="-打开文件-")],
    [sg.Button("开始转换"), sg.Button("退出")],
    [sg.Text("请选择输出文件夹：")],
    [sg.Input(key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Button("查询支持解码的环境")],
    [sg.Combo(["默认解码", "硬解", "mkv", "webm"], key="-打开文件-")]
]

# 创建窗口
window = sg.Window("使用PySimpleGUI实现的视频转换器", layout)

# 读取窗口事件和值
while True:
    event, values = window.read()
    # 根据事件和值进行逻辑处理
    if event == "开始转换":
        # 获取用户选择的文件名和格式
        filename = values["-FILE-"]
        format = values["-打开文件-"]
        # 检查文件名和格式是否有效
        if filename and format:
            # 生成输出文件名
            output = values["-FOLDER-"] + "/" + filename.rsplit(".", 1)[0] + "." + format
            # 调用ffmpeg进行视频转换
            cmd = ["ffmpeg", "-i", filename, output]
            subprocess.run(cmd)
            # 弹出对话框提示转换完成
            sg.popup(f"视频转换完成，输出文件为{output}")
        else:
            # 弹出对话框提示输入错误
            sg.popup("请输入有效的文件名和格式。")
    elif event == "查询支持解码的环境":
        cmdload = ["ffmpeg", "version"]
        subprocess.run(cmdload)
    elif event == "退出" or event == sg.WIN_CLOSED:
        # 退出循环
        break

# 关闭窗口
window.close()