import sys
import os
from common.requests_handler import HandleRequests
from common.excel_handler import excelUtil

# 解决warning: UserWarning: Workbook contains no default style, apply openpyxl's default
import warnings
warnings.simplefilter('ignore')

req = HandleRequests()
sys.path.append("..")

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                         'test_data/want_club/concurrency_cases.xlsx')

# 读取excel文件
excelUtil.load_excel(file_path)
# 获取某个Sheet1的数据
excelUtil.get_sheet_by_name("工作表1")
# 获取第一行的数据，登录信息
test_data = excelUtil.get_row_value(1)


def login():
    url, method,is_josn, payload = test_data[1], test_data[2],test_data[4], test_data[5]
    res = req.visit(url=url, method=method, data=payload, is_json=is_josn)
    header = res.cookies.get_dict()
    return header


login = login()