# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

path = r'D:\PythonProjects\Personal\python-sandbox\drivers\chromedriver.exe'

driver = webdriver.Chrome(path)

driver.get('https://trade.coinext.com.br/trade.html')


