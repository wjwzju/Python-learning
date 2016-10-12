__author__ = 'wjw'

import sys
import random
from PIL import Image,ImageFilter,ImageDraw,ImageFont

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world')
    elif len(args) == 2:
        print('hello, %s' % args[1])
    else:
        print('Too many arguments!')

def thum():
    im = Image.open('test.jpg')
    print(im.format, im.size, im.mode)
    # 图片缩放
    w,h = im.size
    #im.thumbnail((2000,1000))
    im.thumbnail((w//2, h//2))
    im2 = im.filter(ImageFilter.BLUR) #模糊效果
    im.save('thumb.jpg','JPEG')
    im2.save('blur.jpg','jpeg')

#随机字母
def rndChar():
    return chr(random.randint(65,90))

#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#字母验证码
def verifyCode():
    width = 60*4
    height = 60
    image = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',36) #create font
    draw = ImageDraw.Draw(image) # create draw
    #填充像素
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndColor())
    #输出数字
    for t in range(4):
        draw.text((60 * t + 10 , 10),rndChar(),font=font, fill=rndColor2())
    #模糊
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg','jpeg')

if __name__=='__main__':
    # test()
    # thum()
    verifyCode()