# -*- coding: utf-8 -*-
import selenium.common.exceptions
from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm

import pandas
import time
import re


class LinkedInCrawler:
    def __init__(self, path):
        self.df = pandas.read_excel(
            'data/Database thesis v2.xlsx',
            sheet_name='Founders'
        )

        self.credentials = {
        }

        self.driver = webdriver.Chrome(path)

        self.url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

        self.base_url = None

    def login(self):
        self.driver.find_element(
            'xpath', '//*[@id="username"]'
        ).send_keys(self.credentials.get('username'))

        self.driver.find_element(
            'xpath', '//*[@id="password"]'
        ).send_keys(self.credentials.get('password'))
        self.driver.find_element(
            'xpath', '//*[@id="organic-div"]/form/div[3]/button'
        ).click()

    def search(self, profile_name):
        search_bar = self.driver.find_element(
            'xpath',
            '//*[@id="global-nav-typeahead"]/input'
        )
        search_bar.clear()
        search_bar.send_keys(profile_name)
        search_bar.send_keys(webdriver.Keys.ENTER)

        time.sleep(3)

        profiles = BeautifulSoup(
            self.driver.page_source, 'html5lib'
        ).find_all('a', {'class': 'app-aware-link'})[:2]

        self.driver.set_page_load_timeout(2)

        self.base_url = (
            profiles[0].attrs.get('href').split('?')[0],
            profiles[1].attrs.get('href').split('?')[0]
        )

        carrer = self.career(profiles)
        # skills = self.skills(profiles)

    def soup(self):
        return BeautifulSoup(self.driver.page_source, 'html5lib')

    def skills(self, profiles):
        self.driver.get(
            '{}/details/skills/'.format(self.base_url[0])
            if profiles[0].attrs.get('aria-hidden') is not None
            else '{}/details/skills/'.format(self.base_url[1])
        )

        time.sleep(2)

        html = self.soup()

    def career(self, profiles):
        self.driver.get(
            '{}/details/experience/'.format(self.base_url[0])
            if profiles[0].attrs.get('aria-hidden') is not None
            else '{}/details/experience/'.format(self.base_url[1])
        )

        time.sleep(2)

        html = self.soup()

        career_start_year = html.find_all(
            'div', {'class': 'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'}
        )[-1].find_all('span')[6].contents[1].text.split(' ')[1]

        return career_start_year

    def __call__(self, *args, **kwargs):
        self.driver.get(self.url)
        self.login()
        self.driver.maximize_window()
        for i in tqdm(list(set(self.df.Founders))):
            try:
                self.search(i)
            except IndexError:
                pass
            except selenium.common.exceptions.TimeoutException:
                pass
        self.driver.close()


if __name__ == '__main__':
    LinkedInCrawler(
        r"E:\PythonProjects\Personal\friday\data\webdriver\chromedriver.exe"
    ).__call__()
