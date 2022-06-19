from matplotlib import pyplot as plt
import requests as req
import numpy as np
import json, re
from pyproj import Transformer
import math
from datetime import datetime

# Argumento: link do trajeto desejado
# Retorno: link adaptado para a chamada da API
def filtrar_link(link: str):
    filtro = r"https://kartaview.org/details/([0-9]*)/[0-9]*/track-info"
    link_filtrado = re.search(filtro, link)[1]
    return link_filtrado

# Argumento: 
# Retorno:
def coletar_intervalo(id: int, intervalo: tuple):
    seq = [str(i) for i in range(intervalo[0],intervalo[1]+1)]
    site_api = f"https://api.openstreetcam.org/2.0/sequence/{id}/photos?sequenceIndex={','.join(seq)}"
    payload = req.get(site_api)
    dados = payload.json()['result']['data']
    return dados

# Argumento: Recebe o link filtrado e o intervalo de fotos a ser utilizado
# Retorno: dados brutos adquiridos através da API
def coletar_dados(id: int, intervalo: tuple):
    salto = 90
    dados_completos = []

    for i in range(intervalo[0],intervalo[1],salto):
        fim = i+salto-1
        if fim > intervalo[1]: inter_gerado = (i,intervalo[1])
        else: inter_gerado = (i,fim)
        dados_completos += coletar_intervalo(id, inter_gerado)
    
    return dados_completos

# Argumento: nome para a imagem e link da imagem
# Retorno: Sem retorno, salva a imagem
def salvar_imagem(nome:str, link:str):
    imagem = req.get(link)
    with open(f"Fotos/Inglaterra/{nome}.png", "wb") as f:
        f.write(imagem.content)
    

# Argumento: dados brutos, intervalo desejado do trajeto, parametros considerados importantes no trajeto 
# Retorno: dados tratados apenas com as informações importantes
def tratar_dados(dados: list, params: list):
    dados_trajeto = [] # lista de dicionarios para cada frame do trajeto
    for dado in dados:
        amostra = {}
        for param in params:
            if param == "shotDate":
                amostra["date"] = tratar_tempo(dado[param])
                continue
            if param in ["lat", "lng"]:
                amostra[param] = float(dado[param])
                continue
            if param == "sequenceIndex":
                amostra[param] = int(dado[param])
                continue
            amostra[param] = dado[param]
        dados_trajeto.append(amostra)
    return dados_trajeto

# Argumento: coordenadas no formato longitude e latitude
# Retorno: coordenadas no formato planar
def transformar_coordenadas(dados: list):
  for dicionario in dados:
    transformer = Transformer.from_crs("epsg:4326", "epsg:3857")
    p = transformer.transform(dicionario['lng'], dicionario['lat'])
    dicionario["y"] = p[0]
    dicionario["x"] = p[1]

def tratar_tempo(data: str):
    return datetime.strptime(data,"%Y-%m-%d %H:%M:%S")