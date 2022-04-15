from time import sleep

from selenium.webdriver.common.by import By

from pages.pageBase import PageBase


class PersonInfoPage(PageBase):
    person_info_xpath = "//div[1]/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/div/img"
    exit_login_xpath = "/html/body/ul/li[3]/span"
    button_exit_login_xpath = "/html/body/div[2]/div/div[3]/button[2]/span"

    def PersonManager(self):
        pass

    def VersionInfo(self):
        pass

    def ExitLogin(self):
        self.driver.find_element(By.XPATH, PersonInfoPage.person_info_xpath).click()
        sleep(4)
        self.driver.find_element(By.XPATH, PersonInfoPage.exit_login_xpath).click()
        sleep(2)
        self.driver.find_element(By.XPATH, PersonInfoPage.button_exit_login_xpath).click()

    def checkExitLoginOK(self):

        sleep(2)
        text_plain = self.driver.find_element(By.XPATH, "/html/body/div/div/form/label/span[2]/span").text

        if text_plain == '记住密码':
            # print('退出登录: Success')
            self.logger.info('退出登录: Success')
            return True
        else:
            # print('退出登录: Failed')
            self.logger.error('退出登录: Failed')
            return False
