#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re
import time

import requests
from apscheduler.schedulers.blocking import BlockingScheduler

from common.mongo_helper import get_db


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def pc_qq():
    """实时查询qq在线人数
    """
    # 系统时间
    system_time = get_now_time()
    # 时间戳
    timestamp = str(int(time.mktime(time.strptime(system_time, '%Y-%m-%d %H:%M:%S'))))
    temporary = "http://mma.qq.com/cgi-bin/im/online&callback=jQuery19105562977448571473_" + timestamp + "?_=" + timestamp
    url = [temporary]
    print('QQ在线人数网页', temporary)
    cur_re = re.compile(r'"c":(.+?),"ec"', re.DOTALL)
    for ul in url:
        """
        html=urllib.request.urlopen(ul).read()
        codec =urllib.request.urlopen(ul).info().get_param('charset', 'utf8')
        html = html.decode(codec)
        """
        html = requests.get(ul)
        for online_number in cur_re.findall(html.text):
            print("QQ当前在线人数：" + online_number)

    db = get_db()
    post = {
        "online_number": online_number,
        "system_time": datetime.datetime.utcnow()
    }
    posts = db.ebf_qq
    posts.insert(post)


if __name__ == '__main__':
    # 每隔60秒就操作pc_qq()函数
    sched = BlockingScheduler()
    sched.add_job(pc_qq, 'interval', seconds=60)
    sched.start()
