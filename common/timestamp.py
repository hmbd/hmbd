#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.mongo_helper import get_db

import datetime
import pytz
import time


def get_now_time_stamp():
    # 亚洲上海时区
    tz = pytz.timezone('Asia/Shanghai')
    # 系统当前时间
    system_time = datetime.datetime.now(tz)
    # 时间戳
    timestamp = int(time.mktime(system_time.timetuple()))
    return timestamp

if __name__ == '__main__':
    a = get_now_time_stamp()
    print('a:', a)

    db = get_db()
    stamp_time = []
    system_time = []
    online_number = []
    other_time = []
    for u in db.posts.find().sort([("system_time", -1)])[:51]:
        # 时间戳
        timestamp = str(int(time.mktime(time.strptime(str(u['system_time']), '%Y-%m-%d %H:%M:%S'))))
        # 时间数组
        time_array = time.localtime(time.mktime(time.strptime(str(u['system_time']), '%Y-%m-%d %H:%M:%S')))
        # 其他格式时间
        other_style_time = time.strftime("%d %H:%M", time_array)
        stamp_time.append(timestamp)
        other_time.append(other_style_time)
        system_time.append(u['system_time'])
        online_number.append(int(u['online_number']))

    print('stamp_time:', stamp_time)
    print('other_time', other_time)
    print('system_time:', system_time)
    print('online_number', online_number)
