#!-*- coding: utf8 -*-
from selenium.webdriver.support.ui import Select
from selenium import webdriver

import helpers


class NexusRPR:
    def __init__(self):
        self.driver = webdriver.Chrome(
            r'D:\PythonProjects\Personal\python-sandbox\drivers'
            r'\chromedriver.exe'
        )
        self.credentials = helpers.read_json('credentials.json')
        self.url = 'https://banco_abc.nexusweb.com.br/'

    # Used in __call__
    def filling_form(self):
        """This function fills the website's form.

        Returns
        -------

        """
        Select(
            self.driver.find_element_by_xpath('//*[@id="cboCampo"]')
        ).select_by_index(2)

        cpf = self.driver.find_element_by_xpath('//*[@id="txtValor"]')
        cpf.send_keys(self.credentials.get('cpf'))

        password = self.driver.find_element_by_xpath('//*[@id="txtSENHA"]')
        password.send_keys(self.credentials.get('token'))

        captcha = self.driver.find_element_by_xpath('//*[@id="captchacode"]')
        captcha.send_keys(helpers.ocr(r'data/images/a.png'))

        Select(
            self.driver.find_element_by_xpath('//*[@id="cboLocal"]')
        ).select_by_index(1)

        self.driver.find_element_by_xpath('//*[@id="btOk"]').click()

        self.driver.switch_to.alert.accept()

        input()

    # Used in __call__
    def opening_and_screening(self):
        """This function opens the webdriver and screenshots.

        Returns
        -------

        """
        self.driver.get(self.url)
        self.driver.fullscreen_window()
        self.driver.save_screenshot(r'data/images/a.png')

    def __call__(self, *args, **kwargs):
        self.opening_and_screening()
        helpers.crop_image('data/images/a.png', (870, 600, 1050, 650))
        self.filling_form()


if __name__ == '__main__':
    NexusRPR().__call__()
