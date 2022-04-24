# coding=utf-8
from time import sleep

import pytest

from pages.LoginPage import LoginProxy
from utils import UtilsDriver


class TestLoginPage:
    """登录"""

    def setup_class(self):
        self.login_proxy = LoginProxy()

    def teardown_class(self):
        sleep(5)
        UtilsDriver.quit_driver()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username, pwd", [('administrator', '123456')])
    def test_login(self, username, pwd):
        ret = self.login_proxy.login(username, pwd)
        assert '首页' in ret
