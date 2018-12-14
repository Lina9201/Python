# coding:utf-8
import unittest
import ddt
import os
from TCRCInterface.util.operation_excel import Operation_excel
from TCRCInterface.base import SendRequest
import requests
import json

# 获取InterfaceCases.xlsx路径
curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "InterfaceCases.xlsx")
print(curpath)
print(testxlsx)
# 复制InterfaceCases.xlsx文件到report下
report_path = os.path.join(os.path.dirname(curpath), "report")
print(report_path)
reportxlsx = os.path.join(report_path, "result.xlsx")
print(reportxlsx)
testdata = Operation_excel().dict_data()

@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        print("开始执行测试用例")

        # 如果有登录的话，就在这里先登录了
        # writeexcel.copy_excel(testxlsx, reportxlsx) # 复制xlsx

    @ddt.data(*testdata)
    def test_api(self, data):
        # 先复制excel数据到report
        res = SendRequest.send_requests(self.s, data)
        # check = eval(data["实际结果"])
        # print(check)
        # print("检查点->：%s" % check)
        # # 返回结果
        #
        # print("返回实际结果->：%s" % res_text)
        # # 断言
        # self.assertTrue(check in res_text)

if __name__ == "__main__":
    unittest.main()