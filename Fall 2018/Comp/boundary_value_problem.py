#!/usr/bin/python3
import numpy as np
import pylab

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

def main():
    # 0.1-1
    data = []
    for gamma in np.linspace(0.0001,0.009):
    # for gamma in np.linspace(0.0001,100.0):
        func_a = lambda x, v, t: v
        func_b = lambda x, v, t: -9.8 - (gamma * v**2)
        func_b = lambda x, v, t: -9.8 - (gamma * v)
        X = [100]
        v2 = 0.0
        v1 = 1000.0
        while(np.fabs(X[-1]) > 1e-4):
            v_new = (v1+v2)/2.0
            T, X, Y = RungeKutta2(func_a, func_b, 0, v_new, 0, 10, 0.01)
            if X[-1] > 0:
                v1 = v_new
            else:
                v2 = v_new
        data.append(v1)
        print(Y[-1])
        print(gamma, v1)
    #     pylab.plot(np.arange(0, 10, 0.01), X)
    # pylab.show()
    # pylab.plot(np.linspace(0.0001,0.009), data)
    pylab.plot(np.linspace(0.0001,100.0), data)
    pylab.show()

if __name__ == "__main__":
    main()
