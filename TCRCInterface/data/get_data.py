from TCRCInterface.util.operation_excel import Operation_excel
from TCRCInterface.util.operation_json import Operation_json
from TCRCInterface.data.data_config import global_var

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

    # 获取预期结果
    def get_expect_data(self, row):
        col = int(global_var.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == " ":
            return None
        return expect

    # 写入用例执行结果
    def write_result(self, row, value):
        col = int(global_var.get_result())
        self.opera_excel.write_value(row, col, value)

    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = int(global_var.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    # 判断是否有case依赖
    def isdepend(self, row):
        col = (int)(global_var.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_depend_data(self, row):
        col = (int)(global_var.get_field_depend())
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data

if __name__=='__main__':
    opera_excel = Operation_excel()
    testdata = GetData()
    col = (int)(global_var.get_case_depend())
    case_id = opera_excel.get_cell_value(6, col)
    print(testdata.isdepend())










