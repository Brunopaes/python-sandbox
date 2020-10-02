#!-*- coding: utf8 -*-
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions
from selenium import webdriver

import helpers
import time


class NexusRPR:
    def __init__(self):
        self.driver = webdriver.Chrome(
            r'D:\PythonProjects\Personal\python-sandbox\drivers'
            r'\chromedriver.exe'
        )
        self.credentials = helpers.read_json('credentials.json')
        self.url = 'https://banco_abc.nexusweb.com.br/'
        self.alert = None

    # Used in __call__
    def filling_form(self):
        """This function fills the website's form.

        Returns
        -------

        """
        while True:
            self.driver.save_screenshot(r'data/images/a.png')
            helpers.crop_image('data/images/a.png', (870, 600, 1050, 650))

            Select(
                self.driver.find_element_by_xpath('//*[@id="cboCampo"]')
            ).select_by_index(2)

            cpf = self.driver.find_element_by_xpath('//*[@id="txtValor"]')
            cpf.clear()
            cpf.send_keys(self.credentials.get('cpf'))

            password = self.driver.find_element_by_xpath('//*[@id="txtSENHA"]')
            password.clear()
            password.send_keys(self.credentials.get('token'))

            captcha = self.driver.find_element_by_xpath(
                '//*[@id="captchacode"]')
            captcha.clear()
            captcha.send_keys(helpers.ocr(r'data/images/a.png'))

            Select(
                self.driver.find_element_by_xpath('//*[@id="cboLocal"]')
            ).select_by_index(1)

            self.driver.find_element_by_xpath('//*[@id="btOk"]').click()

            try:
                time.sleep(2)
                alert = self.driver.switch_to.alert
                self.alert = alert.text
                alert.accept()
                break
            except exceptions.NoAlertPresentException:
                pass
        return self.alert

    # Used in __call__
    def opening_and_screening(self):
        """This function opens the webdriver and access the nexus webpage.

        Returns
        -------

        """
        self.driver.get(self.url)
        self.driver.fullscreen_window()

    def __call__(self, *args, **kwargs):
        self.opening_and_screening()
        self.filling_form()


if __name__ == '__main__':
    print(NexusRPR().__call__())
