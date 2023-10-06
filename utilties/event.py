import discord
from PIL import Image, ImageDraw
from io import BytesIO

def drawProgressBar(length):
    #length = 0~100
    n = length*5.91
    im = Image.open('progress.png').convert('RGB')
    draw = ImageDraw.Draw(im)
    color=(141,214,214)
    #0~591
    x, y, diam = n, 8, 34
    draw.ellipse([x,y,x+diam,y+diam], fill=color)
    ImageDraw.floodfill(im, xy=(14,24), value=color, thresh=40)

    with BytesIO() as image_binary:
        im.save(image_binary, 'PNG')
        image_binary.seek(0)
        file=discord.File(fp=image_binary, filename='image.png')
    return file