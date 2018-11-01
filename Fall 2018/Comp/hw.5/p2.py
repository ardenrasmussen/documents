import numpy as np
import pylab
from multiprocessing import Pool, cpu_count


def RungeKutta(func, init, a, b, h=0.1):
    X = []
    T = np.arange(a, b, h)
    x = init
    for t in T:
        X.append(x)
        k1 = h * func(x, t)
        k2 = h * func(x + k1 / 2, t + h / 2)
        k3 = h * func(x + k2 / 2, t + h / 2)
        k4 = h * func(x + k3, t + h)
        x += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return T, X


def RungeKutta2(f1, f2, x_init, y_init, a, b, h=0.1):
    X = []
    Y = []
    T = np.arange(a, b, h)
    x = x_init
    y = y_init
    for t in T:
        if(x > np.pi):
            x -= 2 * np.pi
        if(x < -np.pi):
            x += 2 * np.pi
        if (2*t/3) % (2*np.pi) <= h and t > 100:
            X.append(x)
            Y.append(y)
        k1 = h * f1(x, y, t)
        l1 = h * f2(x, y, t)
        k2 = h * f1(x + k1 / 2, y + l1 / 2, t + h / 2)
        l2 = h * f2(x + k1 / 2, y + l1 / 2, t + h / 2)
        k3 = h * f1(x + k2 / 2, y + l2 / 2, t + h / 2)
        l3 = h * f2(x + k2 / 2, y + l2 / 2, t + h / 2)
        k4 = h * f1(x + k3, y + l3, t + h)
        l4 = h * f2(x + k3, y + l3, t + h)
        x += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y += (1 / 6) * (l1 + 2 * l2 + 2 * l3 + l4)
    return T, X, Y

def helper(fD):
    g = 9.8
    l = 9.8
    q = 0.5
    t_max = 200
    OmegaD=2/3
    f1 = lambda theta,omega,t: omega
    f2 = lambda theta,omega,t: -(g/l)*np.sin(theta)-q*omega+fD*np.sin(OmegaD*t)
    T, Theta, Omega = RungeKutta2(f1, f2, 0.2, 0, 0, t_max, 0.001)
    return [(fD, x) for x in Theta]


def main():
    FD = np.linspace(1.35, 1.6, 50)
    pool = Pool(4)
    pts  = pool.map(helper, FD)
    pts = [j for i in pts for j in i]
    pylab.plot(*zip(*pts), 'k.')

    pylab.show()


if __name__ == "__main__":
    main()
