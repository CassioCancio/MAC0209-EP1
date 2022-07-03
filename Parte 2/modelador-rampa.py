import math

def main():
    # Variáveis prontas
    g = 9.8             # Aceleração gravitacional (m/s^2)
    massa = 0.3807      # Massa (kg)
    cinetico = 0.197    # Coeficiente de atrito cinetico
    estatico = 0.297    # Coeficiente de atrito estático
    v = 0               # Velocidade inicial (m/s)
    a = 0               # Aceleração inicial (m/s^2)

    # Variáveis que devem ser definidas
    # Chave para ativar o atrito
    atrito = True
    # Posição inicial (cm)
    x = 0.192
    # Ângulo (°)
    teta = 20.84
    # Variação de tempo entre cada cálculo (s)
    dt = 1/30
    # Tempo final da simulação (s)
    t_final = 0.45
    # Tempo inicial da simulação (s)
    t_inicial = 1/30

    estados = [("Tempo","Posição em cm")]
    teta = teta * math.pi/180

    while(t_inicial <= t_final):
        x += v*dt
        v += a*dt

        if not(atrito): a = g*math.sin(teta)
        elif v == 0:    a = g*(math.sin(teta)-estatico*math.cos(teta))
        else:           a = g*(math.sin(teta)-cinetico*math.cos(teta))
        estados.append((t_inicial,x))
        t_inicial += dt

    imprimir(estados)

def imprimir(estados: list):
    print(f"{estados[0][0]}\t {estados[0][1]}")
    del estados[0]

    for elem in estados:
        print(f"{elem[0]:.3f}\t {elem[1]*100:.2f}")

if __name__ == "__main__":
    main()