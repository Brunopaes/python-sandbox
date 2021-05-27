# -*- coding: utf-8 -*-
from requests_html import HTMLSession
from bs4 import BeautifulSoup

import requests

url = 'https://unite.nike.com.br/oauth.html?client_id=QLegGiUU042XMAUWE4qWL3fPUIrpQTnq&redirect_uri=https%3A%2F%2Fwww.nike.com.br%2Fapi%2Fv2%2Fauth%2Fnike-unite%2Fset&response_type=code&locale=pt_BR&state=%2F'

# credentials = {
#     "user[contact][email][address]": "pedronegri@me.com",
#     "user[dob][date]": -2198707200000,
#     "user[dob][day]": 30,
#     "user[dob][month]": 4,
#     "user[dob][year]": 1900,
#     "user[gender]": "M",
#     "user[marketing][datashare][00001][id]": "00001",
#     "user[marketing][datashare][00001][active]": "true",
#     "user[marketing][email]": "true",
#     "user[marketing][sms]": "true",
#     "user[name][latin][family]": "Arenas",
#     "user[name][latin][given]": "Pedro",
#     "user[nuId]": "10032C8967D32ED0E0534C1C070A6370",
#     "user[upmId]": 12774933647,
#     "user[daysSinceLastVisit]": 0,
#     "address[shipping][code]": "09090-000",
#     "address[shipping][country]": "BR",
#     "address[shipping][guid]": "6406ee0d-416f-41ad-94c1-4e9387b65e13",
#     "address[shipping][label]": "Principal",
#     "address[shipping][line1]": "Rua das Aroeiras, 900",
#     "address[shipping][line2]": 161,
#     "address[shipping][locality]": "Santo André",
#     "address[shipping][preferred]": "true",
#     "address[shipping][province]": "SP",
#     "address[shipping][region]": "Jardim",
#     "address[shipping][type]": "SHIPPING",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][code]": "09090-000",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][country]": "BR",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][guid]": "7964b9c1-c53f-4361-b720-9fc16d47a192",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][label]": "Rua das Aroeiras",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][line1]": "Rua das Aroeiras, 900",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][line2]": "Apt 161",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][locality]": "Santo André",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][preferred]": "false",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][province]": "SP",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][region]": "Jardim",
#     "address[7964b9c1-c53f-4361-b720-9fc16d47a192][type]": "SHIPPING"
# }

credentials = {
    "username": "pedronegri@me.com",
    "password": "Pedro300405",
    "client_id": "QLegGiUU042XMAUWE4qWL3fPUIrpQTnq",
    "ux_id": "com.nike.commerce.nikedotcom.brazil.oauth.web",
    "grant_type": "password"
}

s = HTMLSession()
s.post(url, data=credentials)
s.get('https://www.nike.com.br/Checkout')

