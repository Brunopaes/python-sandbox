# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup

import requests


def launch_schedule():
    html = BeautifulSoup(
        requests.get('https://spaceflightnow.com/launch-schedule/').content,
        'html5lib'
    )

    mission = html.find_all('span', {'class': 'mission'})
    launch_date = html.find_all('span', {'class': 'launchdate'})
    mission_data = html.find_all('div', {'class': 'missiondata'})

    rocket = []
    new_mission = []
    new_mission_data = []
    new_launch_date = []
    for i, j, k in zip(mission, mission_data, launch_date):
        rocket_, mission_ = i.text.split('•')
        rocket.append(rocket_.strip())
        new_mission.append(mission_.strip())
        new_mission_data.append(j.text)
        new_launch_date.append(k.text)

    message = '{}\n{}\n{}'.format(
        new_mission[rocket.index('Falcon 9')],
        new_launch_date[rocket.index('Falcon 9')],
        new_mission_data[rocket.index('Falcon 9')]
    )

    return message


class ETA:
    def __init__(self):
        self.path = r'E:\PycharmProjects\python-sandbox\drivers' \
                    r'\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, chrome_options=self.options)
        self.url = 'https://web.whatsapp.com'

        self.driver.get('http://web.whatsapp.com')

    # Used in __call__
    def click_endgame(self):
        self.driver.find_element_by_xpath(
            '//span[contains(text(),"ESPM+Matias Game Call")]'
        ).click()

    # Used in __call__
    def get_last_message(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        return soup.find_all('span', {
            'class': '_3Whw5 selectable-text invisible-space copyable-text'
        })[-1].text.lower()

    # Used in __call__
    def verify_eta(self, text):
        message_list = text.split(' ')
        if '!launch' in message_list:
            self.send_eta()
        else:
            print('não foi')

    # Used in verify_eta
    def send_eta(self):
        input_box = self.driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        )
        input_box.send_keys(launch_schedule())
        input_box.send_keys(Keys.ENTER)

    def __call__(self, *args, **kwargs):
        input()

        self.click_endgame()
        while True:
            self.verify_eta(self.get_last_message())


if __name__ == '__main__':
    ETA().__call__()
