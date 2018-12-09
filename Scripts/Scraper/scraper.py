from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


class Scraper(object):

    def __init__(self):
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Misc/05.4 - Python_Playground/Drivers/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, chrome_options=self.options)
        self.url = 'https://web.whatsapp.com'
        self.time = 6

    def search(self):
        self.driver.get(self.url)
        time.sleep(self.time)

        elem = self.driver.find_element_by_xpath('//span[contains(text(),"Gustavo Fiusa")]')
        elem.click()

        msg = 'O empenho em analisar o fenômeno da Internet é uma das consequências de todos os recursos funcionais envolvidos. Desta maneira, o aumento do diálogo entre os diferentes setores produtivos deve passar por modificações independentemente do impacto na agilidade decisória.'

        for i in range(15):
            # for j in range(len(msg)):
            input_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(msg)
            input_box.send_keys(Keys.ENTER)
            time.sleep(90)

    def main(self):
        self.search()


if __name__ == '__main__':
    obj = Scraper()
    obj.main()
