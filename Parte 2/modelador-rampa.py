import math
from turtle import pos
from animacao import animar_rampa
from matplotlib import pyplot as plt

def main():
    # Variáveis prontas
    g = 9.8             # Aceleração gravitacional (m/s^2)
    massa = 0.3807      # Massa (kg)
    cinetico = 0.19     # Coeficiente de atrito cinetico
    estatico = 0.270    # Coeficiente de atrito estático
    v = 0               # Velocidade inicial (m/s)
    a = 0               # Aceleração inicial (m/s^2)

    # Variáveis que devem ser definidas
    # Chave para ativar o atrito
    atrito = True
    # Posição inicial (cm)
    x = 0.192
    # Ângulo (°)
    teta = 16.2
    # Variação de tempo entre cada cálculo (s)
    dt = 1/30
    # Tempo final da simulação (s)
    t_final = 1.105
    # Tempo inicial da simulação (s)
    t_inicial = 0.701

    estados = [("Tempo","Posição em cm")]
    
    animacao = []
    
    teta = teta * math.pi/180

    animacao.append((math.cos(teta)*x,math.sin(teta)*x))

    tempo = []
    posicao = []
    
    while(t_inicial <= t_final):
        x += v*dt
        v += a*dt
        
        if not(atrito): a = g*math.sin(teta)
        elif v == 0:    a = g*(abs(math.sin(teta)-estatico*math.cos(teta)))
        else:           a = g*(abs(math.sin(teta)-cinetico*math.cos(teta)))
        estados.append((t_inicial,x))

        tempo.append(t_inicial)
        posicao.append(x)

        t_inicial += dt

        animacao.append((math.cos(teta)*x,math.sin(teta)*x))

    imprimir(estados)

    print(posicao)
    pos = []
    pos.append(posicao)
    pos.append([0.194, 0.194, 0.194, 0.196, 0.198, 0.202, 0.207, 0.213, 0.219, 0.228, 0.232, 0.248, 0.259])

    # print(f"Largura: {len(pos[0])} {len(pos[1])} {len(tempo)}")

    plotar_dados("Tempo em segundos","Posição em metros", tempo, pos)
    # animar_rampa(animacao, teta)

def plotar_dados(x_title: str, y_title: str, tempo: list, posicao: list):
    plt.plot(tempo, posicao[0], "-m", label="Simulação")
    plt.plot(tempo, posicao[1], "-c", label="Experimento")
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.legend()
    plt.grid()
    plt.show()


def imprimir(estados: list):
    print(f"{estados[0][0]}\t {estados[0][1]}")
    del estados[0]

    for elem in estados:
        print(f"{elem[0]:.3f}\t {elem[1]*100:.2f}")

if __name__ == "__main__":
    main()
