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

        elem = self.driver.find_element_by_xpath('//span[contains(text(),"Lucas Leonel")]')
        elem.click()

        msg = ['Hello', 'There!']

        for i in range(1000):
            for j in range(len(msg)):
                input_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                input_box.send_keys(msg[j])
                input_box.send_keys(Keys.ENTER)
                time.sleep(5)

    def main(self):
        self.search()


if __name__ == '__main__':
    obj = Scraper()
    obj.main()
