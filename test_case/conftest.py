import pytest
from time import sleep
from selenium import webdriver

global_cookie = {"name": "wsp"}
global_token = '123456'
# driver = webdriver.Firefox()
baseurl = "http://192.168.43.123"
driver = None




@pytest.fixture(scope='module')
def manager_brower():
    print('前置处理')

    global driver
    if driver is None:
        # 获取firefox驱动  
        driver = webdriver.Firefox()
        # 设置窗口最大化
        driver.maximize_window()
        # 设置等待时间
        driver.implicitly_wait(10)

    yield driver, baseurl

    sleep(1)
    if driver is not None:
        driver.quit()
        driver = None
    print('后置处理')


@pytest.fixture(scope='function')
def set_global_cookie():
    def _set_global_cookie(cookie):
        global global_cookie
        global_cookie = cookie

    return _set_global_cookie
    # sleep(3)
    # cookies = driver.get_cookies()
    # for cookie in cookies:
    #     if cookie['name'] == 'PHPSESSID':
    #         global global_cookie
    #         global_cookie = cookie
    #         logger.debug('get global_cookie:%s' % global_cookie)
    #         return global_cookie


@pytest.fixture(scope='function')
def get_global_cookie():
    global global_cookie
    return global_cookie


@pytest.fixture(scope='function')
def set_global_token():
    def _set_global_token(token):
        global global_token
        global_token = token

    return _set_global_token
    # sleep(3)
    # token = driver.execute_script('return sessionStorage.getItem("token");')
    # global global_token
    # global_token = token
    # logger.debug('get global_token:%s' % global_token)
    # return global_token


@pytest.fixture(scope='function')
def get_global_token():
    global global_token
    return global_token
