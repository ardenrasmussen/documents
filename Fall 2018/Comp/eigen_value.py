#!/usr/bin/python3
import numpy as np
import pylab

h_bar = 1.05e-35
en = 1.6e-19
m = 9.1e-31
l = 5.292e-11


def RungeKutta2(f1, f2, x_init, y_init, a, b, h=0.1, e=0):
    X = []
    Y = []
    T = np.arange(a, b, h)
    x = x_init
    y = y_init
    for t in T:
        X.append(x)
        Y.append(y)
        k1 = h * f1(x, y, t, e)
        l1 = h * f2(x, y, t, e)
        k2 = h * f1(x + k1 / 2, y + l1 / 2, t + h / 2, e)
        l2 = h * f2(x + k1 / 2, y + l1 / 2, t + h / 2, e)
        k3 = h * f1(x + k2 / 2, y + l2 / 2, t + h / 2, e)
        l3 = h * f2(x + k2 / 2, y + l2 / 2, t + h / 2, e)
        k4 = h * f1(x + k3, y + l3, t + h, e)
        l4 = h * f2(x + k3, y + l3, t + h, e)
        x += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y += (1 / 6) * (l1 + 2 * l2 + 2 * l3 + l4)
    return T, X, Y
    # return t, x, y


def main():
    v0 = 0
    L = 1000
    e2 = (8.539e-19)-(1e-19)
    e1 = (8.539e-19)+(1e-19)
    while np.fabs(L) > 1e-20:
        func_a = lambda psi, phi, x, e: phi
        # func_b = lambda phi, psi, x, e: (-2 * m) / h_bar**2 * psi * (v0 * (x / l) * (x / l - 1) + e)
        func_b = lambda psi, phi, x, e: (-2 * m) / h_bar**2 * psi * e
        t1, x1, y1 = RungeKutta2(func_a, func_b, 0, 1, 0, l, l / 100, e1)
        t2, x2, y2 = RungeKutta2(func_a, func_b, 0, 1, 0, l, l / 100, e2)
        print(e1, e2)
        # print(y1, y2)
        # print(x1, x2)
        pylab.plot(t1, x1)
        pylab.plot(t2, x2)
        pylab.show()
        L = x2[-1]
        e3 = e2 - (x2[-1] * (e2 - e1) / (x2[-1] - x1[-1]))
        e1 = e2
        e2 = e3
    print(">>", e2/en)


if __name__ == "__main__":
    main()
