# coding=utf-8

import pytest
from pages.LoginPage import LoginProxy


class TestLoginPage:
    """登录"""

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username, pwd", [('administrator', '123456')])
    def test_login(self, username, pwd):
        login_proxy = LoginProxy()
        ret = login_proxy.login(username, pwd)
        assert '首页' in ret
