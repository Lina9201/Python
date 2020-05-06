# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 16:22
# @Author  : zhuxuefei
from PythonBasic.PTest.TypeCovert import *
import requests

headers = {'Content-Type': 'application/json'}

class RequestUtil:
    def __int__(self):
        self.header = headers

    def send_request(self):
        # self.url = self.compose_url()
        # 将请求参数对象转换为json
        json_body = obj_to_json(self.body)
        resp_act = self.__send_request(data=json_body)
        # 将相应json结果转换为对象


    # def compose_url(self):


    def __send_request(self,data):
        r = None
        common_condition = dict(url = self.url, headers = self.header)
        if self.method == "get":
            r = requests.get(common_condition)
        elif self.method == "post":
            r = requests.post(common_condition, data=data)
        elif self.method == "put":
            r = requests.post(common_condition, data=data)
        elif self.method == "delete":
            r = requests.post(common_condition)
        if str(r.status_code) == '200':
            response = r.json()
            return response
        else:
            print("接口返回异常")
            return None

