"""
作用于test_coupons模块
用于获取登录后台的token和name
"""
import pytest


@pytest.fixture()
def open_Background(login):
    name, token = login
    print('获取到token:%s' % token)
    return token



