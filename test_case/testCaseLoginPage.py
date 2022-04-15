from time import sleep

from api import baseApi
from api.baseApi import *
from pages.LoginPage import LoginPage
from test_case.testCaseBase import TestCaseBase


class TestCaseLoginPage(TestCaseBase):
    """登录"""

    def test_login(self):
        """测试登录"""
        print('test_login')

        cfg_info = get_info_by_cfg(file_name='D:/pycharm/iptv/data/userInfo.csv')

        login_page = LoginPage()

        for userinfo in cfg_info:
            login_page.loginWeb(userinfo)
            sleep(1)
            ret = login_page.checkLoginOk()
            self.assertTrue(ret, msg='断言-测试登录失败-')

        baseApi.cookie = login_page.getCookie()
        baseApi.token = login_page.getToken()
        printCookieAndToken()

