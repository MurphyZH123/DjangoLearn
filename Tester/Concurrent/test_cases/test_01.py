import os
import sys
import json
import grequests
from common.excel_handler import excelUtil
from test_cases.login import login

# 解决warning: UserWarning: Workbook contains no default style, apply openpyxl's default
import warnings

warnings.simplefilter('ignore')

sys.path.append("..")

# 测试用例路径
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                         'test_data/want_club/concurrency_cases.xlsx')
# 读取测试用例excel文件
excelUtil.load_excel(file_path)

# 获取测试用例excel文件中的sheet
excelUtil.get_sheet_by_name("工作表1")

# 获取第x行测试数据，可修改
test_data = excelUtil.get_row_value(2)

# 将取出的数据进行赋值
url, method, payload = test_data[1], test_data[2], test_data[5]
payload = json.loads(payload)  # 将str转成dict

N = 4  # 并发请求次数，可修改

req_list = [grequests.post(url, json=payload, cookies=login) for i in range(N)]  # 并发post请求列表
# req_list = [grequests.get(url,json=payload,cookies=login) for i in range(N)]# 并发get请求列表
res_list = grequests.map(req_list)  # 并行发送，等最后一个运行完后返回
for i in range(len(res_list)):
    if res_list[i].status_code == 200:
        print(res_list[i].status_code, res_list[i].text)
    else:
        print(res_list[i].status_code)

