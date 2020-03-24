from selenium import webdriver
import time


class Scraper(object):
    def __init__(self):
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/misc/05.4 - Python_Playground/drivers/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, chrome_options=self.options)
        self.url = 'https://web.whatsapp.com'

    def access_page(self):
        self.driver.get(self.url)

        input()

        elem = self.driver.find_element_by_xpath('//span[contains(text(),"Boiçucanga The Mission")]')
        elem.click()

        # message = self.driver.find_elements_by_css_selector('#main > div._3zJZ2 > div > div > div._9tCEa > div:nth-child(11) > div')
        message = self.driver.find_element_by_class_name('_3_7SH Zq3Mc tail')

        print(len(message))

        for i in message:
            print(i.text)

    def __call__(self, *args, **kwargs):
        self.access_page()

        input()


if __name__ == '__main__':
    Scraper()()
