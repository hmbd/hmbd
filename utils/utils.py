#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re

import socket
import fcntl
import struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                                        0x8915,  # SIOCGIFADDR
                                        # python3.x写法
                                        struct.pack('256s'.encode(encoding="utf-8"),
                                                    ifname[:15].encode(encoding="utf-8")))[20:24]
                            # python2.x写法
                            # struct.pack('256s', ifname[:15]))[20:24]
                            )
def download_img():
    def get_html(url):
        page = urllib.request.urlopen(url)
        result = page.read()
        return result

    def download_img_(result):
        reg = r'src="(.+?\.jpg)" pic_ext'
        img_re = re.compile(reg)
        img_list = re.findall(img_re, result)
        count = 1
        for i in img_list:
            print('开始下载第%s张图片' % count)
            # 不指定路径就会下载到当前文件夹下
            # python2中需把urllib.request替换成urllib
            urllib.request.urlretrieve(i, '/home/lcx/PycharmProjects/test/test/%s.jpg' % count)
            count += 1

    # html类型是byte
    html = get_html("http://tieba.baidu.com/p/2460150866")
    # 将html转成str
    str_html = html.decode()
    download_img_(str_html)
