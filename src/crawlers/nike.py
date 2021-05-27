# -*- coding: utf-8 -*-
from selenium import webdriver

import time

url = 'https://www.nike.com.br/'

driver = webdriver.Chrome('../../drivers/chromedriver.exe')

js = """fetch("https://www.nike.com.br/Cliente/LogarNike", {
    "credentials": "include",
    "headers": {
        "accept": "application/json, text/javascript, /; q=0.01",
        "accept-language": "en-US,en;q=0.9,pt;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    },
    "referrer": "https://www.nike.com.br/Pedido/Acompanhamento/todos",
    "referrerPolicy": "no-referrer-when-downgrade",
    "body": "user%5Bcontact%5D%5Bemail%5D%5Baddress%5D=pedronegri%40me.com&user%5Bdob%5D%5Bdate%5D=-2198707200000&user%5Bdob%5D%5Bday%5D=30&user%5Bdob%5D%5Bmonth%5D=4&user%5Bdob%5D%5Byear%5D=1900&user%5Bgender%5D=M&user%5Bmarketing%5D%5Bdatashare%5D%5B00001%5D%5Bid%5D=00001&user%5Bmarketing%5D%5Bdatashare%5D%5B00001%5D%5Bactive%5D=true&user%5Bmarketing%5D%5Bemail%5D=true&user%5Bmarketing%5D%5Bsms%5D=true&user%5Bname%5D%5Blatin%5D%5Bfamily%5D=Arenas&user%5Bname%5D%5Blatin%5D%5Bgiven%5D=Pedro&user%5BnuId%5D=10032C8967D32ED0E0534C1C070A6370&user%5BupmId%5D=12774933647&user%5BdaysSinceLastVisit%5D=0&address%5Bshipping%5D%5Bcode%5D=09090-000&address%5Bshipping%5D%5Bcountry%5D=BR&address%5Bshipping%5D%5Bguid%5D=6406ee0d-416f-41ad-94c1-4e9387b65e13&address%5Bshipping%5D%5Blabel%5D=Principal&address%5Bshipping%5D%5Bline1%5D=Rua+das+Aroeiras%2C+900&address%5Bshipping%5D%5Bline2%5D=161&address%5Bshipping%5D%5Blocality%5D=Santo+Andr%C3%A9&address%5Bshipping%5D%5Bpreferred%5D=true&address%5Bshipping%5D%5Bprovince%5D=SP&address%5Bshipping%5D%5Bregion%5D=Jardim&address%5Bshipping%5D%5Btype%5D=SHIPPING&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Bcode%5D=09090-000&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Bcountry%5D=BR&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Bguid%5D=7964b9c1-c53f-4361-b720-9fc16d47a192&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Blabel%5D=Rua+das+Aroeiras&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Bline1%5D=Rua+das+Aroeiras%2C+900&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Bline2%5D=Apt+161&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Blocality%5D=Santo+Andr%C3%A9&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Bpreferred%5D=false&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Bprovince%5D=SP&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Bregion%5D=Jardim&address%5B7964b9c1-c53f-4361-b720-9fc16d47a192%5D%5Btype%5D=SHIPPING",
    "method": "POST",
    "mode": "cors"
})"""

driver.get(url)

driver.execute_script(js)

products = (
    'https://www.nike.com.br/chuteira-nike-phantom-gt-elite-3d-unissex-153-169-171-316414?gridPosition=A1',
    'https://www.nike.com.br/tenis-nike-zoomx-vaporfly-next-2-feminino-1-16-214-311846?gridPosition=A2',
    'https://www.nike.com.br/tenis-nike-zoom-fly-3-feminino-1-16-214-305856?gridPosition=A3',
)
for product in products:
    driver.get(product)
    driver.implicitly_wait(1)
