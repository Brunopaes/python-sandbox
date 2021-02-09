# -*- coding: utf-8 -*-
from google.cloud import bigquery

import requests
import os


def set_path():
    """This function sets settings.json in PATH.

    Returns
    -------

    """
    path = os.path.abspath('gcp-credentials.json')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path


def start_connection():
    """Function used to start connection with GCP's Big Query.

    Returns
    -------

    """
    return bigquery.Client()


class BTCoin:
    def __init__(self):
        self.url = 'https://api.coinext.com.br:8443/AP/GetL2Snapshot'
        self.payload = '{"OMSId": 1, "InstrumentId": 1, "Depth": 1}'
        self.response = self.requesting()

        self.operation = {
            'operation': [],
            'price': [],
            'spread': [],
        }

        self.query = """
            INSERT INTO
                `mooncake-304003.DS_Bruno.btc-trader` 
            VALUES
                ("{}", {}, {}, CURRENT_DATETIME("America/Sao_Paulo"))
        """

        set_path()
        self.client = start_connection()

    # Used in __init__
    def requesting(self):
        """This function is used to request into api endpoint.

        Returns
        -------
        response : str
            The str api response.

        """
        return requests.post(self.url, data=self.payload).text

    # Used in __call__
    def parse_response(self):
        """This function parses the api response into a dictionary.

        Returns
        -------

        """
        self.operation.get('operation').append('buy')
        self.operation.get('price').append(
            float(self.response.split(',')[6])
        )
        self.operation.get('spread').append(
            float(self.response.split(',')[8])
        )

        self.operation.get('operation').append('sell')
        self.operation.get('price').append(
            float(self.response.split(',')[16])
        )
        self.operation.get('spread').append(
            float(self.response.split(',')[18])
        )

    # Used in __call__
    def inserting_in_bd(self):
        """This function inserts buy/sell data into BigQuery.

        Returns
        -------

        """
        for i in range(0, 2):
            self.client.query(self.query.format(
                self.operation.get('operation')[i],
                self.operation.get('price')[i],
                self.operation.get('spread')[i])
            )

    def __call__(self, *args, **kwargs):
        self.parse_response()
        self.inserting_in_bd()


if __name__ == '__main__':
    BTCoin().__call__()
