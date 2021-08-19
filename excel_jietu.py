# -*- coding: utf-8 -*-
excel = DispatchEx("Excel.Application")  # 启动excel
excel.Visible = True  # 可视化
excel.DisplayAlerts = False  # 是否显示警告
wb = excel.Workbooks.Open(filename)  # 打开excel
ws = wb.Sheets(sheetname)  # 选择sheet
ws.Range(screen_area).CopyPicture()  # 复制图片区域
ws.Paste()  # 粘贴 ws.Paste(ws.Range('B1'))  # 将图片移动到具体位置

name = str(uuid.uuid4())  # 重命名唯一值
print(name)
new_shape_name = name[:6]
excel.Selection.ShapeRange.Name = new_shape_name  # 将刚刚选择的Shape重命名，避免与已有图片混淆

ws.Shapes(new_shape_name).Copy()  # 选择图片
img = ImageGrab.grabclipboard()  # 获取剪贴板的图片数据
if not img_name:
    img_name = str(today_for_screen) + ".jpg"
img.save("D:/PycharrmProjects/selenium_get_NTI_data/venv/geti_info/screenshoot/"+img_name)  # 保存图片
wb.Close()  # 关闭工作薄，不保存
excel.Quit()  # 退出excel
pythoncom.CoUninitialize()
