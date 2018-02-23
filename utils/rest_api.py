#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

from bson import ObjectId

url = "http://127.0.0.1:8000/api"
r = requests.delete(url=url, params={"_id": ObjectId("569edd4fd5424a0a70d09581")})
print(r.text)

url = "http://127.0.0.1:8000/api"
r = requests.post(url=url, params={"onlinenumber": '1200000000', "systemtime": "2016-01-21 19:08:45"})
print(r.text)

url = "http://127.0.0.1:8000/api"
r = requests.put(url=url, params={"_id": ObjectId("56933012d5424a0b5853cf3e"), "onlinenumber": '222222222',
                                  "systemtime": "2016-01-20 12:12:12"})
print(r.text)

url = "http://127.0.0.1:8000/api"
r = requests.get(url=url, params={"_id": ObjectId("56933012d5424a0b5853cf3e")})
print(r.text)
