from ImmocInterface.base.runMethod import RunMethod
from ImmocInterface.data.get_data import GetData
class run_test:
    def __init__(self):
        self.run_method =RunMethod()
        self.data = GetData()

    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            url = self.data.get_url(i)
            method = self.data.get_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.get_is_header(i)
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
            return res

if __name__=='__main__':
    run = run_test()
    run.go_on_run()

