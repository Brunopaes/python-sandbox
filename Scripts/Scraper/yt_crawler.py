from selenium import webdriver
import time


class Scraper(object):

    def __init__(self):
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Misc/05.4 - Python_Playground/Drivers/chromedriver'
        self.driver = webdriver.Chrome(self.path)
        self.url = 'https://www.youtube.com/watch?v=6YPd1Foae_Q'
        self.time = 254

    def search(self):
        while True:
            self.driver.get(self.url)
            time.sleep(self.time)

    def main(self):
        self.search()


if __name__ == '__main__':
    obj = Scraper()
    obj.main()
