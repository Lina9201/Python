# -*- coding:utf-8 -*-

from selenium import webdriver
import requests
import os
import time

# 指定chromedriver的位置，如果在默认路径，这两行可以省略。
executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

os.environ["webdriver.chrome.driver"] = executable_path

# 定义配置对象
options = webdriver.ChromeOptions()

# 指定用户的配置地址，并加载至配置对象中。
options.add_argument("--user-data-dir="+r"C:/Users/administrator/AppData/Local/Google/Chrome/User Data/Default")

# 此处注意，有两个参数，后面那个参数，一定要写成 chrome_options=XX的形式，否则运行报错。
driver = webdriver.Chrome(executable_path, chrome_options=options)

time.sleep(3)
driver.get("https://home.cnblogs.com/u/Lina-zhu/followers/")

# 获取浏览器的cookies
cookies = driver.get_cookies()
print(cookies)

# requests添加登录的cookies
# 浏览器的cookies获取到后，用request创建一个session，在session里添加登录成功后的cookies
#s = requests.session()
# 添加cookies到CookieJar
#c = requests.cookies.RequestCookieJar()
#for i in cookies:
#   c.set(i["name"], i["value"])
#s.cookies.update(c)
