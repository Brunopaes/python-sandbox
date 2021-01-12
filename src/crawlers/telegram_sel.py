# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup

import time


class ETA:
    def __init__(self):
        self.path = r'D:\PythonProjects\Personal\python-sandbox\drivers' \
                    r'\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, options=self.options)
        self.url = 'https://web.telegram.org/'

        self.driver.get(self.url)

    # Used in __call__
    def select_chat(self):
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app"]/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]'
            '/ul/li[1]'
        ).click()

    # Used in __call__
    def get_last_message(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        return soup.find_all('div', {
            'class': 'im_message_text'
        })[-1].text.lower()

    # Used in verify_eta
    def send_message(self):
        input_box = self.driver.find_element_by_xpath(
            '//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/'
            'div[3]/div[2]/div/div/div/form/div[2]/div[5]'
        )
        input_box.send_keys('This is the way')
        input_box.send_keys(Keys.ENTER)

    def __call__(self, *args, **kwargs):
        input()
        self.select_chat()
        while True:
            msg = self.get_last_message()
            if msg == 'this is the way':
                self.send_message()
                time.sleep(0.7)


if __name__ == '__main__':
    ETA().__call__()
