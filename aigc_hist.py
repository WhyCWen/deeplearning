import os
import random
import xlwings as xw
# 定义要创建的 Excel 文件名称
file_name = 'test.xlsx'
# 判断文件是否存在
if os.path.isfile(file_name):
    print('文件已经存在')
    # 打开已经存在的文件
    wb = xw.Book(file_name)
else:
    print('文件不存在，现在开始创建文件')
    # 创建新的 Excel 文件
    wb = xw.Book()
    # 保存文件
    wb.save(file_name)
# 生成 20x20 的随机数据
data = [[random.randint(0, 100) for j in range(3)] for i in range(5)]
# 将数据写入 Excel 文件中
sheet = wb.sheets[0]
sheet.range('A1').value = data
# 绘制直方图并将图表插入到 Excel 文件中
chart = sheet.charts.add()
chart.set_source_data(sheet.range('A1:T20'))
chart.name = 'wahaha'
chart.chart_type = '3d_column'
# 保存文件
wb.save()
# 关闭文件
