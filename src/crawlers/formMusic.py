from selenium.webdriver.support.ui import Select
from selenium import webdriver
from tqdm import tqdm

import random
import os


class Forms:
    def __init__(self):
        self.url = 'https://docs.google.com/forms/d/e/1FAIpQLSdoMqzH_' \
                   'JHUUQ4iISgS8EsiITBYmP6jVRRleQfcjz1SdH794Q/viewform'
        self.path = \
            os.path.abspath(os.getcwd() + os.sep + os.pardir + os.sep +
                            os.pardir + '/drivers/chromedriver')
        self.driver = webdriver.Chrome(self.path)

        self.f_list = \
            open(os.path.abspath(os.getcwd() + '/data/first_names.txt'), 'r',
                 encoding='utf-8').read().split(',')

        self.l_list = \
            open(os.path.abspath(os.getcwd() + '/data/last_names.txt'), 'r',
                 encoding='utf-8').read().split(',')


    def access_page(self):
        self.driver.get(self.url)

    def generate_random_names(self):
        f_name = random.choice(self.f_list)
        l_name = random.choice(self.l_list)

        return f_name.strip(' '), l_name.strip(' ')

    def fill_form(self):
        f_name = self.generate_random_names()[0]
        l_name = self.generate_random_names()[1]

        name = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]'
                                                 '/div[2]/div[1]/div/div[2]/'
                                                 'div/div[1]/div/div[1]/input')
        name.send_keys('{} {}'.format(f_name, l_name))

        ra = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]'
                                               '/div[2]/div[2]/div/div[2]/div/'
                                               'div[1]/div/div[1]/input')

        ra.send_keys('11{}{}{}'.format(random.randint(5, 9),
                                       random.randint(1, 2),
                                       '{num:04d}'.format(
                                           num=random.randint(0000, 9999))))

        course = Select(self.driver.find_element_by_xpath('//*[@id="mG61Hd"]'
                                                          '/div/div[2]/div[2]'
                                                          '/div[3]/div/div[2]'
                                                          '/div[1]/div[1]/'
                                                          'div[1]'))

        course.select_by_index(random.randint(0, 7))

    def __call__(self, *args, **kwargs):
        self.access_page()
        self.fill_form()

        input()


if __name__ == '__main__':
    Forms().__call__()
