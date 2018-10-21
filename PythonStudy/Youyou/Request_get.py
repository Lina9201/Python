# -*- coding:utf-8 -*-

import requests
# 带参数的get请求
par = {"Keywords": "yoyoketang"}
r2 = requests.get('http://zzk.cnblogs.com/s/blogpost', params=par)
print(r2.status_code)
print(r2.text)