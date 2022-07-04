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
    R = np.array([S[1], (-g/r)*math.sin(S[0]*pi/180), 1])
    return(R)

def get_initial_omega(experiment, dt):
    return (experiment[1] - experiment[0])/dt

def radians_to_angle(arr):
    return [e*180/pi for e in arr]
)
def main():
    theta = -2.0
    omega = 17.453
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
    
    experiments = [e1,e2,e3,e4,e5]
    experiments_radian = [[e*pi/180 for e in exp] for exp in experiments]
    initial_times = [0.0021, 0.0042, 0.0083, 0.0125, 0.0208]
    experiment_index = 0
    ti = initial_times[experiment_index]
    dt = 0.025
    tf = ti + dt*18
    theta = experiments_radian[experiment_index][0]
    omega = get_initial_omega(experiments_radian[experiment_index], dt)
    vec = initState(theta, omega, ti)
    states = [vec]
    thetas = [vec[0]]
    omegas = [vec[1]]
    times = [vec[2]]
    while ti <= tf:
        vec = nextState(vec, dt)
        states.append(vec)
        thetas.append(vec[0])
        omegas.append(vec[1])
        times.append(vec[2])
        ti += dt

    print(states)
    print(len(e1))
    print(len(times))
    print(len(thetas))
    plt.scatterexperiments[expexperiment_index]1, times)
    plt.plotradians_to_angle(thetas)s, times)
    plt.show()

if __name__ == "__main__":
    main()
