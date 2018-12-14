from TCRCInterface.base.runMethod import RunMethod
from TCRCInterface.util.operation_excel import Operation_excel
from TCRCInterface.data.dependent_data import dependent_data
import requests
import json
def send_requests(s, testdata):
        '''封装requests请求'''
        method = testdata["请求方式"]
        url = testdata["url"]
        header = eval(testdata["header"])
        data = eval(testdata["请求数据"])
        test_nub = testdata['ID']
        expect = eval(testdata['预期结果'])
        depend_case = testdata['依赖id']
        # if depend_case !=None:
        #     depend_data = dependent_data(depend_case)
        #     depend_response_data = depend_data.get_for_key(1)
        #     depend_data = eval(testdata['依赖数据所属字段'])
        #     header[depend_data] = depend_response_data
        #     res = s.request(method=method, url=url, headers=header, data=json.dumps(data))
        #     print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        #     print("请求方式：%s, 请求url:%s" % (method, url))
        #     print("预期结果: %s" % expect)
        #     print("依赖ID: %s" % depend_case)
        #     return res
        # else:
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url:%s" % (method, url))
        print("预期结果: %s" % expect)
        print("依赖ID: %s" % depend_case)
        res = s.request(method=method, url=url, headers=header, data=data)
        print(res)
        print(res.text)
        return res

if __name__ == "__main__":
    data = Operation_excel().dict_data()
    print(data[0])
    s = requests.session()
    res = send_requests(s, data[0])





