#!/usr/bin/python3

from pylab import *
from numpy import *

def simpson(func, a, b, h=0.1):
    """Approximates integral using simpson method"""
    n = int(abs(b - a) / h)
    n -= 1 if n % 2 == 1 else 0
    I1 = (h / 3.0) * (
        func(a) + func(b) +
        (4.0 * sum([func(a + (k * h)) for k in range(1, n, 2)])) +
        (2.0 * sum([func(a + (k * h)) for k in range(2, n - 1, 2)])))
    h2 = 2 * h
    n2 = int(abs(b - a) / h2)
    n2 -= 1 if n2 % 2 == 1 else 0
    I2 = (h2 / 3.0) * (
        func(a) + func(b) +
        (4.0 * sum([func(a + (k * h2)) for k in range(1, n2, 2)])) +
        (2.0 * sum([func(a + (k * h2)) for k in range(2, n2 - 1, 2)])))
    return (I1, abs(I1 - I2) / 3)

def RMI(T, T_max, E1, E2, E3):
    return simpson(lambda x: (2*E1(x)-E2(x)-2*E3(x)) / x**2, T, T_max)

def p3():
    pass

if __name__ == "__main__":
    p3()
