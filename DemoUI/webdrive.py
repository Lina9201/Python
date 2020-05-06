# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 11:10
# @Author  : zhuxuefei

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://172.23.1.2/console')
print(driver.title)
driver.quit()