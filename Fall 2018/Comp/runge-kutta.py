import numpy as np
import pylab


def f(x, t):
    return -x**3 + np.sin(t)


def RungeKutta(func, init, a, b, h=0.1):
    # h = abs(b - a) / N
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

def f2(theta, omega, t):
    return -np.sin(theta)

def f1(theta, omega, t):
    return omega

def main():
    T, Theta, Omega = RungeKutta2(f1, f2, 0.1, 0, 0, 20)
    # pylab.plot(T, Theta)
    # pylab.plot(T, Omega)
    pylab.plot(Theta, Omega)
    pylab.plot(Omega, Theta)
    pylab.show()
    # X, Y = RungeKutta(f, 0, 0, 10)
    # EX, EY = Euler(f, 0, 0, 10)
    # pylab.plot(X, Y)
    # pylab.plot(EX, EY)
    # pylab.show()


if __name__ == "__main__":
    main()
