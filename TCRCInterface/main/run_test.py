from TCRCInterface.base.runMethod import RunMethod
from TCRCInterface.data.get_data import GetData
from TCRCInterface.util.common_util import CommonUtil
import json

class run_test:
    def __init__(self):
        self.run_method =RunMethod()
        self.data = GetData()
        self.util = CommonUtil()

    def go_on_run(self):
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
            print(expect)
            header = self.data.get_is_header(i)
            print(header)
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
                print(res)
                if self.util.is_contain(expect, res):
                    self.data.write_result(i, 'Pass')
                    # resp = json.loads(res)
                    # print(type(res))
                    # print(resp['data'])
                    print("测试通过")
                else:
                    self.data.write_result(i, 'Fail')
                    print("测试失败")


if __name__=='__main__':
    run = run_test()
    run.go_on_run()


