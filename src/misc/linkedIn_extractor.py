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

        self.progress = pandas.read_csv(
            'data/profiles_progress.csv'
        )

        self.profiles_to_run = self.checking_progress()

        self.credentials = {
            'username': '',
            'password': '',
        }

        self.driver = webdriver.Chrome(path)

        self.url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

        self.base_url = None

    def checking_progress(self):
        return set(self.df.Founders).symmetric_difference(self.progress.Founders)

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

        career = self.career(profiles)
        skills = self.skills(profiles)

        return {
            'Founders': [profile_name],
            'StartYear': [career],
            'NumberOfSkills': [skills]
        }

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

        try:
            number_of_skills = int(len(html.find_all(
                    'span', {
                        'class': 'mr1 hoverable-link-text t-bold'
            })) / 2)
        except Exception as e:
            e.args
            number_of_skills = None

        return number_of_skills

    def career(self, profiles):
        self.driver.get(
            '{}/details/experience/'.format(self.base_url[0])
            if profiles[0].attrs.get('aria-hidden') is not None
            else '{}/details/experience/'.format(self.base_url[1])
        )

        time.sleep(2)

        html = self.soup()

        try:
            career_start_year = int(html.find_all(
                'div', {'class': 'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'}
            )[-1].find_all('span')[6].contents[1].text.split(' ')[1])
        except ValueError:
            career_start_year = int(html.find_all(
                'div', {'class': 'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'}
            )[-1].find_all('span')[6].contents[1].text.split(' ')[0])
        except Exception as e:
            e.args
            career_start_year = None

        return career_start_year

    @staticmethod
    def writer(response):
        progress = pandas.read_csv('data/profiles_progress.csv')

        progress = progress.append(
            pandas.DataFrame(response),
            ignore_index=True
        )

        progress.to_csv('data/profiles_progress.csv', index=None)

    def __call__(self, *args, **kwargs):
        self.driver.get(self.url)
        self.login()
        self.driver.maximize_window()

        for founder in tqdm(self.profiles_to_run):
            try:
                response = self.search(founder)
            except IndexError:
                response = {
                    'Founders': [founder],
                    'StartYear': [None],
                    'NumberOfSkills': [None]
                }
            except selenium.common.exceptions.TimeoutException:
                response = {
                    'Founders': [founder],
                    'StartYear': [None],
                    'NumberOfSkills': [None]
                }
            except Exception as e:
                e.args
                response = {
                    'Founder': [founder],
                    'StartYear': [None],
                    'NumberOfSkills': [None]
                }

            self.writer(response)

        self.driver.close()


if __name__ == '__main__':
    LinkedInCrawler(
        r"C:\Users\junio\Desktop\python-sandbox\drivers\chromedriver.exe"
    ).__call__()
