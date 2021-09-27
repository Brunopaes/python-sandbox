# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from helpers import read_json

import datetime
import pyodbc
import pandas
import time


# Exercise 01 - python version
# Excel version on reply e-mail body
def int_to_datetime(int_date):
    """Function for parsing int to datetime.

    Parameters
    ----------
    int_date : int
        Number representing integer.

    Returns
    -------
    date_time : datetime.datetime
        Parsed datetime.

    """
    return datetime.datetime.fromtimestamp(int_date).strftime(
        "%d-%m-%Y %H:%M:%S"
    )


# Exercise 03
def pandas_operation(path=r"data\Tabela_exercicio2.csv",
                     encoding='utf-8'):
    """Function for aggregating shares revenue (prod. sum.) by client.

    Parameters
    ----------
    path : str
        CSV file path.

    encoding : str
        Pandas read csv encoding.

    Returns
    -------
    df : pandas.DataFrame
        Aggregated dataframe.

    """
    return pandas.DataFrame(
        pandas.read_csv(
            path,
            encoding=encoding,
            index_col='Cliente',
            sep=';'
        )[['QTD', 'PREÇO']].prod(axis=1).groupby('Cliente').sum()
    ).rename(columns={0: 'Financeiro em ações'})


# Exercise 03
def db_connection():
    """Function for connecting, creating and

    Returns
    -------

    """
    db_credentials = read_json('data/sql-connection.json')

    conn = pyodbc.connect(
        "Driver={};Server={};Database={};uid={};pwd={};".format(
            db_credentials.get('driver'),
            db_credentials.get('server'),
            db_credentials.get('database'),
            db_credentials.get('user'),
            db_credentials.get('password')
        )
    )

    conn.cursor().execute("""
        CREATE TABLE RV.exp_acoes (
            Cliente INTEGER PRIMARY KEY,
            Financeiro FLOAT NOT NULL
        );
        
        INSERT INTO RV.exp_acoes (Cliente, FInanceiro) VALUES (1, 96000);
        INSERT INTO RV.exp_acoes (Cliente, FInanceiro) VALUES (2, 250000);
        INSERT INTO RV.exp_acoes (Cliente, FInanceiro) VALUES (3, 20500);
    """)

    conn.commit()
    conn.close()


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
                                   r'-sandbox\drivers\chromedriver.exe'):
        self.driver = webdriver.Chrome(driver_path)
        self.url = 'https://www.google.com/'
        self.time_buffer = 2

    def opening_webdriver(self):
        """Function for opening the chrome webdriver.

        Returns
        -------

        """
        self.driver.get(self.url)

    def filling_google_search(self):
        """Function for filling google search bar.

        Returns
        -------

        """
        search_bar = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/form/div[1]/div[1]'
            '/div[1]/div/div[2]/input'
        )

        search_bar.send_keys('XP INC')
        search_bar.send_keys(Keys.ENTER)

    def accessing_website(self):
        """Function for accessing first indexed result.

        Returns
        -------

        """
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
