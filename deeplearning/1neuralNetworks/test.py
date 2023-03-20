from PIL import Image
import numpy as np
# 打开图片
resized_img = Image.open('../images/test2.jpg')

# 缩放图片
# new_size = (128, 128)
# resized_img = image.resize(new_size)
pixels = list(resized_img.getdata())
pixels = np.array(pixels).shape
print(pixels)
# print(resized_img.width,resized_img.height)
# resized_img.show("缩小")
# 压缩图片
quality = 50
# compressed_img = img.save('example_compressed.jpg', optimize=True, quality=quality)

aaa = [0,1,2,3,4,5,6,7,8]

print(aaa[:])