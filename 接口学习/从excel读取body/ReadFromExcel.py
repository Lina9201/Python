import xlrd
import openpyxl
import requests
import json

class OperationExcleData(object):
    """对excel进行操作，包括读取请求参数，和填写操作结果"""
    def __init__(self, excelFile):
        self.excelFile = excelFile
        self.caseList = []

    """传入excel用例名称，其中元素是{}，每个{}包含字段和对应值的键对值"""
    # def getCaseList(self):
    #     readExcel = xlrd.open_workbook(fileName)
    #     # 获取excel的第一个sheet
    #     sheet = readExcel.sheet_by_index(0)
    #     print(sheet.name)
    #     # 获取excel的行数
    #     trows = sheet.nrows
    #     for n in range(1, trows):
    #         tmpdict = {}
    #         tmpdict["name"] = sheet.cell_value(n, 2)
    #         tmpdict["description"] = sheet.cell_value(n, 3)
    #         self.caseList.append(tmpdict)
    #     return self.caseList

    # """写入用例执行结果到excel中"""
    # def writeCaseResult(self, result):
    #     writeExcel = openpyxl.load_workbook(fileName)
    #     try:
    #         # 获取excel的第一个sheet
    #         wtable = writeExcel.get_sheet_by_name("Token鉴权")
    #         wtable.cell(1, 4).value = result
    #         writeExcel.save(fileName)
    #     except Exception as e:
    #         raise
    #     finally:
    #         pass

    def getCaseList(self, excelFile):
        readExcel = xlrd.open_workbook(excelFile)
        # 获取excel的第一个sheet
        sheet = readExcel.sheet_by_index(0)
        # 获取excel的行数和列数
        trows = sheet.nrows
        tcols = sheet.ncols
        tmpdict = {}
        for i in range(1, trows):
            for j in range(2,tcols):
                case_key = sheet.cell_value(0, j)
                case_value = sheet.cell_value(i, j)
                tmpdict[case_key] = case_value
            print(self.caseList.append(tmpdict))
        return tmpdict



if __name__ == '__main__':
    requesturl = "http://172.50.10.42:8000/admin/v1/regions"
    fileName = u'资源池.xlsx'
    ed = OperationExcleData(fileName)
    headers = {"User-Agent": "automation",
               "content-type": "application/json;charset=UTF-8",
               "T-AUTH-TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJjNDQ0MDVjYS00ZDJmLTRiZTYtODQwNS1jYTRkMmZlYmU2ZjYiLCJzdWIiOiJ6aHV4dWVmZWkiLCJpYXQiOjE1NzA1MDAyMzAsImlzcyI6IkFwYWNoZVN5bmNvcGUiLCJleHAiOjE1NzA1MTQ2MzAsIm5iZiI6MTU3MDUwMDIzMH0.Px6ht5ryFMRzn9CN6hcdWibZ9IZVLT5eEzDQfq9-cDRuvKFOl4_kcGaIA-ycNrpzSGATgLdv3Au1k_Zx8H0ZYA"}
    ed.getCaseList(fileName)
    # for caseDict in ed.getCaseList(fileName):
    #     print(caseDict)
    #     createResourcepool = requests.post(url=requesturl,
    #                                      data=json.dumps(caseDict),
    #                                      headers=headers)
    #     print(createResourcepool.text)

        # ed.writeCaseResult(createResourcepool.text)

