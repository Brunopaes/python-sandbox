import time
import os


class Crontab():

    def __init__(self):
        self.myFile = open('/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/misc/05.4 - Pandas/data/crontab.txt', 'a')

    @staticmethod
    def remove():
        os.remove('/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/misc/05.4 - Pandas/data/crontab.txt')

    def setCrons(self):
        # setting in the crontab - Chow scripts
        self.myFile.write('58 7 {0} {1} {2} /usr/bin/python script.py\n'.format(time.strftime("%d"), time.strftime("%m"), time.strftime("%w")))
        # setting my script to update the crontab
        self.myFile.write('58 7 {0} {1} {2} /usr/bin/python contrab.py\n'.format(time.strftime("%d"), time.strftime("%m"), time.strftime("%w")))


if __name__ == '__main__':
    c = Crontab()
    c.setCrons()
