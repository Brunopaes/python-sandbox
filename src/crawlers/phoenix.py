#!-*- coding: utf8 -*-
from bs4 import BeautifulSoup
from tqdm import tqdm

import requests
import datetime
import pandas


class PhoenixScrapper:
    def __init__(self, file_path):
        self.df = pandas.ExcelFile(file_path)

        self.youtube = pandas.read_excel(self.df, 'YouTube').set_index('Nick')
        self.stream = pandas.read_excel(self.df, 'Stream')
        self.press = pandas.read_excel(self.df, 'Imprensa')
        self.instagram = pandas.read_excel(self.df, 'Instagram')
        self.segmentation = pandas.read_excel(self.df, 'Segmentação')
        self.strategy = pandas.read_excel(self.df, 'Strategy')

        self.url_list = self.cleaning_dataframe()

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
        self.multiplier_factor = {
            'K': 1000,
            'M': 1000000
        }
        self.followers = []
        self.viewers = []

    def cleaning_dataframe(self):
        url_list = self.selecting_url_list()
        self.youtube = self.youtube[self.youtube['Social Blade'].isin(url_list)]

        return url_list

    def selecting_url_list(self):
        return self.youtube['Social Blade'].dropna().to_list()

    @staticmethod
    def parse_html(response):
        return BeautifulSoup(response.content, 'html5lib')

    def filtering_page_elements(self, html):
        subscribers = html.find('span', {
            'id': 'youtube-stats-header-subs'
        }).text

        viewers = \
            html.find_all('div', {
                'style': 'width: 860px; '
                         'height: 50px; '
                         'background: #fff; '
                         'padding: 0px 20px; '
                         'color:#444; '
                         'font-size: 9pt; '
                         'border-bottom: 1px solid #eee;'
            })[-2].find_all('div')[-2].text

        self.followers.append(
            int(self.multiplier_factor.get(subscribers[-1]) *
                float(subscribers[:-1])))
        self.viewers.append(int(viewers.strip().replace(',', '')))

    def writing(self):
        writer = pandas.ExcelWriter('xbox-{}.xlsx'.format(datetime.date.today()))

        self.youtube.to_excel(writer, 'Youtube')
        self.stream.to_excel(writer, 'Stream')
        self.press.to_excel(writer, 'Imprensa')
        self.instagram.to_excel(writer, 'Instagram')
        self.segmentation.to_excel(writer, 'Segmentação')
        self.strategy.to_excel(writer, 'Strategy')

        writer.save()

    def __call__(self, *args, **kwargs):
        for url in tqdm(self.url_list):
            self.filtering_page_elements(self.parse_html(
                requests.get(url, headers=self.headers)))

        self.youtube['Seguidores'] = self.followers
        self.youtube['Viewers semanal'] = self.viewers

        self.writing()


if __name__ == '__main__':
    PhoenixScrapper(r'.\..\..\data\files\sample.xlsx').__call__()
