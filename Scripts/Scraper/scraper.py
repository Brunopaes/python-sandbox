from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


class Scraper(object):

    def __init__(self):
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Misc/05.4 - Python_Playground/Drivers/chromedriver'
        self.driver = webdriver.Chrome(self.path)
        self.url = 'https://web.whatsapp.com'

    def search(self):
        self.driver.get(self.url)
        time.sleep(15)

        elem = self.driver.find_element_by_xpath('//span[contains(text(),"Guilherme Heitzmann")]')
        elem.click()

        for i in range(10):
            input_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys('Treme')
            input_box.send_keys(Keys.ENTER)
            time.sleep(1)

    def main(self):
        self.search()


if __name__ == '__main__':
    obj = Scraper()
    obj.main()
