from TCRCInterface.base.runMethod import RunMethod
from TCRCInterface.data.get_data import GetData
from TCRCInterface.util.common_util import CommonUtil
from TCRCInterface.data.dependent_data import dependent_data
import requests
import json


class run_test:
    def __init__(self):
        self.run_method =RunMethod()
        self.data = GetData()
        self.util = CommonUtil()

    def go_on_run(self):
        paas_count = []
        fail_count = []
        res = None
        rows_count = self.data.get_case_lines()
        print(rows_count)
        for i in range(1, rows_count):
            print(i)
            url = self.data.get_run_url(i)
            method = self.data.get_method(i)
            print(method)
            is_run = self.data.get_is_run(i)
            print(is_run)
            data = self.data.get_requests_data(i)
            print(data)
            expect = self.data.get_expect_data(i)
            header = self.data.get_is_header(i)
            print(header)
            depend_case = self.data.isdepend(i)
            if depend_case != None:
                self.depend_data = dependent_data(depend_case)
                print(depend_case)
                depend_response_data = self.depend_data.get_for_key(i)
                print(depend_response_data)
                depend_key = self.data.get_depend_data(i)
                print(depend_key)
                header[depend_key] = depend_response_data
                print(method, url, data, header)
            # if is_run:
                if method == 'post':
                    res = requests.post(url=url, data=json.dumps(data), headers=header)
                print(res.json())
            else:
                res = self.run_method.run_main(method, url, data, header)
                print(res)
                # if depend_case != None:
                #     # 获取依赖的响应数据
                #     depend_response_data = self.depend_data.get_for_key(i)
                #     # 获取依赖的key
                #     depend_key = self.data.get_depend_data(i)
                #     header[depend_key] = depend_response_data

            if self.util.is_contain(expect, res):
                self.data.write_result(i, 'Pass')
                paas_count.append(i)
                # resp = json.loads(res)
                # print(type(res))
                # print(resp['data'])
                print("测试通过")
            else:
                self.data.write_result(i, 'Fail')
                fail_count.append(i)
                print("测试失败")
            print(len(paas_count))
            print(len(fail_count))

if __name__=='__main__':
    run = run_test()
    run.go_on_run()


