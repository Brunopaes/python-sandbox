from selenium import webdriver
from bs4 import BeautifulSoup


class Scraper(object):

    def __init__(self):
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Misc/05.4 - Python_Playground/Drivers/chromedriver'
        self.driver = webdriver.Chrome(self.path)
        self.url = 'https://docs.google.com/forms/d/e/1FAIpQLSc9cen8bcj65UTOko_EWHng0xMTn5rYUsMMNqgHhAErveF36w/viewform'
        self.time = 3

    def bs(self):
        html = BeautifulSoup(self.url, 'html.parser')
        print(html)

    def search(self):
        self.bs()

        # while True:
        #     self.driver.get(self.url)
        #
        #     name = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input')
        #     name.send_keys('Pedro Gucciardi')
        #
        #     self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div[2]/div/content/div/label[3]').get_attribute('TECH')

    def main(self):
        self.search()


if __name__ == '__main__':
    obj = Scraper()
    obj.main()
