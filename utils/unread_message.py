#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


def add_num(img):
    draw = ImageDraw.Draw(img)
    my_font = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', size=90)
    fillcolor = "#ff0000"
    width, height = img.size
    # 绘制圆形，第一个参数界定绘制区域，我选择了宽高为原图1/3的右上角区域
    #  不难发现坐标系是以左上角为原点，向下y递增，向右x递增
    draw.pieslice([(width/3*2, 0), (width, height/4)], 0, 360, fill=fillcolor)
    # 第一个参数是坐标，第二个参数是文本绘制内容，第三个是字体对象
    draw.text((width - 90, 10), '4', font=my_font, fill="white")
    img.show()  # 展示绘制结果（使用系统默认的图片浏览器）
    img.save("result.jpg", "jpeg")


if __name__ == "__main__":
    image = Image.open('D:\er.jpg')
    add_num(image)
