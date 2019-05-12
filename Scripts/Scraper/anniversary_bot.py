#!-*- coding: utf8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup

import pandas
import time


class Anniversary:
    def __init__(self):

        self.df_ = pandas.DataFrame(pandas.read_excel('/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Misc/05.4 - ' 
                                     'Python_Playground/Scripts/Scraper/Data/words_.xlsx'))

        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Misc/05.4 - Python_Playground/Drivers/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, chrome_options=self.options)
        self.url = 'https://web.whatsapp.com'

        self.driver.get('http://web.whatsapp.com')

    def get_unread(self):
        try:
            content = self.driver.find_element_by_css_selector('.OUeyt')
            content.click()

            time.sleep(4)

            self.get_last_message()

        except NoSuchElementException:
            pass

    def get_last_message(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        lst_msg = soup.find_all('span', {'class': 'selectable-text invisible-space copyable-text'})
        try:
            msg = lst_msg[-1].text
            msg_ = msg.lower().split(' ')

            val = self.df_['words'].isin(msg_).tolist()

            if True in val:
                send_m = '{}\n{}\n{}\n\n{}'.format('Oi, eu sou o Bot!',
                                                   'Quanto à sua mensagem, Bruno agradece sua demonstração de afeto',
                                                   'Sua mensagem será salva e assim que possível ele deverá te '
                                                   'responder com os devidos agradecimentos.', 'Att, Bot')

                input_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                input_box.send_keys(send_m)
                input_box.send_keys(Keys.ENTER)

            else:
                send_m = '{}\n{}\n{}\n\n{}'.format('Oi, eu sou o Bot!',
                                                   'Meu material de treinamento é um tanto quanto restrito, sendo assim'
                                                   ' só consigo te responder sobre questões de aniversário.',
                                                   'Digo isso, pois identifiquei que sua mensagem não apresenta '
                                                   'nenhuma demonstração de afeto, portanto, recomendo fortemente que, '
                                                   'em caso de urgencia, busque outros meios de comunicação.',
                                                   'Att, Bot')

                input_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                input_box.send_keys(send_m)
                input_box.send_keys(Keys.ENTER)

        except:
            pass

    def main(self):
        print('QR - blablabla')
        input()

        while True:
            self.get_unread()


if __name__ == '__main__':
    cls1 = Anniversary()
    cls1.main()
