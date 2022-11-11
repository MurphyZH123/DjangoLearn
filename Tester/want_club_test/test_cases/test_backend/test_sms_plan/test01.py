# -*- coding: utf-8 -*-
# @Time : 2022/6/15 6:30 下午
# @Author : 00422829
# @File : test01
# @Project : want_club_test
import os
import json
from common.excel_handler import excelUtil
login_token = [0,1]
# 优惠券测试用例路径
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
                         'test_data/want_backend'
                         '/coupon_cases.xlsx')
# 读取excel文件
excelUtil.load_excel(file_path)
# 获取sheet
excelUtil.get_sheet_by_name("Sheet1")

test_data = excelUtil.get_row_value(1)
header = test_data[3]
header = json.loads(header)
print(type(header))
header["accessToken"] = login_token[0]
print(header)
