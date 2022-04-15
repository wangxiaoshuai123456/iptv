import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from HTMLTestRunner import HTMLTestRunner


class BaiduTest(unittest.TestCase):
    """测试百度搜索功能"""

    def setUp(self) -> None:
        # 获取firefox驱动
        self.driver = webdriver.Firefox()

        # 设置窗口最大化
        self.driver.maximize_window()

        # 设置等待时间
        self.driver.implicitly_wait(30)

        # 获取百度URL
        self.baseurl = "https://www.baidu.com"

    def test_multiWindows(self):
        """打开百度一下网页"""
        # 打开百度一下网页
        self.driver.get(self.baseurl)
        sleep(2)
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.100.123" + '/#/login')
        sleep(2)
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.100.123" + '/#/001base/base')
        sleep(2)

        # 定位关键字输入框元素
        kw = self.driver.find_element(By.ID, 'kw')

        # 清空输入框
        kw.clear()

        # 输入文字“林志玲”
        kw.send_keys('林志玲')

        # 定位搜索按钮“百度一下”，然后点击
        self.driver.find_element(By.ID, 'su').click()

        # 断言

        # 定位超文本链接“林志玲-知乎”
        text = self.driver.find_element(By.LINK_TEXT, '林志玲 - 知乎').click()
        text = self.driver.find_element(By.LINK_TEXT, '林志玲 - 知乎')
        print('text:', text)

        # 切换至弹窗
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(2)


        # 关闭弹窗
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/button').click()

        # 定位搜索框
        self.driver.find_element(By.ID, 'Popover1-toggle').clear()

        # 输入文字“范冰冰”
        self.driver.find_element(By.ID, 'Popover1-toggle').send_keys('范冰冰')

        # 定位且点击搜索按钮
        self.driver.find_element(By.XPATH,
                                 '//body/div[1]/div/div[2]/header/div[2]/div[1]/div/form/div/div/label/button').click()

        print('end')

    def tearDown(self) -> None:
        sleep(30)
        self.driver.quit()
