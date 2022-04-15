from time import sleep

from selenium.webdriver.common.by import By

from api.baseApi import get_info_by_cfg
from pages.pageBase import PageBase


class LoginPage(PageBase):
    """登录WEB管理端"""

    def __init__(self):
        super().__init__()
        pass

    def loginWeb(self, userinfo):
        """登录"""

        # 打开数据配置文件,读取配置信息
        # cfg_info = get_info_by_cfg(filename)

        # for 遍历用户信息
        # for userinfo in cfg_info:
        self.userName = userinfo['username']
        self.passWord = userinfo['pwd']
        # print('username:%s, pwd:%s' % (self.userName, self.passWord))
        self.logger.debug('username:%s, pwd:%s' % (self.userName, self.passWord))

        # 打开登录界面
        self.driver.get(self.baseurl + '/#/login')

        # 定位账号输入框，清空输入框，输入账号
        self.driver.find_element(By.XPATH, '//input[@name="username"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(self.userName)
        sleep(1)
        # 定位密码输入框，清空输入框，输入密码
        self.driver.find_element(By.XPATH, '//input[@name="password"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(self.passWord)
        # 定位登录按钮，点击登录
        self.driver.find_element(By.XPATH, '//button').click()

    def checkLoginOk(self):
        # if 页面包含VSAP，则证明登录成功
        if '首页' in self.driver.page_source:
            # print('登录成功')
            self.logger.info('登录成功')
            return True
        else:
            # print('登录失败')
            self.logger.error('登录失败')
            self.driver.get_screenshot_as_file('../pics/logError_' + self.userName + '.png')
            return False

    def getCookie(self):
        cookies = self.driver.get_cookies()
        # print('all cookies:', cookies)
        for cookie in cookies:
            if cookie['name'] == 'PHPSESSID':
                # print('cookie ', cookie)
                self.logger.debug('cookie %s' % cookie)
                return cookie

    def getToken(self):
        token = self.driver.execute_script('return sessionStorage.getItem("token");')
        # print('token', token)
        self.logger.debug('token', token)
        return token


    
