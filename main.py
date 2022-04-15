import time
import unittest

from BeautifulReport import BeautifulReport
from test_case.testCaseEnableServerPage import TestCaseEnableServerPage
from test_case.testCaseLoginPage import TestCaseLoginPage
from test_case.testCasePersonInfoPage import TestCasePersonInfoPage
from api.baseApi import log

if __name__ == '__main__':
    # print('start...')
    logger = log()
    logger.info('start...')
    suite = unittest.TestSuite()
    suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestCaseLoginPage), \
                    unittest.defaultTestLoader.loadTestsFromTestCase(TestCaseEnableServerPage),\
                    unittest.defaultTestLoader.loadTestsFromTestCase(TestCasePersonInfoPage)])
    # 打开文件
    now_time = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
    filename = now_time + '_' + 'result.html'
    with open(filename, 'wb') as file:
        # HTMLTestRunner
        # runner = HTMLTestRunner(stream=file, title='HTMLTestRunner测试', description='HTMLTestRunner测试')
        # runner.run(suite)

        # BeautifulReport
        beau_runner = BeautifulReport(suite)
        beau_runner.report(description='IPTV测试', filename=filename, log_path='./report/')
        file.close()
    logger.info('end...')


