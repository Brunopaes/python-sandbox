from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self):
        self.url = 'http://www2.aneel.gov.br/scg/gd/GD_Estadual.asp'
        self.sess = requests.Session()

    def access_page(self):
        print(self.sess.get(self.url).content)


if __name__ == '__main__':
    Scraper().access_page()
