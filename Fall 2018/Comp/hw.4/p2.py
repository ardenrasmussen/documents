import numpy as np
import math
import pylab

G = 6.674e-11
M=5.974e24
m=7.348e22
R=3.844e8
w=2.662e-6

def Newtons(func, x_init, delta=1e-4):
    x = x_init
    # h = 0.5
    # df = lambda x: (func(x + h) - func(x - h)) / (2 * h)
    df = lambda x: -2*G*M/x**3-2*G*m/(R-x)**3-w**2
    while np.fabs(x) > delta:
        x -=  (func(x)/ df(x))
    return x

def main():
    func = lambda r: (G*M/r**2)-(G*m/(R-r)**2)-(w**2*r)
    approx = Newtons(func, R/2)
    print("r \u2245 {:e}m".format(approx))

if __name__ == "__main__":
    main()
