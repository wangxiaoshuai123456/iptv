# coding=utf-8
from time import sleep

from selenium.webdriver.common.by import By

from api import baseApi
from api.baseApi import *
import pytest
import allure_pytest
import allure_commons
import pytest_ordering
import pytest_rerunfailures
import requests
from api.baseApi import log

logger = log()


class TestLoginPage:
    """登录"""
    driver = 0
    baseurl = ''

    # @pytest.mark.skip()
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username, pwd", [('administrator', '123456')])
    def test_logining(self, username, pwd, manager_brower):
        """测试登录"""
        TestLoginPage.driver, TestLoginPage.baseurl = manager_brower
        # 获取URL
        # TestLoginPage.baseurl = my_baseurl

        # 打开登录界面
        TestLoginPage.driver.get(TestLoginPage.baseurl + '/#/login')

        # 定位账号输入框，清空输入框，输入账号
        TestLoginPage.driver.find_element(By.XPATH, '//input[@name="username"]').clear()
        TestLoginPage.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(username)
        sleep(1)
        # 定位密码输入框，清空输入框，输入密码
        TestLoginPage.driver.find_element(By.XPATH, '//input[@name="password"]').clear()
        TestLoginPage.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(pwd)
        # 定位登录按钮，点击登录
        TestLoginPage.driver.find_element(By.XPATH, '//button').click()
        sleep(2)
        # 断言登录成功
        assert '首页' in TestLoginPage.driver.page_source
        # cookies = self.driver.get_cookies()
        # ret = False

    # @pytest.mark.skip()
    @pytest.mark.run(order=2)
    def test_save_token_cookie(self, set_global_cookie, set_global_token):

        cookies = TestLoginPage.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'PHPSESSID':
                set_global_cookie(cookie)
                logger.debug('get global_cookie:%s' % cookie)
                break

        token = TestLoginPage.driver.execute_script('return sessionStorage.getItem("token");')

        logger.debug('get global_token:%s' % token)
        set_global_token(token)
        assert cookie and token

    # def test_set_addr(self, set_global_addr):
    #     addr = 'qwert'
    #     set_global_addr(addr)
    #     assert True
    #
    # def test_get_addr(self, get_global_addr):
    #     addr = get_global_addr
    #     logger.debug('wsp:addr: %s' % addr)
    #     assert addr
