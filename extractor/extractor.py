from pprint import pprint

import requests
from model import model


def getJsonInfoFromUrl(url: str, header: dict, bodyA: dict = {}) -> any:
    data = requests.post(url=url, headers=header, json=bodyA)
    return data.json()


api_url = "http://veiculos.fipe.org.br/api/veiculos/ConsultarTabelaDeReferencia"

api_headers = {
    "Host": "veiculos.fipe.org.br",
    "Referer": "http://veiculos.fipe.org.br",
    "Content-Type": "application/json"
}

fipeInformation = getJsonInfoFromUrl(api_url, api_headers)

tableReferenceCode = fipeInformation[0]["Codigo"]

carInformation = model.list_cars()

for car in carInformation:
    body = {
        "codigoTabelaReferencia": tableReferenceCode,
        "codigoTipoVeiculo": 1,
        "anoModelo": 2012,
        "modeloCodigoExterno": car.externalCode,
        "codigoTipoCombustivel": 1,
        "tipoConsulta": "codigo"
    }
    urlNova = "http://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros"
    fipeCarInfo = getJsonInfoFromUrl(urlNova, api_headers, body)
    model.insert_car_price(car, price=fipeCarInfo['Valor'])
