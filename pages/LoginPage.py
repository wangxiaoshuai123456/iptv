# coding=utf-8
from time import sleep

from selenium.webdriver.common.by import By

from pages.pageBase import PageBase, HandleBase, set_global_cookie, set_global_token


# 定义对象库层类
class LoginPage(PageBase):
    """登录页面"""

    def __init__(self):
        # super().__init__()
        # 打开登录界面

        self.driver.get(self.baseurl + '/#/login')

        # 用户名输入框
        self.userName = By.NAME, "username"
        # 密码输入框
        self.passWord = By.NAME, "password"
        # 记住密码勾选框
        self.rememberPassWord = By.CSS_SELECTOR, ".el-checkbox__inner"
        # 登录按钮
        self.loginButton = By.TAG_NAME, "button"

    # 定位用户名输入框元素
    def find_userName(self):
        return self.get_element(self.userName)

    # 定位密码输入框元素
    def find_passWord(self):
        return self.get_element(self.passWord)

    # 定位记住密码勾选框元素
    def find_rememberPassWord(self):
        return self.get_element(self.rememberPassWord)

    # 定位登录按钮元素
    def find_loginButton(self):
        return self.get_element(self.loginButton)


# 定义操作层类
class LoginHandle(HandleBase):
    login_page = LoginPage()

    def __init__(self):
        # self.login_page = LoginPage()
        pass

    # 输入用户名
    def input_userName(self, userName):
        self.input_text(self.login_page.find_userName(), userName)

    # 输入密码
    def input_passWord(self, passWord):
        self.input_text(self.login_page.find_passWord(), passWord)

    # 勾选记住登录密码
    def accept_checkbox_rememberPassWord(self):
        self.accept_checkbox(self.login_page.find_rememberPassWord())

    # 点击登录按钮
    def click_loginButton(self):
        self.login_page.find_loginButton().click()

    # 检查登录是否成功, 如果登录成功则提取cookie，token
    def check_login_status(self):
        if '首页' in self.login_page.driver.page_source:
            # # 提取cookie  保存
            cookies = self.login_page.driver.get_cookies()
            for cookie in cookies:
                if cookie['name'] == 'PHPSESSID':
                    set_global_cookie(cookie)
                    break
            # #  提取token 保存
            token = self.driver.login_page.execute_script('return sessionStorage.getItem("token");')
            set_global_token(token)
            return True
        else:
            return False


# 定义业务层类
class LoginProxy:
    login_handle = None

    def __int__(self):
        # self.login_handle = LoginHandle()
        pass

    # 登录功能
    def login(self, userName, passWord):
        self.login_handle = LoginHandle()

        self.login_handle.input_userName(userName)
        self.login_handle.input_passWord(passWord)
        sleep(1)
        self.login_handle.accept_checkbox_rememberPassWord()
        sleep(1)
        self.login_handle.click_loginButton()
        # 检查是否登录成功
        ret = self.login_handle.check_login_status()
        return '首页'
