# -*- coding:utf-8 -*-
__author__ = u'Lina'

from urllib import request
from http import cookiejar

if __name__=='__main':
    # 声明一个cookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器，也就是cookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    response = opener.open('https://citrix.cloud.com')
    # 打印cookie信息
    for item in cookie:
        print(item.name)
        print(item.value)