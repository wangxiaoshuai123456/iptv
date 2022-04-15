from pages.PersonInfoPage import PersonInfoPage
from test_case.testCaseBase import TestCaseBase


class TestCasePersonInfoPage(TestCaseBase):
    """个人信息页面"""

    def test_ExitLogin(self):
        """测试退出登录"""
        print('test_ExitLogin')
        person_info = PersonInfoPage()
        person_info.ExitLogin()
        ret = person_info.checkExitLoginOK()
        self.assertTrue(ret, '断言：退出登录：失败')
