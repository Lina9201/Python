# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 15:38
# @Author  : zhuxuefei

class AdminLogin:
    def __int__(self):
        self.host = "http://172.23.1.7/api"
        self.uri = "/v1/tokens"
        self.method = "post"
        self.body = self.Body

    class Body:
        def __int__(self):
            self.username = "zhuxuefei"
            self.password = "1qaz!QAZ"