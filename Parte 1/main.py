import requests as req
import numpy as np
import json, re
import math
from itertools import accumulate
from matplotlib import pyplot as plt
from pyproj import Transformer
from datetime import datetime
from distancias import *
from auxiliar import *
    
# Argumentos: Lista dos pontos do trajeto com seus dados
# Retorno: Distancias entre os pontos, tempo entre pontos, velocidades entre pontos, distância total, tempo total, velocidade média do trajeto
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
        distTrig.append(distancia_trigonometria(dados[i-1],dados[i]))
        dt.append((dados[i]["date"] - dados[i-1]["date"]).total_seconds())
        if dt[i-1] == 0:
            velHaversine.append(distHaversine[i-1])
            velMercator.append(distMercator[i-1])
            velTrig.append(distTrig[i-1])    
        else:
            velHaversine.append(distHaversine[i-1]/dt[i-1])
            velMercator.append(distMercator[i-1]/dt[i-1])
            velTrig.append(distTrig[i-1]/dt[i-1])
        i += 1
    distancias = (distHaversine, distMercator, distTrig)
    velocidades = (velHaversine, velMercator, velTrig)
    distTotal = [ distancia_haversine(dados[len(dados)-1],dados[0]), distancia_xy(dados[len(dados)-1],dados[0]), distancia_trigonometria(dados[len(dados)-1],dados[0]) ]
    tempTotal = (dados[len(dados)-1]["date"] - dados[0]["date"]).total_seconds()
    velMed = [dist/tempTotal for dist in distTotal]

    return distancias , dt, velocidades, distTotal, tempTotal, velMed
    
# Argumentos: Lista com as velocidades e as diferencas de tempo entre os pontos
# Plota os graficos de velocidade x tempo das diferentes formulas
def plotar_dados(parametro: list, dt: list):
    plt.plot(parametro[0], dt)
    plt.plot(parametro[1], dt)
    plt.plot(parametro[2], dt)
    plt.xlabel("Tempo (s)")
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
    parametros = ["lat", "lng", "sequenceIndex", "fileurlLTh", "shotDate"] # formato de data: ano-mes-dia hora:min:seg // datetime.strptime(time,"%Y-%m-%d %H:%M:%S")
    dados_tratados_brasil = tratar_dados(dados_brutos_brasil, parametros)
    dados_tratados_fora = tratar_dados(dados_brutos_fora, parametros)

    # baixa as fotos do trajeto
    # for dado in dados_tratados_fora:
    #     salvar_imagem(dado["sequenceIndex"], dado["fileurlLTh"])

    # transforma coordenadas
    transformar_coordenadas(dados_tratados_brasil)
    transformar_coordenadas(dados_tratados_fora)
    for i in range(10):
        print(dados_tratados_brasil[i]["date"])

    # Dados subtrecho
    distancias_br, dt_br, velocidades_br, dist_total_br, tempo_total_br, vel_med_br = subtrecho_info(dados_tratados_brasil)
    distancias_fora, dt_fora, velocidades_fora, dist_total_fora, tempo_total_fora, vel_med_fora = subtrecho_info(dados_tratados_fora)
    
    cum_dist_br = (list(accumulate(distancias_br[0])),list(accumulate(distancias_br[1])),list(accumulate(distancias_br[2])))
    cum_dt_br = (list(accumulate(dt_br)))
    cum_dist_fora = (list(accumulate(distancias_fora[0])),list(accumulate(distancias_fora[1])),list(accumulate(distancias_fora[2])))
    cum_dt_fora = (list(accumulate(dt_fora)))


    # Plota graico
    plotar_dados(cum_dist_br, cum_dt_br)
    plotar_dados(cum_dist_fora, cum_dt_fora)

if __name__ == "__main__":
 	main()