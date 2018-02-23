#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
import time
from decimal import Decimal

from bson import ObjectId


class UTC2LocalEncoder(json.JSONEncoder):
    """
    在json格式化的时候将时间转换成本地时间
    可以在这个时候对数据进行一些处理和转换
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return (obj + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return (obj + datetime.timedelta(hours=8)).strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def utc2local(utc_st):
    """
    UTC时间转本地时间（+8:00)
    :param utc_st:
    :return:
    """
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


def local2utc(local_st):
    """
    本地时间转UTC时间（-8:00)
    :param local_st:
    :return:
    """
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    utc_st = local_st - offset
    return utc_st
