"""
作为最外层的conftest.py文件，作用范围为全局的，用来做登录处理
"""

import json
import sys
import os
import pytest
from jsonpath_ng import parse
from common.requests_handler import HandleRequests
from common.excel_handler import excelUtil

# 解决warning: UserWarning: Workbook contains no default style, apply openpyxl's default
import warnings
warnings.simplefilter('ignore')

req = HandleRequests()
sys.path.append("..")

file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                         'test_data/want_backend'
                         '/login_cases.xlsx')

# 读取excel文件
excelUtil.load_excel(file_path)
# 获取某个Sheet1的数据
excelUtil.get_sheet_by_name("Sheet1")
# 获取第一行的数据，登录信息
test_data = excelUtil.get_row_value(1)


@pytest.fixture(scope="session")
def login():
    url, method, header, is_josn, payload = test_data[1], test_data[2], test_data[3], test_data[4], test_data[5]
    header, payload = json.loads(header), json.loads(payload)  # 将str转成dict
    res = req.visit(url=url, method=method, data=payload, is_json=is_josn, headers=header)
    res_json = res.json()  # 将返回结果转成json
    expr = parse("$.Response.token")  # 使用parse来定位json格式数据中的元素
    token = [match.value for match in expr.find(res_json)][0]  # 将所需要的元素提取出来
    name = payload.get("employeeId")  # 提取json数据格式中的元素
    yield name, token
    return token
