import xlrd

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

    def get_data(self):
        data1 = xlrd.open_workbook(self.filename)
        tables1 = data1.sheet_by_index(self.sheet_id)
        return tables1

    def get_lines(self):
        tables = self.data
        return tables.nrows

    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)


if __name__=='__main__':
    oper = Operation_excel()
    print(oper.get_cell_value(1, 4))
    print(oper.get_lines())



