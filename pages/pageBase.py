# coding=utf-8


from selenium.webdriver.support.wait import WebDriverWait

from utils import UtilsDriver, log

# BASEURL = "http://192.168.43.123"
BASEURL = "http://127.0.0.1"
global_cookie = {}
global_token = ''


# 定义对象库层基类 用于定位元素
class PageBase:
    logger = log()
    driver = UtilsDriver.get_driver()
    baseurl = BASEURL

    # 初始化获取web驱动
    # def __int__(self):
    #     # self.logger = log()
    #     # self.driver = UtilsDriver.get_driver()
    #     # self.baseurl = BASEURL
    #     pass

    # 定义获取元素的方法
    def get_element(self, location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element

    def import_cookie_token(self):
        """测试启用禁用服务"""

        # 打印cookie token的值
        # logger.debug('\ncookie :%s\n  token:%s' % (TestEnableServerPage.cookie, TestEnableServerPage.token))

        # 1 初始化配置 cookie and token   '/#/login'
        # TestEnableServerPage.driver.get(TestEnableServerPage.baseurl + '/#/001base/base')
        self.driver.get(self.baseurl + '/#/login')
        # 添加cookie
        self.driver.add_cookie(get_global_cookie())
        # 添加token
        js_token = 'sessionStorage.setItem("token", "' + get_global_token() + '")'

        self.driver.execute_script(js_token)



# 定义操作层基类 用于操作元素：对文本元素进行 文本输入等操作
class HandleBase:

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

    def accept_checkbox(self, element):
        element.click()


# 定义处理 cookie token方法
def set_global_cookie(cookie):
    global global_cookie
    global_cookie = cookie


def get_global_cookie():
    global global_cookie
    return global_cookie


def set_global_token(token):
    global global_token
    global_token = token


def get_global_token():
    global global_token
    return global_token
