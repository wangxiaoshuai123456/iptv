from pages.ServerPage import ServerPage
from test_case.testCaseBase import TestCaseBase


class TestCaseEnableServerPage(TestCaseBase):
    """启用禁用服务"""

    def test_EnableServer(self):
        """测试启用禁用服务"""
        print('test_EnableServer')

        server_page = ServerPage()
        server_page.EnableServer()
        ret = server_page.checkOnLineStatus()
        self.assertTrue(ret, msg='断言-测试启用禁用服务:失败')
