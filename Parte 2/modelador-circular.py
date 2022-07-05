import numpy as np
from matplotlib import pyplot as plt
import math
from math import pi

def initState(theta, omega,t):
    S = np.array([theta, omega, t])
    return(S)

def nextState(S,dt):
    Sn = S + dt * rate(S,dt)
    return(Sn)

def rate(S,dt):
    g = 9.807
    r = 0.145
    R = np.array([S[1], (-g/r)*math.sin(S[0]), 1])
    return(R)

class Experiment_Handler:
    # todos dados de experimento abaixo representam angulos em graus
    # Experimento 2: (teta)
    e1 = [-2.0, 23.0, 48.0, 72.0, 92.0, 110.5, 127.5, 142.5, 156.0, 170.0, 183.0, 198.0, 212.5, 229.0, 248.0, 269.0, 291.0, 314.0, 337.0]
    # Experimento 3: (teta)
    e2 = [1.5, 26.0, 51.0, 72.5, 93.0, 113.0, 128.0, 143.0, 157.5, 171.0, 184.5, 198.0, 213.0, 230.0, 250.0, 270.0, 293.0, 326.0, 340.0]
    # Experimento 5: (teta)
    e3 = [6.0, 31.0, 55.0, 77.0, 97.0, 115.0, 131.0, 146.0, 160.0, 173.0, 187.5, 201.0, 217.0, 234.0, 253.0, 274.0, 296.0, 320.0, 344.0]
    # Experimento 7: (teta)
    e4 = [10.0, 35.5, 58.5, 80.5, 100.0, 118.0, 133.5, 148.0, 162.0, 175.5, 189.0, 204.0, 220.0, 237.0, 256.0, 278.0, 300.0, 324.0, 348.0]
    # Experimento 9: (teta)
    e5 = [18.0, 43.5, 65.5, 86.5, 107.0, 125.5, 139.0, 153.0, 167.0, 180.0, 194.0, 209.0, 225.0, 244.0, 264.0, 285.0, 308.0, 332.5, 356.0]
    # Lista de cada experimento:
    experiments = [e1, e2, e3, e4, e5]
    experiments_radian = [[e*pi/180 for e in exp] for exp in experiments]

    # Tempos iniciais de cada experimento:
    initial_times = [0.0021, 0.0042, 0.0083, 0.0125, 0.0208]

    dt = 0.025         # intervalo de tempo constante para cada experimento.

    def radians_to_angle(self, arr):
        return [elem*180/pi for elem in arr]

    def get_initial_omega(self, index):
        return (self.experiments_radian[index][1] - self.experiments_radian[index][0])/self.dt

    def __init__(self, experiment_index, intervals=18):
        self.index = experiment_index
        self.ti = self.initial_times[self.index]
        self.tf = self.ti + self.dt*intervals
        self.theta = self.experiments_radian[self.index][0]
        self.omega = self.get_initial_omega(self.index)

    def train(self):
        self.state_vec = initState(self.theta, self.omega, self.ti)
        self.states = [self.state_vec]
        self.thetas_vec = [self.theta]
        self.omegas_vec = [self.omega]
        self.time_vec = [self.ti]
        
        while self.ti <= self.tf:
            self.state_vec = nextState(self.state_vec, self.dt)
            self.states.append(self.state_vec)
            self.thetas_vec.append(self.state_vec[0])
            self.omegas_vec.append(self.state_vec[1])
            self.time_vec.append(self.state_vec[2])
            self.ti += self.dt

    def graph(self):
        plt.plot(self.time_vec, self.experiments[self.index], color="cyan", label="Experimento")
        plt.plot(self.time_vec, self.radians_to_angle(self.thetas_vec), color="magenta", label="Simulação")
        plt.ylabel("Ângulo em graus")
        plt.xlabel("Tempo em segundos")
        plt.legend()
        plt.grid()
        plt.show()


def main():
    experiment_index = 0   # escolher qual dos experimentos a modelar
    experiment = Experiment_Handler(experiment_index)
    experiment.train()
    experiment.graph()

if __name__ == "__main__":
    main()
