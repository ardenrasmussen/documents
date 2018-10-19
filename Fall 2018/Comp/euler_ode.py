import numpy as np
import pylab

def f(x, t):
    return -x**3+np.sin(t)

def Euler(func, init, a, b, N=1000):
    h = abs(b - a) / N
    x = init
    X = []
    T = np.arange(a, b, h)
    for t in T:
        X.append(x)
        x += h*func(x,t)
    return X, T

def main():
    Y, T = Euler(f, 0, 0, 10)
    pylab.plot(T, Y)
    pylab.show()
    pass

if __name__ == "__main__":
    main()
