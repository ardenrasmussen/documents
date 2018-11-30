import numpy as np
import pylab

m = 9.1094e-31
hbar = 1.0546e-34
e = 1.6022e-19
V0 = 50 * e
a = 1e-11
N = 1000
L = 20 * a
h = L / N


def V1(x):
    return V0 * (x**2) / (a**2)


def V2(x):
    return V0 * (x**4) / (a**4)


def f(r, x, E, V):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    # print(V(x)-E)
    fphi = (2 * m / hbar**2) * (V(x) - E) * psi
    # if x == -L/2 or x == L/2:
    #     fphi = 0
    return np.array([fpsi, fphi], float)


def solve(E, V):
    psi = 0.0
    phi = 1.0
    r = np.array([psi, phi], float)
    y = []

    for x in np.arange(-L / 2, L / 2, h):
        k1 = h * f(r, x, E, V)
        k2 = h * f(r + 0.5 * k1, x + 0.5 * h, E, V)
        k3 = h * f(r + 0.5 * k2, x + 0.5 * h, E, V)
        k4 = h * f(r + k3, x + h, E, V)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y.append(r[0])

    return r[0], y


def get_state(e1, e2, V):
    E1 = e1
    E2 = e2
    psi2, plt = solve(E1, V)

    target = e / 1000
    while abs(E1 - E2) > target:
        psi1 = psi2
        psi2, plt = solve(E2, V)
        E1, E2 = E2, E2 - psi2 * (E2 - E1) / (psi2 - psi1)
    return E2 / e, plt

def integrate(data):
    return h * ((0.5 * (np.fabs(data[0])**2 + np.fabs(data[-1])**2)) + sum([np.fabs(x)**2 for x in data]))

def main():
    print("E0 {}".format(get_state(0.0, e, V1)[0]))
    print("E1 {}".format(get_state(e, 300 * e, V1)[0]))
    print("E2 {}".format(get_state(300 * e, 500 * e, V1)[0]))
    print("E0 {}".format(get_state(0.0, 300*e, V2)[0]))
    print("E1 {}".format(get_state(300*e, 900 * e, V2)[0]))
    print("E2 {}".format(get_state(900 * e, 1200 * e, V2)[0]))
    global L
    L = 10*a
    _, E1 = get_state(0.0, 300*e, V2)
    _, E2 = get_state(300*e, 900*e, V2)
    _, E3 = get_state(900*e, 1200*e, V2)
    scale_1 = integrate(E1)
    scale_2 = integrate(E2)
    scale_3 = integrate(E3)
    X = np.arange(-L/2, L/2, h)
    E1 = [np.fabs(x)**2/scale_1 for x in E1]
    E2 = [np.fabs(x)**2/scale_2 for x in E2]
    E3 = [np.fabs(x)**2/scale_3 for x in E3]
    pylab.plot(X, E1)
    pylab.plot(X, E2)
    pylab.plot(X, E3)
    pylab.show()

if __name__ == "__main__":
    main()
