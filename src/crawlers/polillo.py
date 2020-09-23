# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup

import time


class ETA:
    def __init__(self):
        self.path = r'D:\PythonProjects\Personal\python-sandbox\drivers\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, options=self.options)
        self.url = 'https://web.whatsapp.com'

        self.driver.get('http://web.whatsapp.com')

        self.message = ""

    # Used in __call__
    def click_endgame(self):
        self.driver.find_element_by_xpath(
            '//span[contains(text(),"ESPM+Matias Game Call")]'
        ).click()

    # Used in __call__
    def get_last_message(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        return soup.find_all('span', {
            'class': '_3Whw5 selectable-text invisible-space copyable-text'
        })[-1].text.lower(), soup.find_all('span', {
            'class': '_3Whw5 selectable-text invisible-space copyable-text'
        })[-2].text.lower()

    # Used in __call__
    def verify_eta(self, text_1, text_2):
        message_list = text_1.split(' ')

        if '!copy' in message_list:
            self.message = text_2
        elif '!paste' in message_list:
            if len(message_list) == 1:
                for i in range(5):
                    self.send_eta()
            else:
                for i in range(int(message_list[1])):
                    self.send_eta()
        else:
            print('não foi')

    # Used in verify_eta
    def send_eta(self):
        input_box = self.driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        )
        input_box.send_keys(self.message)
        input_box.send_keys(Keys.ENTER)

    def __call__(self, *args, **kwargs):
        input()
        self.click_endgame()
        while True:
            self.verify_eta(*self.get_last_message())


if __name__ == '__main__':
    ETA().__call__()
