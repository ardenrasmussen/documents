import numpy as np
import matplotlib.pyplot as plt

K = 1000
M = 5

def euler(x, v, a, dt, ti, tf):
    X = [x]
    V = [v]
    A = [a]
    for t in np.arange(ti, tf, dt):
        X.append(X[-1] + V[-1] * dt)
        V.append(V[-1] + A[-1] * dt)
        A.append(-K*X[-1] / M)
    return X[:-1], V[:-1], A[:-1]

def euler_cromer(x, v, a, dt, ti, tf):
    X = [x]
    V = [v]
    A = [a]
    for t in np.arange(ti, tf, dt):
        V.append(V[-1] + A[-1] * dt)
        X.append(X[-1] + V[-1] * dt)
        A.append(-K*X[-1]/ M)
    return X[:-1], V[:-1], A[:-1]

def analytical(x, v, a, dt, ti, tf):
    X = [x]
    V = [v]
    A = [a]
    E = 0.5*K*np.power(X[0], 2)
    omega=np.sqrt(K/M)
    beta = np.arcsin(np.sqrt(K/(2*E))*X[0])
    alpha = np.sqrt(2*E/K)
    for t in np.arange(ti, tf, dt):
        X.append(alpha*np.sin(omega*t+beta))
        V.append(alpha*omega*np.cos(omega*t+beta))
    return X[:-1], V[:-1], A

def main():
    T = np.arange(0, 1, 0.01)
    X, V, A = euler(0.1, 0, -20, 0.01, 0, 1)
    Xc, Vc, Ac = euler_cromer(0.1, 0, -20, 0.01, 0, 1)
    Xa, Va, Aa = analytical(0.1, 0, -20, 0.01, 0, 1)
    E = [0.5*K*pow(X[i], 2)+0.5*M*pow(V[i], 2) for i in range(len(X))]
    Ec = [0.5*K*pow(Xc[i], 2)+0.5*M*pow(Vc[i], 2) for i in range(len(Xc))]
    Ea = [0.5*K*pow(Xa[i], 2)+0.5*M*pow(Va[i], 2) for i in range(len(Xa))]
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(T, X, 'k--', label="Euler")
    ax1.plot(T, Xc, 'k:', label="Euler-Cromer")
    ax1.plot(T, Xa, 'k-', label="Analytical")
    ax1.set_title("X(t)")
    ax1.legend()
    ax2.plot(T, E, 'k--', label="Euler")
    ax2.plot(T, Ec, 'k:', label="Euler-Cromer")
    ax2.plot(T, Ea, 'k-', label="Analytical")
    ax2.set_title("E(t)")
    ax2.legend()
    fig.set_size_inches(6,9)
    # plt.savefig("hw1.ps", papertype="a4")
    plt.savefig("hw1.ps", papertype="a4")
    # plt.show()

if __name__ == "__main__":
    main()
