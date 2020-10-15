# -*- coding: utf-8 -*-
from imgurpython import ImgurClient
from helpers import read_json

import logging
import random
import praw
import os


class Poster:
    def __init__(self, path, subreddit, name=None, playboy_on_reddit=False):
        self.credentials = read_json('settings.json')
        self.logging_('%(levelname)s: %(asctime)s - %(message)s')
        self.path = path

        self.name = name
        self.subreddit = subreddit

        if playboy_on_reddit:
            self.subreddit = 'PlayboyOnReddit'
            self.credentials.get('reddit')['username'] = 'PlayboyOnReddit'
            self.credentials.get('reddit')['client_id'] = 'H5SoyNl14zTjVQ'
            self.credentials.get('reddit')['client_secret'] = \
                '0RJmTHumxR6AyM0FdFjLwi9Jzpo'

        self.reddit = self.reddit_authenticate()
        self.imgur = self.imgur_authenticate()

        self.reddit.validate_on_submit = True

    # used in __init__
    @staticmethod
    def logging_(logging_format):
        """This functions initializes the logging function.

        Parameters
        ----------
        logging_format : str
            log format - type: time - message

        Returns
        -------

        """
        logging.basicConfig(filename='data/run_log.log',
                            level=logging.INFO, format=logging_format)

    # used in __init__
    def reddit_authenticate(self):
        """This function logs in some reddit´s account.

        Returns
        -------

        """
        logging.info('Authenticating in Reddit')
        return praw.Reddit(**self.credentials.get('reddit'))

    # used in __init__
    def imgur_authenticate(self):
        """This function authenticates into imgur api.

        Returns
        -------
        ImgurClient : imgurpython.client.ImgurClient
            The imgur connection instance.

        """
        logging.info('Authenticating in Imgur')
        return ImgurClient(**self.credentials.get('imgur'))

    # used in __init__
    def choose_file(self):
        """This function given a specific path random selects a to be posted
        image file.

        Returns
        -------
        playmate_dir : str
            Random chosen directory.
        filename : str
            Image filename.
        post_title : str
            Post Title (Obtained from image filename).

        """
        playmate_dir = random.choice(os.listdir(os.path.abspath(self.path)))
        filename = \
            random.choice(os.listdir(r'{}\{}'.format(self.path, playmate_dir)))
        post_title = \
            ' '.join([i.capitalize() for i in filename.split('-')[:-1]])

        logging.info('Choosing file: {}, {}'.format(playmate_dir, filename))

        return playmate_dir, filename, post_title

    # used in __init__
    def upload_to_imgur(self, path):
        """This function uploads a image to Imgur.

        Parameters
        ----------
        path : str
            Image path.

        Returns
        -------
        imgur_dict: dict
            The upload responses.

        """
        return self.imgur.upload_from_path(path)

    # used in __init__
    def upload_to_reddit(self, imgur_dict, post_title):
        """This function uploads an imgur link to Reddit.

        Parameters
        ----------
        imgur_dict : dict
            The upload responses.
        post_title : str
            Post Title.
        Returns
        -------

        """
        if 'And' in post_title:
            post_title = post_title.replace('And', 'and')

        self.reddit.subreddit(self.subreddit).submit(
            title='{} | NSFW'.format(post_title), url=imgur_dict.get('link')
        )
        print("{}'s photo was uploaded with {} to reddit".format(
            post_title,
            imgur_dict.get('link')
        ))
        logging.info('Uploaded {} to reddit'.format(imgur_dict.get('link')))

    def __call__(self, *args, **kwargs):
        if self.name is None:
            self.playmate_dir, self.filename, self.post_title = \
                self.choose_file()

            self.final_path = r'{}\{}\{}'.format(
                self.path, self.playmate_dir, self.filename
            )

            self.upload_to_reddit(self.upload_to_imgur(
                self.final_path), self.post_title
            )
        else:
            self.upload_to_reddit(self.upload_to_imgur(self.path), self.name)


if __name__ == '__main__':
    for i in range(2):
        Poster(
            r'C:\Users\bruno\iCloudDrive\Documents\Playboy\Playboy Photos',
            'Playboy',
        ).__call__()
