import unittest
from time import sleep
from api.baseApi import log
from selenium import webdriver


class PageBase(unittest.TestCase):
    """所有WEB页面基类"""
    Firefox_driver = webdriver.Firefox()
    logger = log()

    def __init__(self):
        self.driver = PageBase.Firefox_driver
        # 获取百度URL
        self.baseurl = "http://192.168.100.123"

    def setUp(self) -> None:
        # 获取firefox驱动
        # self.driver = webdriver.Firefox()

        # 设置窗口最大化
        self.driver.maximize_window()

        # 设置等待时间
        self.driver.implicitly_wait(30)

        # # 获取百度URL
        # self.baseurl = "http://192.168.100.123"

    def tearDown(self) -> None:
        sleep(1)
        self.driver.quit()
