# coding=utf-8
import unittest
from TCRCInterface.util import HTMLTestRunner_api
import os

# 用例路径
case_path = "E:\\Pycharm\\TCRCInterface\\case"
# 报告存放地址
report_path = "E:\\Pycharm\\TCRCInterface\\report"
print(report_path)

def all_case():
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern="test*.py",
                                                top_level_dir=None)
    print(discover)
    return discover

def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    htmlreport = reportpath+r"\result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner_api.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__ == "__main__":
    cases = all_case()
    run_case(cases)


