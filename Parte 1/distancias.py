import math

# Argumentos: Dois pontos do trajeto
# Retorno: Distância em km entre esses dois pontos usando a fórmula de haversine
def distancia_haversine(p1: dict, p2: dict):
    lat1 = math.radians(p1["lat"])
    lat2 = math.radians(p2["lat"])
    lng1 = math.radians(p1["lng"])
    lng2 = math.radians(p2["lng"])
    raio = 6371000 #km
    hav = math.sin((lat2 - lat1)/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lng2 - lng1) / 2)**2
    return 2 * raio * math.asin(math.sqrt(hav))

# Argumentos: Dois pontos do trajeto
# Retorno: Distância em km entre esses dois pontos usando trigonometria esférica
def distancia_trigonometria(p1: dict, p2: dict):
    lat1 = math.radians(p1["lat"])
    lat2 = math.radians(p2["lat"])
    lng1 = math.radians(p1["lng"])
    lng2 = math.radians(p2["lng"])
    raio = 6371000 #km
    return math.acos( math.sin(lat1)*math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lng2-lng1) ) * raio

# Argumentos: Dois pontos do trajeto
# Retorno: Distância em km entre esses dois pontos usando distancia euclidiana
def distancia_xy(p1: dict, p2: dict):
    return math.sqrt((p2["y"] - p1["y"])**2 + (p2["x"] - p1["x"])**2)