from bs4 import BeautifulSoup
from tqdm import tqdm

import datetime
import requests
import pandas


URL_LIST = [
    "https://sisdipre.ream.com.br/lancamentos/?produto=1&data__year={}&data__month={}",
    "https://sisdipre.ream.com.br/lancamentos/?produto=2&data__year={}&data__month={}",
    "https://sisdipre.ream.com.br/lancamentos/?produto=3&data__year={}&data__month={}",
    "https://sisdipre.ream.com.br/lancamentos/?produto=4&data__year={}&data__month={}",
    "https://sisdipre.ream.com.br/lancamentos/?produto=5&data__year={}&data__month={}",
    "https://sisdipre.ream.com.br/lancamentos/?produto=6&data__year={}&data__month={}",
    "https://sisdipre.ream.com.br/lancamentos/?produto=8&data__year={}&data__month={}",
    "https://sisdipre.ream.com.br/lancamentos/?produto=9&data__year={}&data__month={}",
    "https://sisdipre.ream.com.br/lancamentos/?produto=11&data__year={}&data__month={}"
]

if __name__ == '__main__':
    ffill = pandas.DataFrame()
    for url in tqdm(URL_LIST):
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html5lib")

        product = soup.find("div", {"class": "row mt-4"}).find("b").text

        table = pandas.read_html(str(soup.find("table")))[-1]

        try:
            table["Preço"] = table["Preço"].apply(lambda row: float(
                row.split("R$")[-1].strip().replace(",", ".")))
        except ValueError:
            table["Preço"] = table["Preço"].apply(lambda row: float(
                row.split("R$")[-1].strip().replace(",", "")))

        table["Data"] = \
            pandas.to_datetime(table["Data"], format="%d/%m/%Y")

        table["Produto"] = product

        for mode in table["Modalidade de Venda"].unique():
            for local in table["Local"].unique():
                temp = table[
                    (table["Modalidade de Venda"] == mode) &
                    (table["Local"] == local)
                ]
                if temp.empty:
                    continue

                all_dates = pandas.date_range(
                    min(temp.Data),
                    datetime.date.today()
                )

                temp = temp.set_index("Data").reindex(
                    all_dates, method="ffill"
                ).reset_index().rename(columns={'index': 'Data'})

                ffill = pandas.concat([ffill, temp])

    ffill.to_csv(
        "REAM.csv",
        index=None
    )