import requests

url = "https://dseriesapi.dcide.com.br/api/Auth/Login"

url_series = "https://dseriesapi.dcide.com.br/api/series/registros/"

series = [
    "indice_curve_forward_trimestre_convencional"
]

sess = requests.Session(

)

response = sess.post(url, json={
    "userName": "",
    "password": ""
}).json()

params = {
    "serie": series[0],
    "dataInicio": "2023-06-20",
    "dataFim": "2023-06-30"
}

headers = {
    "Authorization-key": response["sessionKey"],
    "userName": response["User"]["userName"]
}

sess.get(url_series, headers=headers, params=params)