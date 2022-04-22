# coding=utf-8
from pages.PersonInfoPage import PersonInfoPage
import pytest
import allure_pytest
import allure_commons
import pytest_ordering
import pytest_rerunfailures
import requests


class TestPersonInfoPage:
    """个人信息页面"""

    @pytest.mark.run(order=7)
    def test_exit_login(self):
        """测试退出登录"""
        person_info = PersonInfoPage()
        person_info.ExitLogin()
        assert person_info.checkExitLoginOK()
