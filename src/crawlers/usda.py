# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm

import pandas
import time


class USDA:
    def __init__(self):
        self.path = r'C:\Users\bruno\PycharmProjects\python-sandbox\drivers' \
                    r'\chromedriver.exe'
        self.driver = webdriver.Chrome(self.path)
        self.url = 'https://www.nrcs.usda.gov/Internet/FSE_DOCUMENTS/' \
                   'nrcseprd1512826.html'
        self.pickle_path = r'C:\Users\bruno\PycharmProjects\python-sandbox' \
                           r'\data\files\pickle.rick'

    def selecting(self, id_):
        """

        Parameters
        ----------
        id_

        Returns
        -------

        """
        time.sleep(5)
        selection = Select(self.driver.find_element_by_id(id_)).options
        for option in tqdm(selection[1:]):
            option.click()
            time.sleep(50)
            self.filtering(BeautifulSoup(self.driver.page_source, 'html5lib'))

    def filtering(self, html):
        """This function filters and searches the main table into the html
        file.

        Parameters
        ----------
        html

        Returns
        -------

        """
        table = pandas.read_html(str(html.find('table')))
        try:
            old_table = pandas.read_pickle(self.pickle_path)
        except FileNotFoundError:
            old_table = pandas.DataFrame()

        merged_table = old_table.append(table)
        merged_table.to_pickle(self.pickle_path)

    def __call__(self, *args, **kwargs):
        self.driver.get(self.url)
        self.selecting('selectId1')


if __name__ == '__main__':
    USDA().__call__()
