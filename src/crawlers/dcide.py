import requests
import pandas


def requests_auth(auth_url, **kwargs):
    return requests.post(auth_url, **kwargs)


def requests_series(series_url, **kwargs):
    return requests.get(series_url, **kwargs)


if __name__ == '__main__':
    settings = {
        "auth_url": "https://dseriesapi.dcide.com.br/api/Auth/Login",
        "auth_credentials": {
            "json": {
                "userName": None,
                "password": None
            }
        },
        "series_url": "https://dseriesapi.dcide.com.br/api/series/registros",
        "series": [
            "indice_curva_forward_trimestre_convencional",
            "indice_curva_forward_trimestre_incentivada50",
            "indice_curva_forward_4anos_convencional",
            "indice_curva_forward_4anos_incentivada50"
        ],
        "series_credentials": {
            "headers": {
                "Authorization-Key": None,
                "userName": None
            },
            "params": {
                "serie": None,
                "dataInicio": "2023-02-13",
                "dataFim": "2023-07-06"
            }
        }
    }

    tickers = {
        "indice_curva_forward_trimestre_convencional": "PWBDSCST Index",
        "indice_curva_forward_trimestre_incentivada50": "PWBDSIST Index",
        "indice_curva_forward_4anos_convencional": "PWBDSCLT Index",
        "indice_curva_forward_4anos_incentivada50": "PWBDSILT Index"
    }

    credentials = requests_auth(
        settings.get("auth_url"),
        **settings.get("auth_credentials")
    ).json()

    settings.get("series_credentials").get("headers").update({
        "Authorization-Key": credentials.get("sessionKey"),
        "userName": credentials.get("User").get("userName")
    })

    df_list = []
    for series in settings.get("series"):
        settings["series_credentials"]["params"]["serie"] = series
        data_series = requests_series(
            settings.get("series_url"),
            **settings.get("series_credentials")
        ).json()

        df_serie = pandas.DataFrame(data_series)
        df_serie["serie_id"] = series
        df_serie.set_index("serie_id", inplace=True)
        df_list.append(df_serie)

    df_merged = pandas.concat(df_list)
    df_merged["tickers"] = df_merged.index.map(tickers)
    df_merged.to_csv("NRNZap.csv")
