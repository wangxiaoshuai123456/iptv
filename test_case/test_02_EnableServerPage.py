# coding=utf-8
from time import sleep
from selenium.webdriver.common.by import By
# from pages.ServerPage import ServerPage
import pytest
import allure_pytest
import allure_commons
import pytest_ordering
import pytest_rerunfailures
import requests

from api.baseApi import log

logger = log()


class TestEnableServerPage:
    """启用禁用服务"""
    cookie = {}
    token = ''
    driver = 0
    baseurl = ''

    serverInfos = ({"serverName": "北清服务", \
                    "serverXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/span", \
                    "OnlineStatusXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div/span"},
                   {"serverName": "录像服务", \
                    "serverXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[2]/td[2]/div/span", \
                    "OnlineStatusXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[2]/td[6]/div/span"},
                   {"serverName": "外域服务", \
                    "serverXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[3]/td[2]/div/span", \
                    "OnlineStatusXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[3]/td[6]/div/span"},
                   {"serverName": "中心服务", \
                    "serverXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[4]/td[2]/div/span", \
                    "OnlineStatusXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[4]/td[6]/div/span"},
                   {"serverName": "设备服务", \
                    "serverXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[5]/td[2]/div/span", \
                    "OnlineStatusXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[5]/td[6]/div/span"},
                   {"serverName": "媒体服务", \
                    "serverXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[6]/td[2]/div/span", \
                    "OnlineStatusXpath": "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[6]/td[6]/div/span"})

    @pytest.mark.run(order=4)
    def test_get_cookie(self, get_global_cookie):
        TestEnableServerPage.cookie = get_global_cookie
        # name = get_global_cookie['name']
        logger.debug('\nwsp-cookie :%s' % TestEnableServerPage.cookie)
        assert TestEnableServerPage.cookie

    @pytest.mark.run(order=5)
    def test_get_token(self, get_global_token):
        TestEnableServerPage.token = get_global_token

        logger.debug('\n wsp-token:%s' % TestEnableServerPage.token)
        assert TestEnableServerPage.token

    def import_cookie_token(self):
        """测试启用禁用服务"""

        # 打印cookie token的值
        logger.debug('\ncookie :%s\n  token:%s' % (TestEnableServerPage.cookie, TestEnableServerPage.token))

        # 1 初始化配置 cookie and token   '/#/login'
        # TestEnableServerPage.driver.get(TestEnableServerPage.baseurl + '/#/001base/base')
        TestEnableServerPage.driver.get(TestEnableServerPage.baseurl + '/#/login')
        # 添加cookie
        TestEnableServerPage.driver.add_cookie(TestEnableServerPage.cookie)
        # 添加token
        js_token = 'sessionStorage.setItem("token", "' + TestEnableServerPage.token + '")'

        TestEnableServerPage.driver.execute_script(js_token)

    def operate(self):
        # 3 定位 服务页面
        ServerPageXpath = "//div[@id='app']/div/div/div[2]/div/div/ul/div[2]/li/ul/div[2]/a/li/span"
        # RecordServerXpath = "//div/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/span"
        OffLineButton = "//div/div/div[2]/div[2]/section/div/div/div[1]/button[5]/span"
        OnLineButton = "//div/div/div[2]/div[2]/section/div/div/div[1]/button[4]/span"
        sleep(2)
        TestEnableServerPage.driver.find_element(By.XPATH, ServerPageXpath).click()
        sleep(5)

        for serverInfo in TestEnableServerPage.serverInfos:
            # 4 定位 ”录像服务“，后点击
            TestEnableServerPage.driver.find_element(By.XPATH, serverInfo['serverXpath']).click()

            # 5 定位“下线”按钮，后点击
            TestEnableServerPage.driver.find_element(By.XPATH, OffLineButton).click()
            sleep(2)

            # 6 定位 ”录像服务“，后点击
            TestEnableServerPage.driver.find_element(By.XPATH, serverInfo['serverXpath']).click()

            # 7 定位“上线”按钮，后点击
            TestEnableServerPage.driver.find_element(By.XPATH, OnLineButton).click()
            sleep(2)

    def checkOnLineStatus(self):
        ret = True
        # 8 刷新页面
        # 9 定位 在线状态
        # 10 获取 在线状态的文本，判断是否是“在线”，是 返回True
        TestEnableServerPage.driver.refresh()
        sleep(1)
        # 定位状态是否在线
        for serverInfo in TestEnableServerPage.serverInfos:
            isline = TestEnableServerPage.driver.find_element(By.XPATH, serverInfo['OnlineStatusXpath'])
            ret = isline.text
            if ret == '在线':
                # print('重启 %s: %s' % (serverInfo['serverName'], "Success"))
                logger.info('重启 %s: %s' % (serverInfo['serverName'], "Success"))
            else:
                ret = False
                # print('重启 %s: %s' % (serverInfo['serverName'], "Failed"))
                logger.error('重启 %s: %s' % (serverInfo['serverName'], "Failed"))

        return ret

    @pytest.mark.run(order=6)
    def test_enable_server(self, manager_brower):
        TestEnableServerPage.driver, TestEnableServerPage.baseurl = manager_brower
        self.import_cookie_token()

        # TestEnableServerPage.driver.refresh()  # 刷新

        # 2 get请求 打开首页
        TestEnableServerPage.driver.get(TestEnableServerPage.baseurl + '/#/001base/base')
        sleep(2)
        self.operate()
        assert self.checkOnLineStatus()
