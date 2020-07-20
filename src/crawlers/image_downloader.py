# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from tqdm import tqdm

import requests
import io
import os


class ImageDownloader:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.path = os.path.abspath('data/{}'.format(self.filename))
        self.checkpoint = 0

        self.check_directory()

    # used in __init__
    def check_directory(self):
        """This function checks if on the given path the directory exists. If
        exists add it into the self.checkpoint the index of the most recent
        file - For not overwriting images. Otherwise, create the directory.

        Returns
        -------

        """
        if os.path.exists(self.path):
            try:
                self.checkpoint += len(os.listdir(self.path))
            except TypeError:
                self.checkpoint = 0
            except IndexError:
                self.checkpoint = 0
        else:
            os.makedirs(self.path)

    # Used in __call__
    @staticmethod
    def soup(html):
        """This function parses the html.
        Parameters
        ----------
        html : requests.models.Response
            Unparsed html.
        Returns
        -------
        parsed_html : bs4.BeautifulSoup
            Parsed html.
        """
        return BeautifulSoup(html.content, 'html5lib')

    # Used in __call__
    @staticmethod
    def filtering(html):
        """This function double filters the html and returns the image list.

        Parameters
        ----------
        html : bs4.BeautifulSoup4

        Returns
        -------
        html_tag : bs4.element.ResultSet

        """
        return html.find_all('img', {
            'alt': html.find('img', {
                'sizes': '(max-width: 420px) 100vw,'
                         '(max-width: 899px) and (min-width: 421px) 33.3vw,'
                         '(max-width: 1300px) and (min-width: 900px) 25vw,'
                         '(min-width: 1301px) 20vw'}).attrs.get('alt')
        })

    # Used in __call__
    def filename_format(self, idx, extension):
        """This function formats the filepath by adding its abspath and
        extension.

        Parameters
        ----------
        idx : int
            The image index - For not overwriting.
        extension : str
            Image extension.

        Returns
        -------
        formatted_filepath : str
            The formatted filepath.

        """
        return self.path + '/' + self.filename + '-{}.{}'. \
            format(idx + self.checkpoint, extension)

    # Used in __call__
    def saving_image(self, image_list):
        """This function iterates through the image list.

        Parameters
        ----------
        image_list : iterator
            The images list.

        Returns
        -------

        """
        for idx, img in enumerate(image_list, 1):
            filename = self.filename_format(idx, 'jpg')
            with io.open(filename, 'wb') as file:
                file.write(requests.get(
                    img.attrs.get('srcset').split(' ')[0]).content)

    def __call__(self, *args, **kwargs):
        self.saving_image(self.filtering(self.soup(requests.get(self.url))))


def finding_url_list(url_):
    html = BeautifulSoup(requests.get(url_).content, 'html5lib')
    url_list_ = []
    for elem in html.find_all('ul', {'class': 'gallery-a b'}):
        for link in elem.find_all('a'):
            url_list_.append(link.attrs.get('href'))
    return url_list_[::-1]


if __name__ == '__main__':
    for url in tqdm(finding_url_list('https://www.elitebabes.com/model/cara-mell/')):
        ImageDownloader(url, 'cara-mell').__call__()
