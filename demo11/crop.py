from PIL import Image


image = Image.open('./demo11/AI4.jpg')
# image.show()
print(image.size)

# crop() LEFT - TOP - RIGHT - BUTTON
# WIDTH LEFT & RIGHT
# HEIGHT TOP & BUTTON
im_cr = image.crop(box=(0, 126, 1555, 950))
# im_cr.show()

# resize()  scaling
im_re = image.resize((1000, 550), box=(0, 126, 1555, 950),
                     resample=Image.BICUBIC)
im_re.show()
im_re.save('AI41.jpg')

# rotate() rotation (angle,center,fillcolor,)
im_ro = image.rotate(30, resample=Image.BICUBIC, center=(
    750, 550), expand=True, fillcolor='#4ec8c4')
# im_ro.show()
