# coding=utf-8
from time import sleep

import self
from selenium.webdriver.common.by import By

from pages.pageBase import PageBase


class ServerPage(PageBase):
    """启用禁用服务"""

    cookie = {}
    token = ''

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

    def __init__(self):
        super().__init__()

    def EnableServer(self):
        """启用禁用服务"""

        # # 1 初始化配置 cookie and token
        # driver.get(''baseurl + '/#/001base/base')
        # # 添加cookie
        # ''driver.add_cookie(self.cookie)
        # # 添加token
        # js_token = 'sessionStorage.setItem("token", "' + self.token + '")'
        #
        # self.driver.execute_script(js_token)
        #
        # self.driver.refresh()  # 刷新

        # # 2 get请求 打开首页
        # self.driver.get(self.baseurl + '/#/001base/base')
        sleep(2)

        # 3 定位 服务页面
        ServerPageXpath = "//div[@id='app']/div/div/div[2]/div/div/ul/div[2]/li/ul/div[2]/a/li/span"
        # RecordServerXpath = "//div/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/span"
        OffLineButton = "//div/div/div[2]/div[2]/section/div/div/div[1]/button[5]/span"
        OnLineButton = "//div/div/div[2]/div[2]/section/div/div/div[1]/button[4]/span"
        sleep(2)
        self.driver.find_element(By.XPATH, ServerPageXpath).click()
        sleep(5)

        for serverInfo in ServerPage.serverInfos:
            # 4 定位 ”录像服务“，后点击
            self.driver.find_element(By.XPATH, serverInfo['serverXpath']).click()

            # 5 定位“下线”按钮，后点击
            self.driver.find_element(By.XPATH, OffLineButton).click()
            sleep(2)

            # 6 定位 ”录像服务“，后点击
            self.driver.find_element(By.XPATH, serverInfo['serverXpath']).click()

            # 7 定位“上线”按钮，后点击
            self.driver.find_element(By.XPATH, OnLineButton).click()
            sleep(2)

    def checkOnLineStatus(self):
        ret = True
        # 8 刷新页面
        # 9 定位 在线状态
        # 10 获取 在线状态的文本，判断是否是“在线”，是 返回True
        self.driver.refresh()
        sleep(1)
        # 定位状态是否在线
        for serverInfo in ServerPage.serverInfos:
            isline = self.driver.find_element(By.XPATH, serverInfo['OnlineStatusXpath'])
            ret = isline.text
            if ret == '在线':
                # print('重启 %s: %s' % (serverInfo['serverName'], "Success"))
                self.logger.info('重启 %s: %s' % (serverInfo['serverName'], "Success"))
            else:
                ret = False
                # print('重启 %s: %s' % (serverInfo['serverName'], "Failed"))
                self.logger.error('重启 %s: %s' % (serverInfo['serverName'], "Failed"))

        return ret
