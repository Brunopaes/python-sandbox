# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from tqdm import tqdm

import requests
import io
import os


class AnaDiasDownloader:
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
        return html.find_all('a', {'itemprop': 'contentUrl'})

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
        for idx, img in enumerate(tqdm(image_list), 1):
            filename = self.filename_format(idx, 'jpg')
            with io.open(filename, 'wb') as file:
                file.write(requests.get(
                    img.attrs.get('href')).content)

    def __call__(self, *args, **kwargs):
        self.saving_image(self.filtering(self.soup(requests.get(self.url))))


if __name__ == '__main__':
    AnaDiasDownloader(
        'http://www.anadiasphotography.com/proj/adel-vakula-last-house-on-mulholland/',
        'adel-vakula'
    ).__call__()
