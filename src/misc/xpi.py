# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import datetime
import pyodbc
import pandas
import time


# Exercise 01 - python version
# Excel version on reply e-mail body
def int_to_datetime(int_date):
    return datetime.datetime.fromtimestamp(int_date).strftime(
        "%d-%m-%Y %H:%M:%S"
    )


# Exercise 03
def pandas_operation(path=r"data\Tabela_exercicio2.csv"):
    return pandas.DataFrame(
        pandas.read_csv(
            path,
            encoding='utf-8',
            index_col='Cliente',
            sep=';'
        )[['QTD', 'PREÇO']].prod(axis=1).groupby('Cliente').sum()
    ).rename(columns={0: 'Financeiro em ações'})


# Exercise 03
def db_connection():
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=XP1;'
        'Database=RV;'
        'uid=teste;'
        'pwd=teste123;'
    )


# Exercise 04
def sum_shares():
    """
    SELECT
        SUM(Financeiro) AS Financeiro_SUM
    FROM
        RV.exp_acoes
    """


# Exercise 05
class XPinGooogle():
    def __init__(self, driver_path=r'D:\PythonProjects\Personal\python'
                                   r'-sandbox\drivers\chromedriver.exe',):
        self.driver = webdriver.Chrome(driver_path)
        self.url = 'https://www.google.com/'
        self.time_buffer = 2

    def opening_webdriver(self):
        self.driver.get(self.url)

    def filling_google_search(self):
        search_bar = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/form/div[1]/div[1]'
            '/div[1]/div/div[2]/input'
        )

        search_bar.send_keys('XP INC')
        search_bar.send_keys(Keys.ENTER)

    def accessing_website(self):
        self.driver.find_element_by_xpath(
            '//*[@id="tads"]/div/div/div/div[1]/a'
        ).click()

    def __call__(self, *args, **kwargs):
        self.opening_webdriver()
        self.filling_google_search()
        time.sleep(self.time_buffer)
        self.accessing_website()
        self.driver.maximize_window()
        time.sleep(self.time_buffer * 5)


XPinGooogle().__call__()

