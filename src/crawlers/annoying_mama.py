from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time


class AnnoyingMama:
    def __init__(self):
        self.path = r'C:\Users\bruno\PycharmProjects\python-sandbox\drivers\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, options=self.options)
        self.url = 'https://web.whatsapp.com'

    def access_page(self):
        self.driver.get(self.url)

        input()

        chat = self.driver.find_element_by_xpath('//span[contains(text(),"Rato")]')
        chat.click()

        for i in range(10000):
            input_box = self.driver.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys('LIGA AIII')
            input_box.send_keys(Keys.ENTER)

            time.sleep(0.1)

    def __call__(self, *args, **kwargs):
        self.access_page()


if __name__ == '__main__':
    AnnoyingMama().__call__()