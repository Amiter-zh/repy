# Pillow 是PIL的一个派生分支其本事比PIL更具活力且PIL和Pilow不能共存
# open() new() convery()
from PIL import Image

image = Image.open(fp='./demo11/AI4.jpg')

# image.show()

# print(image.size)
# print(image.mode)
# print(image.format)

# image.mode 图像的渲染方式
# 可以通过convert修改
# i1 = image.convert('L')
# i1.show()
# print(i1.size)
# print(i1.mode)
# print(i1.format)

# new()创建一张新图片
l2 = Image.new('RGB', (220, 150), (66, 25, 154))
l2.show()
