from TCRCInterface.util.operation_excel import Operation_excel
from TCRCInterface.base.runMethod import RunMethod
from TCRCInterface.data.get_data import GetData
from jsonpath_rw import jsonpath, parse
import json


# 处理数据依赖相关的
class dependent_data:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = Operation_excel()
        self.data = GetData()

    # 通过case_depend字段就是case_id去获取相应用例id的行内容
    def case_line_data(self, case_id):
        rows_data = self.opera_excel.get_row_value(case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_rows_num("TCRC-001")
        print(row_num)
        request_data = self.data.get_requests_data(row_num)
        header = self.data.get_is_header(row_num)
        method = self.data.get_method(row_num)
        url = self.data.get_run_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_for_key(self, row):
        dependent_data = self.data.get_depend_key(row)
        print(dependent_data)
        response_data = self.run_dependent()
        print(response_data)
        jsonpath_expr = parse(dependent_data)
        madle = jsonpath_expr.find(response_data)
        print(madle)
        return [match.value for match in madle][0]


