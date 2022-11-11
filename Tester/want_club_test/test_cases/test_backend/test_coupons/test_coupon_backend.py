import os
import sys
import json
import pytest
from common.excel_handler import excelUtil
from common.requests_handler import HandleRequests
from common.loggers_handler import logzeros

# 解决warning: UserWarning: Workbook contains no default style, apply openpyxl's default
import warnings
warnings.simplefilter('ignore')

sys.path.append("..")


# 优惠券测试用例路径
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
                         'test_data/want_backend'
                         '/coupon_cases.xlsx')
# 读取优惠券测试用例excel文件
excelUtil.load_excel(file_path)
# 获取优惠券测试用例excel文件中的sheet
excelUtil.get_sheet_by_name("Sheet1")

# 实例化封装好的请求类
req = HandleRequests()


class TestCouponStore:
    def test_list(self,open_Background):
        headers = {"accessToken": open_Background}
        logzeros.info(headers)
        # 获取第一行的数据，获取活动列表数据
        test_data = excelUtil.get_row_value(1)
        # 取出可用的url、method等数据
        url, method, is_json, payload = test_data[1], test_data[2], test_data[4], test_data[5]
        # 发起请求
        res = req.visit(url=url, method=method, data=payload, is_json=is_json, headers=headers)
        # 对接口返回数据进行校验
        try:
            assert res.status_code == 200
            logzeros.info('用例执行成功')
            logzeros.info(f'该用例的返回参数为{res.json()}')
        except AssertionError as e:
            logzeros.error('用例执行失败')
            logzeros.error(f'该用例的返回参数为{res.json()}')
            raise e


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__), 'test_coupon_backend.py')
    pytest.main(['-vs', path])
