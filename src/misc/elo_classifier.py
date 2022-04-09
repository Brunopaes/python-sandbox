# -*- coding: utf-8 -*-
from tkinter.filedialog import askopenfilename
from itertools import permutations
from tkinter import Tk

import datetime
import pandas
import random
import math
import csv
import os


class TopSomething:
    def __init__(self):
        self.file = self.choose_file()
        self.dict = {}
        self.keys = []
        self.matches = []

        self.file_name = 'elo-rating_{}.csv'.format(datetime.date.today())

        self.k = 30

    @staticmethod
    def choose_file(path='./', file_type=(('All files', '*.*'), )):
        root = Tk()
        root.withdraw()
        filename = askopenfilename(initialdir=path,
                                   title='Select file',
                                   filetypes=file_type)
        root.destroy()

        return filename

    def open_file(self):
        with open(self.file, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                self.dict.update({row[0]: [1000.0]})

    def generating_matches(self):
        self.matches = list(permutations(self.keys, 2))
        for i in range(random.randint(10, 100)):
            random.shuffle(self.matches)

    def running_matches(self):
        for match in self.matches:
            self.winner(match)

    def winner(self, competitors):
        phrase = 'Which one is your favorite?\n'\
                 '   1 - {}\n'\
                 '   2 - {}\n\n'.format(competitors[0], competitors[1])

        while True:
            try:
                qst = int(input(phrase))
            except ValueError:
                print('Non Valid Option')
                continue

            if qst in [1, 2]:
                break
            print('Non Valid Option!')

        self.calculating_elo(int(qst), competitors)

    @staticmethod
    def calculating_win_probability(rating_1, rating_2):
        return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating_1 - rating_2)))

    def updating_elo(self, ra, rb, winner_name, loser_name):
        self.dict[winner_name] = [ra]
        self.dict[loser_name] = [rb]

    def calculating_elo(self, d, competitors):
        if d == 1:
            winner_name = competitors[0]
            loser_name = competitors[1]
        else:
            winner_name = competitors[1]
            loser_name = competitors[0]

        ra = self.dict.get(winner_name)[0]
        rb = self.dict.get(loser_name)[0]

        pa = self.calculating_win_probability(ra, rb)
        pb = self.calculating_win_probability(rb, ra)

        if d == 1:
            ra = ra + self.k * (1 - pa)
            rb = rb + self.k * (0 - pb)
        else:
            ra = ra + self.k * (1 - pa)
            rb = rb + self.k * (0 - pb)

        self.updating_elo(ra, rb, winner_name, loser_name)

    def formatting_output(self):
        df = pandas.DataFrame(self.dict).T.sort_values(0, ascending=False)
        df.columns = ['ELO Rating']

        df.to_csv(self.file_name)
        os.startfile(self.file_name)

    def __call__(self, *args, **kwargs):
        self.open_file()
        self.keys = list(self.dict.keys())
        self.generating_matches()
        self.running_matches()

        self.formatting_output()


if __name__ == '__main__':
    TopSomething().__call__()
