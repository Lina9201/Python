from ImmocInterface.util.operation_excel import Operation_excel
from ImmocInterface.util.operation_json import Operation_json
from ImmocInterface.data.data_config import global_var

class GetData:
    def __init__(self):
        self.opera_excel = Operation_excel()
    # 去获取excel中的行数，也就是用例的个数

    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(global_var.get_run())
        run_module = self.opera_excel.get_cell_value(row, col)
        if run_module == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取用例是否携带header
    def get_is_header(self, row):
        col = int(global_var.get_header())
        header = eval(self.opera_excel.get_cell_value(row, col))
        #if header == 'yes':
        return header
        #else:
        #   return None

    # 获取用例的请求方法
    def get_method(self, row):
        col = int(global_var.get_run_away())
        requests_method = self.opera_excel.get_cell_value(row, col)
        return requests_method

    # 获取用例url
    def get_run_url(self, row):
        col = int(global_var.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_requests_data(self, row):
        col = int(global_var.get_dat())
        data = eval(self.opera_excel.get_cell_value(row, col))
        if data == '':
            return None
        else:
            return data

    def get_data_for_json(self, row):
        opera_json = Operation_json()
        request_data = opera_json.get_correctdata(self.get_requests_data(row))
        return request_data

    def get_expect_data(self, row):
        col = int(global_var.get_expect())
        expect = eval(self.opera_excel.get_cell_value(row, col))
        if expect == " ":
            return None
        return expect



