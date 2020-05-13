# -*- coding: utf-8 -*-
import pandas
import bs4


class Reader:
    def __init__(self, path):
        self.path = path
        self.html = self.open_html()
        self.dict = {
            'date': [],
            'pageviews': [],
            'uniques': [],
            'members-joined': []
        }
        self.table = None

    @staticmethod
    def soup(unparsed_html, parser='html5lib'):
        return bs4.BeautifulSoup(unparsed_html, parser)

    def open_html(self):
        return self.soup(open(self.path, 'r').read())

    def find_div(self):
        return self.html.find_all('div', {'class': '_23vJv7PbwZphG7Y4LE5wFA'})

    def find_span(self, div_list):
        for div in div_list:
            span = div.find_all('span')

            self.dict.get('date').append(span[0].text)
            self.dict.get('pageviews').append(span[1].text)
            self.dict.get('uniques').append(span[2].text)
            self.dict.get('members-joined').append(span[3].text)

    @staticmethod
    def formatting_row(row):
        return int(row.replace(',', ''))

    def pandas_parser(self):
        df = pandas.DataFrame(self.dict)

        df.date = pandas.to_datetime(df.date)
        df.pageviews = df.pageviews.apply(lambda row: self.formatting_row(row))
        df.uniques = df.uniques.apply(lambda row: self.formatting_row(row))
        df['members-joined'] = \
            df['members-joined'].apply(lambda row: self.formatting_row(row))

        self.table = df

    def __call__(self, *args, **kwargs):
        self.find_span(self.find_div())
        self.pandas_parser()
