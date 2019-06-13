from selenium import webdriver
from tqdm import tqdm

import random
import time
import os


class Form:
    def __init__(self):
        self.url = 'https://docs.google.com/forms/d/e/1FAIpQLSdoX7YZbt3cTJ' \
                   'BIW55voWHSecnMp2cm3d5s5wCTJPUbd_rhbg/viewform'

        self.path = os.path.abspath(os.getcwd() + os.sep + os.pardir + os.sep +
                                    os.pardir + '/Drivers/chromedriver')
        self.driver = webdriver.Chrome(os.path.abspath(self.path))

        self.iterator = 1

        self.lists_ = [
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[3]/div/span/div/label[8]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[3]/div/span/div/label[9]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[3]/div/span/div/label[10]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[3]/div/span/div/label[11]/div[2]/div/div[3]/div'
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[3]/div/span/div/label[4]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[3]/div/span/div/label[5]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[3]/div/span/div/label[6]/div[2]/div/div[3]/div',
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[3]/div/span/div/label[5]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[3]/div/span/div/label[6]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[3]/div/span/div/label[8]/div[2]/div/div[3]/div'
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[3]/div/span/div/label[3]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[3]/div/span/div/label[4]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[3]/div/span/div/label[5]/div[2]/div/div[3]/div'
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[3]/div/span/div/label[8]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[3]/div/span/div/label[9]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[3]/div/span/div/label[10]/div[2]/div/div[3]/div'
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[3]/div/span/div/label[6]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div',
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[3]/div/span/div/label[8]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[3]/div/span/div/label[9]/div[2]/div/div[3]/div'
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[8]/div/div[3]/div/span/div/label[4]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[8]/div/div[3]/div/span/div/label[5]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[8]/div/div[3]/div/span/div/label[6]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[8]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div'
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[9]/div/div[3]/div/span/div/label[4]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[9]/div/div[3]/div/span/div/label[5]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[9]/div/div[3]/div/span/div/label[6]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[9]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div'
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[10]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[10]/div/div[3]/div/span/div/label[8]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[10]/div/div[3]/div/span/div/label[9]/div[2]/div/div[3]/div'
            ],
            [
                None,
                None,
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[11]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[11]/div/div[3]/div/span/div/label[8]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[11]/div/div[3]/div/span/div/label[9]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[11]/div/div[3]/div/span/div/label[10]/div[2]/div/div[3]/div'
            ],
            [
                None,
                None,
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[12]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[12]/div/div[3]/div/span/div/label[8]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[12]/div/div[3]/div/span/div/label[9]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[12]/div/div[3]/div/span/div/label[10]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[12]/div/div[3]/div/span/div/label[11]/div[2]/div/div[3]/div'
            ],
            [
                None,
                None,
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[13]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[13]/div/div[3]/div/span/div/label[8]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[13]/div/div[3]/div/span/div/label[9]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[13]/div/div[3]/div/span/div/label[10]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[13]/div/div[3]/div/span/div/label[11]/div[2]/div/div[3]/div'
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[14]/div/div[3]/div/span/div/label[4]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[14]/div/div[3]/div/span/div/label[5]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[14]/div/div[3]/div/span/div/label[6]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[14]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div'
            ],
            [
                None,
                None,
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[15]/div/div[3]/div/span/div/label[6]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[15]/div/div[3]/div/span/div/label[7]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[15]/div/div[3]/div/span/div/label[8]/div[2]/div/div[3]/div',
            ],
            [
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[16]/div/div[3]/div/span/div/label[3]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[16]/div/div[3]/div/span/div/label[4]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[16]/div/div[3]/div/span/div/label[5]/div[2]/div/div[3]/div',
                '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[16]/div/div[3]/div/span/div/label[6]/div[2]/div/div[3]/div'
            ]
        ]

    def access_page(self):
        self.driver.get(self.url)

    def fill_form(self):
        for element in self.lists_:
            try:
                self.driver.find_element_by_xpath(
                    random.choice(element)).click()
            except Exception as e:
                e.args
                continue

    def submit_form(self):
        sleep = random.randint(1, 300)
        for i in tqdm(range(sleep), total=sleep,
                      desc='Iteration Number {}'.format(self.iterator)):
            time.sleep(1)

        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div').click()

    def __call__(self, *args, **kwargs):
        while True:
            self.access_page()
            self.fill_form()
            self.submit_form()

            self.iterator += 1


if __name__ == '__main__':
    Form().__call__()
