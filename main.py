import requests as req
import json, re

def filtrar_link(link):
    filtro = r"https://kartaview.org/details/([0-9]*)/[0-9]*/track-info"
    link_filtrado = re.search(filtro, link)[1]
    return link_filtrado

def coletar_dados(id):
    site_api = f"https://api.openstreetcam.org/2.0/sequence/{id}/photos"
    payload = req.get(site_api)
    dados = payload.json()['result']['data']
    return dados

def tratar_dados(dados, parametros):
    pass

def main():
    
    # prepara o link para extração dos dados
    link = "https://kartaview.org/details/28199/0/track-info"
    link_filtrado = filtrar_link(link)

    # coleta dados brutos
    dados_brutos = coletar_dados(link_filtrado)
    print(dados_brutos[0])

    # tratamento dos dados brutos
    parametros = ["distance", "from", "heading", "height", "lat", "lng", "matchLat", "matchLng", "to", "width"]
    dados_tratados = tratar_dados(dados_brutos, parametros)

if __name__ == "__main__":
 	main()