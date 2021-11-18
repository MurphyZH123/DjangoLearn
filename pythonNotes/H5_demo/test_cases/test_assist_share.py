import pytest
from pytest_assume.plugin import assume
from common.request_handler import HandleRequests
from common.logs_handler import logzeros

headers_dict = {'SESSION': ''}


class TestAssistShare:
    req = HandleRequests()

    # @pytest.mark.skip(reason="测试登录，暂时不需要执行")
    def test_share_login(self):
        url = "https://dev.hotkidclub.com/api/member/registerOrLogin.ctrl"
        method = "post"
        payload = {
            "mobileNumber": '17634380268',
            "validationCode": "1234",
            "channel": "MOBILE",
            "platform": "WEB",
            "campaign": "MEMBER"}
        res = self.req.visit(url=url, method=method, data=payload, is_json=True)
        with assume:
            assert res.status_code == 200
            print(res.cookies.get_dict().get('SESSION'))
            headers_dict['SESSION'] = (res.cookies.get_dict().get('SESSION'))
            print(headers_dict)
            logzeros.info(res.json())
        with assume:
            assert res.json().get("Response").get("data") is not None
            print("测试成功")

    # @pytest.mark.skip(reason="测试助力分享，暂时不需要测试")
    def test_share_assist(self):
        url = "https://dev.hotkidclub.com/api/cpn/autumn/assistance.ctrl"
        method = "post"
        payload = {"shareCode": "uczX6S2T"}
        headers = headers_dict
        print(headers)
        res = self.req.visit(url=url, method=method, headers=headers, data=payload, is_json=True)
        with assume:
            assert res.status_code == 200
            logzeros.info(res.json())
        with assume:
            assert res.json().get("Response") is not None
            print("测试成功")


if __name__ == '__main__':
    pytest.main(['-vs', '/Users/00422829/Documents/H5_demo/test_cases/test_assist_share.py'])
