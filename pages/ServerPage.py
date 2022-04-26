# coding=utf-8
from time import sleep

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from selenium.webdriver.common.by import By

from pages.pageBase import PageBase, HandleBase


class ServerPage(PageBase):
    """启用禁用服务"""

    def __init__(self):
        # super().__init__()
        # 打开登录界面

        # #导入cookie token
        # self.import_cookie_token()
        # # 打开服务页面
        # self.driver.get(self.baseurl + '/#/001base/service/servs')

        # 下线按钮
        self.OffLineButton = By.XPATH, "//div/div/div[2]/div[2]/section/div/div/div[1]/button[5]/span"
        # 上线按钮
        self.OnLineButton = By.XPATH, "//div/div/div[2]/div[2]/section/div/div/div[1]/button[4]/span"

        # 后台服务元素、是否在线元素
        self.serverPathBase = "/html/body/div[1]/div/div[2]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/"
        self.serverInfos = (
            {
                "serverName": "北清外域服务", \
                "serverPath": (By.XPATH, self.serverPathBase + "tr[1]/td[2]/div/span"), \
                "OnlineStatusPath": (By.XPATH, self.serverPathBase + "/tr[1]/td[6]/div/span")},
            {
                "serverName": "录像存储服务", \
                "serverPath": (By.XPATH, self.serverPathBase + "tr[2]/td[2]/div/span"), \
                "OnlineStatusPath": (By.XPATH, self.serverPathBase + "/tr[2]/td[6]/div/span")},
            {
                "serverName": "外域管理服务", \
                "serverPath": (By.XPATH, self.serverPathBase + "tr[3]/td[2]/div/span"), \
                "OnlineStatusPath": (By.XPATH, self.serverPathBase + "/tr[3]/td[6]/div/span")},
            {
                "serverName": "中心管理服务", \
                "serverPath": (By.XPATH, self.serverPathBase + "tr[4]/td[2]/div/span"), \
                "OnlineStatusPath": (By.XPATH, self.serverPathBase + "/tr[4]/td[6]/div/span")},
            {
                "serverName": "设备接入服务", \
                "serverPath": (By.XPATH, self.serverPathBase + "tr[5]/td[2]/div/span"), \
                "OnlineStatusPath": (By.XPATH, self.serverPathBase + "/tr[5]/td[6]/div/span")},
            {
                "serverName": "媒体转发服务", \
                "serverPath": (By.XPATH, self.serverPathBase + "tr[6]/td[2]/div/span"), \
                "OnlineStatusPath": (By.XPATH, self.serverPathBase + "/tr[6]/td[6]/div/span")})

    # 定位服务元素
    def find_servers(self, location):
        return self.get_element(location)

    # 定位上线按钮元素
    def find_OnLineButton(self):
        return self.get_element(self.OnLineButton)

    # 定位下线按钮元素
    def find_OffLineButton(self):
        return self.get_element(self.OffLineButton)

    # 定位 是否在线的状态显示元素
    def find_OnlineStatus(self, location):
        return self.get_element(location)


# 定义操作层类
class HandleServer(HandleBase):
    server_page = ServerPage()

    # 勾选服务元素
    def click_server_checkbox(self, location):
        self.server_page.find_servers(location).click()

    # 点击下线按钮元素
    def click_OffLineButton(self):
        self.server_page.find_OffLineButton().click()

    # 点击上线按钮元素
    def click_OnLineButton(self):
        self.server_page.find_OnLineButton().click()

    # 获取 在线元素 的文本信息 是否 在线/不在线
    def check_OnlineStatus(self, location):
        text = self.server_page.find_OnlineStatus(location).text
        return text



# 定义业务层类
class ServerProxy:
    handle_server = HandleServer()
    serverInfos = handle_server.server_page.serverInfos


    def disable_servers(self):

        #导入cookie token
        self.handle_server.server_page.import_cookie_token()
        # 打开服务页面
        self.handle_server.server_page.driver.get(self.handle_server.server_page.baseurl + '/#/001base/service/servs')

        ret = True
        for server in self.serverInfos:
            self.handle_server.click_server_checkbox(server["serverPath"])
            self.handle_server.click_OffLineButton()
            text = self.handle_server.check_OnlineStatus(server["OnlineStatusPath"])
            if text != "不在线":
                ret = False
        return ret

    def enable_servers(self):
        # 打开服务页面
        self.handle_server.server_page.driver.get(self.handle_server.server_page.baseurl + '/#/001base/service/servs')
        ret = True
        for server in self.serverInfos:
            self.handle_server.click_server_checkbox(server["serverPath"])
            self.handle_server.click_OnLineButton()
            text = self.handle_server.check_OnlineStatus(server["OnlineStatusPath"])
            if text != "在线":
                ret = False
        return ret



