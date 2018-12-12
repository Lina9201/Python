import xlrd
from xlutils.copy import copy
#打开xlsx文件
#data = xlrd.open_workbook('../dataconfig/InterfaceCases.xlsx')

#print(data.sheet_names())
#获取sheet页,以index为0获取第一个sheet页
#tables = data.sheet_by_index(0)
# 获取表格有多少行
#print(tables.nrows)
# 获取表格中某单元格的值，下标都是从0开始的
#print(tables.cell_value(1, 3))
#print(tables.nrows())

####################################################
# 优化使用类进行封装
class Operation_excel:
    def __init__(self, filename=None, sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
        else:
            self.filename = '../dataconfig/InterfaceCases.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取某个sheet的表格
    def get_data(self):
        data1 = xlrd.open_workbook(self.filename)
        tables1 = data1.sheet_by_index(self.sheet_id)
        return tables1

    # 获取表格中的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取表格中某个单元格的值
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.filename)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.filename)

    # 根据依赖的case_id去获取行号
    def get_rows_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1



    # 根据依赖的case_id去获取对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_rows_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data


    # 根据行号去获取行的内容
    def get_row_value(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id = None):
        if col_id != None:
            self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols




if __name__=='__main__':
    oper = Operation_excel()
    print(oper.get_cell_value(1, 4))
    print(oper.get_lines())



