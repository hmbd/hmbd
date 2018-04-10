#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import io
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from math import ceil

# 验证码部分
# 修改自https://github.com/tianyu0915/DjangoCaptcha，以支持python3
current_path = os.path.normpath(os.path.dirname(__file__))


class Captcha(object):
    answer = ""

    def __init__(self, img_width=150, img_height=30, code_type='number'):
        """初始化,设置各种属性
        """
        self.words = self._get_words()

        # 验证码图片尺寸
        self.img_width = img_width
        self.img_height = img_height
        self.type = code_type
        self.code = None

    def _get_font_size(self):
        """将图片高度的70%作为字体大小
        """
        s1 = int(self.img_height * 0.7)
        s2 = int(self.img_width // len(self.code))
        return int(min((s1, s2)) + max((s1, s2)) * 0.05)

    def _get_words(self):
        """读取默认的单词表
        """
        file_path = os.path.join(current_path, 'word_code.list')
        f = open(file_path, 'r')
        return [line.replace('\n', '') for line in f.readlines()]

    @classmethod
    def _set_answer(cls, answer):
        """设置答案
        """
        cls.answer = str(answer)

    def _yield_code(self):
        """  生成验证码文字,以及答案

        """

        # 英文单词验证码
        def word():
            code = random.sample(self.words, 1)[0]
            self._set_answer(code)
            return code

        # 数字公式验证码
        def number():
            m, n = 1, 50
            x = random.randrange(m, n)
            y = random.randrange(m, n)

            r = random.randrange(0, 2)
            if r == 0:
                code = "%s - %s = ?" % (x, y)
                z = x - y
            else:
                code = "%s + %s = ?" % (x, y)
                z = x + y
            self._set_answer(z)
            return code

        # 数字字母组合
        def char():
            _letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
            _upper_cases = _letter_cases.upper()  # 大写字母
            _numbers = ''.join(map(str, range(3, 10)))  # 数字
            init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
            length = 4
            code = random.sample(init_chars, length)
            asd = ''.join(code)
            self._set_answer(asd)
            return code

        func = eval(self.type.lower())
        return func()

    def display(self):
        """生成验证码图片
        """

        # 字体颜色
        font_color = ['black', 'darkblue', 'darkred']

        # 背景颜色
        background = (random.randrange(230, 255), random.randrange(230, 255), random.randrange(230, 255))

        # clean
        self._set_answer("")

        # creat a image
        im = Image.new('RGB', (self.img_width, self.img_height), background)
        self.code = self._yield_code()

        # set font size automaticly
        font_size = self._get_font_size()

        # creat a pen
        draw = ImageDraw.Draw(im)

        def create_points():
            """
            绘制干扰点
            """
            point_chance = 2
            chance = min(100, max(0, int(point_chance)))  # 大小限制在[0, 100]
            width, height = 120, 30
            for w in range(width):
                for h in range(height):
                    tmp = random.randint(0, 100)
                    if tmp > 100 - chance:
                        draw.point((w, h), fill=(0, 0, 0))

        create_points()
        # 最多干扰线条数
        if self.type == 'word':
            c = int(8 // len(self.code) * 3) or 3
        elif self.type == 'number':
            c = 2
        else:
            c = 3

        for i in range(random.randrange(c - 2, c)):
            line_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
            xy = (
                random.randrange(0, int(self.img_width * 0.2)),
                random.randrange(0, self.img_height),
                random.randrange(3 * self.img_width // 4, self.img_width),
                random.randrange(0, self.img_height)
            )
            draw.line(xy, fill=line_color, width=int(font_size * 0.1))
            # draw.arc(xy,fill = line_color, width = int(font_size * 0.1))
        # draw.arc(xy, 0, 1400, fill = line_color)

        # draw code
        j = int(font_size * 0.3)
        k = int(font_size * 0.5)
        x = random.randrange(j, k)  # starts point
        for i in self.code:
            # 上下抖动量,字数越多,上下抖动越大
            y = random.randrange(1, 2)

            if i in ('+', '=', '?'):
                # 对计算符号等特殊字符放大处理
                font_size *= 1.2

            # 文字字体
            font_path = os.path.join(current_path, 'msyh.ttf')
            # 设置字体大小和格式
            font = ImageFont.truetype(font=font_path, size=ceil(font_size))

            draw.text((x, y), i, font=font, fill=random.choice(font_color))
            x += self.img_width / len(self.code)
        del x
        del draw
        buf = io.BytesIO()
        # params = [1 - float(random.randint(1, 2)) / 100,
        #           0,
        #           0,
        #           0,
        #           1 - float(random.randint(1, 10)) / 100,
        #           float(random.randint(1, 2)) / 100,
        #           0.001,
        #           float(random.randint(1, 2)) / 500
        #           ]
        # im = im.transform((120, 30), Image.PERSPECTIVE, params)  # 创建扭曲

        # im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）
        im.save(buf, 'gif')
        buf.closed
        return HttpResponse(buf.getvalue(), 'image/gif')

    @classmethod
    def validate(cls, code):
        """检查用户输入的验证码是否正确

        :param code: str 输入的验证码

        :rtype bool
        :return
            True: 验证码正确
            False: 验证码错误
        """

        _code = cls.answer

        cls._set_answer("")
        return _code.lower() == str(code).lower()
