from ImmocInterface.base.runMethod import RunMethod
from ImmocInterface.data.get_data import GetData

class run_test:
    def __init__(self):
        self.run_method =RunMethod()
        self.data = GetData()

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
            header = self.data.get_is_header(i)
            print(header)
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
            return res


if __name__=='__main__':
    run = run_test()
    run_result = run.go_on_run()
    print(run_result.json())

