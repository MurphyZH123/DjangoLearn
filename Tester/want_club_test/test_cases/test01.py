import sys
import os
import pytest
import random
from common.requests_handler import HandleRequests
from common.ymal_handler import yamlUtil
from common.loggers_handler import logzeros

# 解决warning: UserWarning: Workbook contains no default style, apply openpyxl's default
import warnings
warnings.simplefilter('ignore')

req = HandleRequests()
sys.path.append("..")

# 测试用例文件位置
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_data/want_backend'
                                                                     '/test_create_coupon.yaml')

# data = yamlUtil.read_yaml(file_path)
# print(data)

for i in range(21,31):
    code = 'wzjlbshjbm'
    code = code + str(i)
    print(code)


