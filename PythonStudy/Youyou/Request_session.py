# *-* coding:utf-8 *-*

import requests

url = "https://passport.cnblogs.com/user/signin"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
}

s = requests.session()
r = s.get(url, headers=headers, verify=True)
print(s.cookies)

# 添加登录需要的两个cookie
c = requests.cookies.RequestCookieJar()
c.set()
