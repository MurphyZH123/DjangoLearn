import pytest
from time import sleep
from pytest_assume.plugin import assume
from common.request_handler import HandleRequests
from common.logs_handler import logzeros

headers = {'SESSION': 0}
person_count = {'count': ''}


class TestMaster:
    req = HandleRequests()

    # @pytest.mark.parametrize('mobileNumber', [18854823673, 15026884569])
    # @pytest.mark.skip(reason="测试登录接口,暂时不需要执行")
    def test_login(self):
        url = "https://dev.hotkidclub.com/api/member/registerOrLogin.ctrl"
        method = "post"
        payload = {
            "mobileNumber": '18854823673',
            "validationCode": "1234",
            "channel": "MOBILE",
            "platform": "WEB",
            "campaign": "MEMBER"}
        res = self.req.visit(url=url, method=method, data=payload, is_json=True)
        sleep(3)
        with assume:
            assert res.status_code == 200
            headers['SESSION'] = res.cookies.get_dict().get('SESSION')
            logzeros.info(res.json())
        with assume:
            assert res.json().get("Response").get("data") is not None
            print("测试成功")

    @pytest.mark.skip(reason="测试是否有登录状态，暂时不需要执行")
    def test_login_info(self):
        url = "https://dev.hotkidclub.com/api/member/info.ctrl"
        method = "get"
        res = self.req.visit(url=url, method=method, headers=headers)
        with assume:
            assert res.status_code == 200
            logzeros.info(res.json())
        with assume:
            assert res.json().get("Response").get("data") is not None
            print("测试成功")

    @pytest.mark.skip(reason="测试参与活动，暂时不需要执行")
    def test_participate(self):
        url = "http://dev.hotkidclub.com/api/cpn/autumn/joinActivity.ctrl"
        method = "get"
        res = self.req.visit(url=url, method=method, headers=headers)
        with assume:
            assert res.status_code == 200
            logzeros.info(res.json())
        with assume:
            assert res.json().get("Response") is not None
            print("测试成功")

    @pytest.mark.skip(reason="测试活动主页面，暂时不需要执行")
    def test_home_page(self):
        url = "http://dev.hotkidclub.com/api/cpn/autumn/main.ctrl"
        method = "get"
        res = self.req.visit(url=url, method=method, headers=headers)
        with assume:
            assert res.status_code == 200
            logzeros.info(res.json())
        with assume:
            assert res.json().get("Response") is not None
            person_count['count'] = res.json().get("Response").get('data').get('count')
            print("测试成功")

    @pytest.mark.skip(reason="测试分享活动，暂时不需要执行")
    def test_share(self):
        url = "http://dev.hotkidclub.com/api/cpn/autumn/share.ctrl"
        method = "get"
        res = self.req.visit(url=url, method=method, headers=headers)
        with assume:
            assert res.status_code == 200
            logzeros.info(res.json())
        with assume:
            assert res.json().get("Response").get("data") is not None
            print("测试成功")

    @pytest.mark.skip(reason="获取优惠券，暂时不需要执行")
    def test_obtain_coupon(self):
        url = "http://dev.hotkidclub.com/api/cpn/autumn/giveCoupon.ctrl"
        method = "get"
        if person_count['count'] == 4:
            res = self.req.visit(url=url, method=method, headers=headers)
            with assume:
                assert res.status_code == 200
                logzeros.info(res.json())
            with assume:
                assert res.json().get("Response").get("data") is not None
                print("测试成功")


if __name__ == "__main__":
    pytest.main(['-vs', "/Users/00422829/Documents/H5_demo/test_cases/test_assist.py"])
