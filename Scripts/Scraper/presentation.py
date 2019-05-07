from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import time


class Message:
    def __init__(self):
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Misc/05.4 - Python_Playground/Drivers/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, chrome_options=self.options)
        self.url = 'https://web.whatsapp.com'

        self.driver.get('http://web.whatsapp.com')

    def get_unread(self):
        try:
            unread_chat = self.driver.find_element_by_css_selector('.OUeyt')
            unread_chat.click()

            time.sleep(2)

            self.get_last_message()

        except Exception:
            pass

    def get_source_code(self):
        html = self.driver.page_source
        return BeautifulSoup(html, 'html5lib')

    def get_last_message(self):
        soup = self.get_source_code()

        lst_msg = soup.find_all('span', {'class': 'selectable-text invisible-space copyable-text'})
        try:
            msg = lst_msg[-1].text

            input_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(msg)
            input_box.send_keys(Keys.ENTER)

        except Exception:
            pass

    def __call__(self, *args, **kwargs):
        print('Starting API')
        input()

        while True:
            self.get_unread()


if __name__ == '__main__':
    Message().__call__()
