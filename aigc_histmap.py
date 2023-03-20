import os
import random
import xlwings as xw
import matplotlib.pyplot as plt
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
data = [[random.randint(0, 100) for j in range(10)] for i in range(10)]
# 将数据写入 Excel 文件中
sheet = wb.sheets[0]
sheet.range('A1').value = data
# 绘制直方图并将图表插入到 Excel 文件中
# import matplotlib.pyplot as plt
# fig = plt.figure()
# plt.plot([1, 2, 3, 4, 5])
# sht.pictures.add(fig, name='MyPlot', update=True)
# <Picture 'MyPlot' in <Sheet [Book1]Sheet1>>
fig, ax = plt.subplots()
ax.hist(data)
ax.set_title('Histogram of Random Data')
fig.canvas.draw()
image = xw.Picture(fig.canvas)
sheet.pictures.add(image, name='Histogram', update=True)
# 保存文件
wb.save()
# 关闭文件
wb.close()