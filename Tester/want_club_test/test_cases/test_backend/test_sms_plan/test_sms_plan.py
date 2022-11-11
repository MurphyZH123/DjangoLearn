import os
import sys
import json
import pytest
from common.ymal_handler import yamlUtil
from common.requests_handler import HandleRequests
from common.loggers_handler import logzeros

# 解决warning: UserWarning: Workbook contains no default style, apply openpyxl's default
import warnings
warnings.simplefilter('ignore')

sys.path.append("..")

# 测试用例文件位置
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
                         'test_data/want_backend'
                         '/test_create_coupon.yaml')
# 读取yaml文件中的数据
data = yamlUtil.read_yaml(file_path)

# 实例化封装好的请求类
req = HandleRequests()


class TestCouponStore:
    def test_createPlan(self,open_Background):
        headers = {"accessToken": open_Background}
        url, method, is_json, payload = data[0]['url'], data[0]['method'], data[0]['is_json'], data[0]['data']
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
    path = os.path.join(os.path.dirname(__file__), 'test_sms_plan.py')
    pytest.main(['-vs', path])
