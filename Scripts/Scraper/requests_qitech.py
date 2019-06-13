import multiprocessing
from tqdm import tqdm

import datetime
import requests
import random


class Requester:
    def __init__(self, name):
        self.url = 'http://postal-code.sandbox.certifier.qitech.app/' \
                   'postal_code/{}'
        self.sess = requests.Session()
        self.name = name

    def generating_cep(self):
        cep = '{0:08d}'.format(random.randint(00000000, 99999999))
        open('Data/cep_log.txt', 'a').write('{}   {}   {}\n'.format(self.name, datetime.datetime.today(), cep))

        return cep

    def formatting_url(self, cep):
        return self.url.format(cep)

    def access_page(self):
        self.sess.get(self.formatting_url(self.generating_cep()))

    def __call__(self, *args, **kwargs):
        while True:
            for i in tqdm(range(1000), total=1000, desc='{}'.format(self.name)):
                self.access_page()


if __name__ == '__main__':
    processes = []
    for process in range(20):
        processes.append(multiprocessing.Process(target=Requester('T{}'.format(process))))

    for process in processes:
        process.start()

    for process in processes:
        process.join()
