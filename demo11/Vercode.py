# This module implements a functionality to automatically generate verification code
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# This function randomly generates the background color
# return them as a tuple representing an RGB color value


def get_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


# This function randomly select characters from the string 's' ti form a random combination of letters and create a verification code
# Specify the length of the verification code as a parameter


def get_code(length):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    code = ''
    for i in range(length):
        code += random.choice(s)

    return code


# This function is used to draw a verification code

def draw_code():
    # Specify the height and width of the canvas
    width = 120
    height = 40
    image_size = (width, height)

    # define the canvas
    # create a canvas using new()
    image = Image.new('RGB', image_size, get_color())
    # define the brush
    draw = ImageDraw.Draw(image)

    # generate a verification code
    code = get_code(4)

    # specify font size and font
    # ImageFont.truetype() Load a local font file and set the font size
    myfont = ImageFont.truetype(font='./demo11/tahoma.ttf', size=30)

    # Draw the characters of the verification code
    for i in range(4):
        # height 40 size 30 width 120 x = 120/4 y = (40-30)/2
        distance_x = random.randint(30 * i, 30 * i + 5)
        distance_y = random.randint(0, 5)
        # draw.text(pisition,content,font, fillcolor)
        draw.text((distance_x, distance_y),
                  code[i], font=myfont, fill=get_color())

    # Draw the interference lines
    for i in range(10):
        # Specify the starting and ending position
        starting = (random.randint(0, width), random.randint(0, height))
        ending = (random.randint(0, width), random.randint(0, height))
        draw.line((starting, ending), fill=get_color())

    # Draw the interference point
    for i in range(10):
        draw.point((random.randint(0, width),
                   random.randint(0, height)), fill=get_color())

    # filler Edge enhancement
    image = image.filter(ImageFilter.EDGE_ENHANCE)
    image.show()
    image1 = image.filter(ImageFilter.BLUR)
    image1.show()


draw_code()
