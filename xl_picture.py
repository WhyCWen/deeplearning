import os
import xlwings as xw
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path = 'example.xlsx'
if os.path.exists(file_path):
    wb = xw.Book(file_path)
else:
    wb = xw.Book()
    wb.save(file_path)
# 生成随机数据
data = np.random.randn(10, 50)
# 写入到Excel
sheet = wb.sheets['Sheet1']
sheet.range('A1').value = pd.DataFrame(data)
# 生成直方图
plt.hist(data.flatten(), bins=10)
plt.show()
