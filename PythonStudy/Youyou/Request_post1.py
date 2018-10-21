# -*- coding:utf-8 -*-

import requests
import urllib3
urllib3.disable_warnings()

payload = {"Username": "feifei妹纸",
           "Password": "zxfw779616131",
           "Remember": True}

header = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "_ga=GA1.2.1024364476.1515327000;_gid=GA1.2.838719747.1521725726;ASP.NET_SessionId=24weai1hcb4eosg4k1h3hnyn;SERVERID=34e1ee01aa40e94e2474dffd938824db|1521727418|1521727401",
"Host":"passport.cnblogs.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}

r = requests.post('https://passport.cnblogs.com/user/signin', data=payload, headers=header, verify=False)

print(r.text)
print(r.json())


