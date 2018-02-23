#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
需要在终端运行，输入：踏雪
"""

import pygame


def chinese_to_pinyin(x):
    y = ''
    dic = {}
    with open("unicode_pinyin.txt") as f:
        for i in f.readlines():
            dic[i.split()[0]] = i.split()[1]
    for i in x:
        i = str(i.encode('unicode_escape'))[-5:-1].upper()
        try:
            y += dic[i] + ' '
        except:
            y += 'XXXX '
    return y


def make_vioce(x):
    pygame.mixer.init()
    vio = chinese_to_pinyin(x).split()
    print(vio)
    for i in vio:
        if i == 'XXXX':
            continue
        pygame.mixer.music.load("vioce/" + i + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
    return None


while True:
    p = input("请输入文字：")
    make_vioce(p)
