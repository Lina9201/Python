from TCRCInterface.data.dependent_data import dependent_data
from TCRCInterface.util.operation_excel import Operation_excel
import requests
import json
from jsonpath_rw import jsonpath, parse
def send_requests(s, testdata):
        '''封装requests请求'''
        method = testdata["请求方式"]
        url = testdata["url"]
        header = eval(testdata["header"])
        data = eval(testdata["请求数据"])
        test_nub = testdata['ID']
        expect = eval(testdata['预期结果'])
        depend_case = testdata['依赖id']
        depend_data = testdata['依赖数据']
        if depend_case == "":
            print("*******正在执行用例：-----  %s  ----**********" % test_nub)
            print("请求方式：%s, 请求url:%s" % (method, url))
            print("预期结果: %s" % expect)
            res = s.request(method=method, url=url, headers=header, data=data)
            print("请求响应结果: %s" % res.text)
        else:
            dependdata = dependent_data(depend_case)
            depend_response_data = dependdata.run_dependent(depend_case)
            jsonpath_expr = parse(depend_data)
            madle = jsonpath_expr.find(depend_response_data)
            depend_response_data_new = [match.value for match in madle][0]
            depend_data_new = testdata['依赖数据所属字段']
            header[depend_data_new] = depend_response_data_new
            res = s.request(method=method, url=url, headers=header, data=json.dumps(data))
            print("*******正在执行用例：-----  %s  ----**********" % test_nub)
            print("请求方式：%s, 请求url:%s" % (method, url))
            print("预期结果: %s" % expect)
            print("依赖ID: %s" % depend_case)
            print("依赖数据: %s" % depend_data)
            print("依赖数据的值: %s" % depend_response_data_new)
            print("请求响应结果: %s" % res.text)
            return res

if __name__ == "__main__":
    data = Operation_excel().dict_data()
    print(data[0])
    s = requests.session()
    res = send_requests(s, data[0])





