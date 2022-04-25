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

from pages.ServerPage import ServerProxy
from utils import UtilsDriver


class TestEnableServerPage:
    """启用禁用服务"""

    def setup_class(self):
        self.server_proxy = ServerProxy()

    def teardown_class(self):
        sleep(5)
        UtilsDriver.quit_driver()

    @pytest.mark.run(order=2)
    def test_disble_server(self):
        assert self.server_proxy.disable_servers()

    @pytest.mark.run(order=3)
    def test_enable_server(self):
        assert self.server_proxy.enable_servers()
