from matplotlib import pyplot as plt
import requests as req
import numpy as np
import json, re
from pyproj import Transformer
import math

# toDo
# Argumento: link do trajeto desejado
# Retorno: link adaptado para a chamada da API
def filtrar_link(link: str):
    filtro = r"https://kartaview.org/details/([0-9]*)/[0-9]*/track-info"
    link_filtrado = re.search(filtro, link)[1]
    return link_filtrado


def coletar_intervalo(id: int, intervalo: tuple):
    seq = [str(i) for i in range(intervalo[0],intervalo[1]+1)]
    site_api = f"https://api.openstreetcam.org/2.0/sequence/{id}/photos?sequenceIndex={','.join(seq)}"
    payload = req.get(site_api)
    dados = payload.json()['result']['data']
    return dados
    
# toDo
# Argumento: 
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

def salvar_imagem(nome:str, link:str):
    imagem = req.get(link)
    with open(f"Fotos/{nome}.png", "wb") as f:
        f.write(imagem.content)
    

# Argumento: dados brutos, intervalo desejado do trajeto, parametros considerados importantes no trajeto 
# Retorno: dados tratados apenas com as informações importantes
def tratar_dados(dados: list, params: list):
    dados_trajeto = [] # lista de dicionarios para cada frame do trajeto
    for dado in dados:
        amostra = {}
        for param in params:
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

# Argumentos: Dois pontos do trajeto
# Retorno: Distância em km entre esses dois pontos usando a fórmula de haversine
def distancia_haversine(p1: dict, p2: dict):
    lat1 = math.radians(p1["lat"])
    lat2 = math.radians(p2["lat"])
    lng1 = math.radian(p1["lng"])
    lng2 = math.radians(p2["lng"])
    raio = 6371 #km
    hav = math.sin(lat2 - lat1)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lng2 - lng1) / 2)**2
    return 2 * raio * math.asin(math.sqrt(hav))

# Argumentos: Dois pontos do trajeto
# Retorno: Distância em km entre esses dois pontos usando trigonometria esférica
def distancia_trigonometria(p1: dict, p2: dict):
    lat1 = math.radians(p1["lat"])
    lat2 = math.radians(p2["lat"])
    lng1 = math.radian(p1["lng"])
    lng2 = math.radians(p2["lng"])
    raio = 6371 #km
    C = math.sin(lat1) * math.sin(lat2) + math.cos(lng2 - lng1) * math.cos(lat1) * math.cos(lat2)
    return (raio * math.pi * math.acos(C)) / 180

# Argumentos: Dois pontos do trajeto
# Retorno: Distância em km entre esses dois pontos usando distancia euclidiana
def distancia_xy(p1: dict, p2: dict):
    return math.sqrt((p1["y"]-p1["x"])**2+p2["y"]-p2["x"]**2)
    
#toDo
def subtrecho_info(dados: list, p1: dict, p2: dict):
    i = 1
    distMercador = []   
    distHaversine = []
    distTrig = []
    dt = []
    while (i<len(dados)):
        distMercador.append(distancia_xy(dados[i-1],dados[i]))
        distHaversine.append(distancia_haversine(dados[i-1],dados[i]))
        distTrig.append(distancia_haversine(dados[i-1],dados[i]))
        
    
# toDo
def plotar_dados(dados: list, parametro: list):
    pontos = [dado[parametro] for dado in dados]
    plt.plot(pontos)
    plt.show()

def main():  
    # prepara o link para extração dos dados
    link = "https://kartaview.org/details/3604093/1263/track-info"
    intervalo = (1263,1705)
    link_filtrado = filtrar_link(link)

    # coleta dados brutos
    dados_brutos = coletar_dados(link_filtrado, intervalo)
    print(f"length: {len(dados_brutos)}")

    # tratamento dos dados brutos
    parametros = ["lat", "lng", "sequenceIndex", "fileurlLTh"]
    dados_tratados = tratar_dados(dados_brutos, parametros)

    # baixa as fotos do trajeto
    # for dado in dados_tratados:
    #     salvar_imagem(dado["sequenceIndex"],dado["fileurlLTh"])
        
    # transforma coordenadas
    transformar_coordenadas(dados_tratados)
    print(dados_tratados[0])
    print(dados_tratados[-1])

if __name__ == "__main__":
 	main()