import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import time


def calc_eta():
    avengers = datetime.datetime.today().replace(day=25, month=4, year=2019, hour=0, minute=1, second=0, microsecond=0)
    date = datetime.datetime.today() - avengers

    m, s = divmod(date.seconds, 60)
    h, m = divmod(m, 60)

    return '+{:d} horas {:02d} minutos {:02d} segundos'.format(h, m, s)


class ETA:
    def __init__(self):
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/misc/05.4 - Python_Playground/drivers/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, chrome_options=self.options)
        self.url = 'https://web.whatsapp.com'

        self.driver.get('http://web.whatsapp.com')

    def click_endgame(self):
        self.driver.find_element_by_xpath('//span[contains(text(),"Verônica Brandt")]').click()

    def get_last_message(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        return soup.find_all('span', {'class': 'selectable-text invisible-space copyable-text'})[-1].text.lower()

    def verify_eta(self, text):
        message_list = text.split(' ')
        if 'eta' in message_list:
            self.send_eta()

        else:
            print('não foi')

    def send_eta(self):
        input_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        input_box.send_keys(str(calc_eta()))
        input_box.send_keys(Keys.ENTER)

    def __call__(self, *args, **kwargs):
        input()

        self.click_endgame()
        time.sleep(5)
        while True:
            self.verify_eta(self.get_last_message())


if __name__ == '__main__':
    ETA().__call__()
