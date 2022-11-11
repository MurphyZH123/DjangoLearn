import sys
import os
import pytest
import random
from common.requests_handler import HandleRequests
from common.ymal_handler import yamlUtil
from common.excel_handler import excelUtil
from common.loggers_handler import logzeros

# 解决warning: UserWarning: Workbook contains no default style, apply openpyxl's default
import warnings

warnings.simplefilter('ignore')

req = HandleRequests()
sys.path.append("..")

# 测试用例文件位置
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
                         'test_data/want_backend'
                         '/test_create_coupon.yaml')
# 读取yaml文件中的数据
data = yamlUtil.read_yaml(file_path)

# 售货机券码和主题门店券码
excel_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
                          'test_data/want_backend/coupons_code001.xlsx')


def generate_coupon_excel():
    # 读取excel文件
    excelUtil.load_excel(excel_path)
    # 获取sheet
    excelUtil.get_sheet_by_name("工作表1")
    # 获取所选区间的数据
    data_list = excelUtil.get_cell_by_inner(1, 20, 1, 1)
    # print(data_list[-1])
    # # 取出要使用的字符串str，数字code
    data_str = data_list[-1].split('0')[0]
    data_code = data_list[-1].split('l')[1]
    # 拼接新的code
    new_data_list = []
    i = 0
    while i < 20:
        data_code = int(data_code) + 1
        new_data_list.append(str(data_str) + str(data_code).zfill(4))
        i += 1
    # 将新的优惠券编码写入文档
    for i in range(len(new_data_list)):
        row = int(i + 1)
        value = str(new_data_list[i])
        excelUtil.write_data_cell(row=row, col=1, value=value, path=excel_path)
    # 获取全部数据
    exl_data = excelUtil.get_excel_data()
    return exl_data


class TestNewCoupon:
    @pytest.mark.parametrize("req_data", data)
    def test_New_coupons(self, req_data, open_Background):
        headers = {"accessToken": open_Background}
        url, method, is_json, payload = req_data["url"], req_data["method"], req_data["is_json"], req_data["data"]
        res = req.visit(url=url, method=method, data=payload, is_json=is_json, headers=headers)
        try:
            assert res.status_code == 200
            logzeros.info(f'{req_data["data"]["couponName"]}用例接口走通')
            logzeros.info(f'该用例的返回参数为{res.json()}')
        except AssertionError as e:
            logzeros.error('用例执行失败')
            logzeros.error(f'该用例的返回参数为{res.json()}')
            raise e
        
    # @pytest.mark.skip(reason="暂时不需要执行编辑券")
    def test_edit_coupon(self, open_Background):
        headers = {"accessToken": open_Background}
        url, method, is_json, payload = data[6]['url'], data[6]['method'], data[6]['is_json'], data[6]['data']
        res = req.visit(url=url, method=method, data=payload, is_json=is_json, headers=headers)
        # 对接口返回数据进行校验
        try:
            assert res.status_code == 200
            logzeros.info('创建兑换券-微信代金券用例接口走通')
            logzeros.info(f'该用例的返回参数为{res.json()}')
        except AssertionError as e:
            logzeros.error('用例执行失败')
            logzeros.error(f'该用例的返回参数为{res.json()}')
            raise e