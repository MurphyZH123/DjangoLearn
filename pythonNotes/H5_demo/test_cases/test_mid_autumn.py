import pytest
from common.request_handler import HandleRequests
from common.logs_handler import logzeros
from pytest_assume.plugin import assume

headers = {"SESSION": ''}


class TestMidAutumn:
    req = HandleRequests()
    # @pytest.mark.skip("测试登录，暂时不需要执行")
    def test_login(self):
        url = "https://dev.hotkidclub.com/api/member/registerOrLogin.ctrl"
        method = "post"
        payload = {
            "mobileNumber": '18530880282',
            "validationCode": "1234",
            "channel": "MOBILE",
            "platform": "WEB",
            "campaign": "MEMBER"}
        res = self.req.visit(url=url, method=method, data=payload, is_json=True)
        with assume:
            assert res.status_code == 200
            headers['SESSION'] = res.cookies.get_dict().get('SESSION')
            logzeros.info(res.json())
        with assume:
            assert res.json().get("Response").get("data") is not None
            print("测试成功")
    # @pytest.mark.skip("测试助力签到，暂时不需要执行")

    def test_assistNew(self):
        url = "https://dev.hotkidclub.com/api/campaign/attendance/share/assistNew.ctrl"
        method = "post"
        payload = {"shareCode": "6283NklUM", "channel": "其他H5", "mid": "DoubleCheck"}
        res = self.req.visit(url=url, method=method, data=payload, is_json=True)
        with assume:
            assert res.status_code == 200
            logzeros.info(res.json())
        with assume:
            assert res.json().get("Response") is not None


if __name__ == '__main__':
    pytest.main(['-vs', '/Users/00422829/Documents/H5_demo/test_cases/test_mid_autumn.py'])
