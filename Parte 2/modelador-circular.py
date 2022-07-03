import numpy as np
from matplotlib import pyplot as plt
import math

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

def main():
    theta = -2.0
    omega = 17.453
    # Experimento 2: (teta)
    e1 = [-92.0,-67.0,-42.0,-18.0,2.0,20.5,37.5,52.5,66.0,80.0,93.0,108.0,122.5,139.0,158.0,179.0,201.0,224.0,247.0]
    e1 = [e + 90 for e in e1]
    print(e1)
    # Experimento 3: (teta)
    e2 = [-88.5,-64.0,-39.0,-17.5,3.0,23.0,38.0,53.0,67.5,81.0,94.5,108.0,123.0,140.0,160.0,180.0,203.0,236.0,250.0]
    # Experimento 5: (teta)
    e3 = [-84.0,-59.0,-35.0,-13.0,7.0,25.0,41.0,56.0,70.0,83.0,97.5,111.0,127.0,144.0,163.0,184.0,206.0,230.0,254.0]
    # Experimento 7: (teta)
    e4 = [-80.0,-54.5,-31.5,-9.5,10.0,28.0,43.5,58.0,72.0,85.5,99.0,114.0,130.0,147.0,166.0,188.0,210.0,234.0,258.0]
    # Experimento 9: (teta)
    e5 = [-72.0,-46.5,-24.5,-3.5,17.0,35.5,49.0,63.0,77.0,90.0,104.0,119.0,135.0,154.0,174.0,195.0,218.0,242.5,266.0]
    # omega = 
    ti = 0.0021
    dt = 0.025
    tf = 0.4521
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
    plt.scatter(e1, times[:-1])
    plt.plot(thetas[:-1], times[:-1])
    plt.show()

if __name__ == "__main__":
    main()
