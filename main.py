from matplotlib import pyplot as plt
import requests as req
import numpy as np
import json, re
from pyproj import Transformer
import math
from datetime import datetime
from distancias import *
from auxiliar import *
    
#toDo
def subtrecho_info(dados: list):
    i = 1
    distMercator = []   
    distHaversine = []
    distTrig = []
    dt = []
    velMercator = []
    velHaversine = []
    velTrig = []
    while(i<len(dados)):
        distMercator.append(distancia_xy(dados[i-1],dados[i]))
        distHaversine.append(distancia_haversine(dados[i-1],dados[i]))
        distTrig.append(distancia_haversine(dados[i-1],dados[i]))
        dt.append((dados[i]["date"] - dados[i-1]["date"]).total_seconds())
        velHaversine.append()
        velMercator.append()
        velTrig.append
    distTotal = [ distancia_haversine(dados[len(dados)-1],dados[0]), distancia_xy(dados[len(dados)-1],dados[0]), distancia_trigonometria(dados[len(dados)-1],dados[0]) ]
    tempTotal = (dados[len(dados)-1]["date"] - dados[0]["date"]).total_seconds()
    velMe
    
    return  distHaversine, distMercator, distTrig, dt, distTotal, tempTotal

# toDo
def plotar_dados(velocidade_mercator: list, velocidade_haversine: list, velocidade_trigonometrica: list):
    plt.plot(velocidade_mercator)
    plt.plot(velocidade_haversine)
    plt.plot(velocidade_trigonometrica)
    plt.xlabel("Trajeto")
    plt.ylabel("Velocidade")
    plt.show()

def main():  
    # prepara o link para extração dos dados
    link_brasil = "https://kartaview.org/details/3604093/1263/track-info"
    link_fora = "https://kartaview.org/details/444319/1953/track-info"

    # define intervalos
    # aproximadamente 7km
    intervalo_brasil = (1263,1705)
    # aproximadamente 4.5km
    intervalo_fora = (1953,2070)

    # trata link fornecido
    link_filtrado_brasil = filtrar_link(link_brasil)
    link_filtrado_fora = filtrar_link(link_fora)

    # coleta dados brutos
    dados_brutos_brasil = coletar_dados(link_filtrado_brasil, intervalo_brasil)
    dados_brutos_fora = coletar_dados(link_filtrado_fora, intervalo_fora)
    print(f"length_brasil: {len(dados_brutos_brasil)}")
    print(f"length_fora: {len(dados_brutos_fora)}")

    # tratamento dos dados brutos
    parametros = ["lat", "lng", "sequenceIndex", "fileurlLTh", "dateAdded"] # formato de data: ano-mes-dia hora:min:seg // datetime.strptime(time,"%Y-%m-%d %H:%M:%S")
    dados_tratados_brasil = tratar_dados(dados_brutos_brasil, parametros)
    dados_tratados_fora = tratar_dados(dados_brutos_fora, parametros)

    # baixa as fotos do trajeto
    # for dado in dados_tratados_fora:
    #     salvar_imagem(dado["sequenceIndex"], dado["fileurlLTh"])

    # transforma coordenadas
    transformar_coordenadas(dados_tratados_brasil)
    transformar_coordenadas(dados_tratados_fora)

    # Calcula distancias
    dHaversineBr, dMercatorBr, dTrigonometricaBr, dtBr = subtrecho_info(dados_tratados_brasil)
    dHaversine, dMercator, dTrigonometrica, dt = subtrecho_info(dados_tratados_fora)

    #Calcula velocidades
    velocidade_mercator_br = calcula_velocidade(dMercatorBr, dtBr)
    velocidade_haversine_br = calcula_velocidade(dHaversineBr, dtBr)
    velocidade_trigonometrica_br = calcula_velocidade(dTrigonometricaBr, dtBr)
    velocidade_mercator = calcula_velocidade(dMercator, dt)
    velocidade_haversine = calcula_velocidade(dHaversine, dt)
    velocidade_trigonometrica = calcula_velocidade(dTrigonometrica, dt)
    
    # Plota graico
    plotar_dados(velocidade_mercator_br, velocidade_haversine_br, velocidade_trigonometrica_br)
    plotar_dados(velocidade_mercator, velocidade_haversine, velocidade_trigonometrica)

if __name__ == "__main__":
 	main()