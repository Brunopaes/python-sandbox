#!-*- coding: utf8 -*-
from bs4 import BeautifulSoup

import requests

url = 'https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo/?onde=,S%C3%' \
      'A3o%20Paulo,S%C3%A3o%20Paulo,,,,,city,BR%3ESao%20Paulo%3ENULL%3ESao%' \
      '20Paulo,-23.5505199,-46.63330939999999&tipo=Im%C3%B3vel%' \
      '20usado&transacao=Venda'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.61 Safari/537.36'
}

html = BeautifulSoup(requests.get(url, headers=headers).content, 'html5lib')

print(html)
