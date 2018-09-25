#!/usr/bin/python3

from pylab import *
from math import *
from numpy import *

def simpson(func, a, b, n=1000):
    """Approximates integral using simpson method"""
    n -= 1 if n % 2 == 1 else 0
    h = abs(b - a) / n
    return (h / 3.0) * (
        func(a) + func(b) +
        (4.0 * sum([func(a + (k * h)) for k in range(1, n, 2)])) +
        (2.0 * sum([func(a + (k * h)) for k in range(2, n - 1, 2)])))


def p1():
    """5.4: The diffraction limit of a telescope"""

    def J(m, x, n=1000):
        return (1 / pi) * simpson(lambda theta: cos(m * theta - x * sin(theta)),
                                  0, pi, n)

    def a():
        plot(linspace(0, 20), [J(0, x) for x in linspace(0, 20)])
        plot(linspace(0, 20), [J(1, x) for x in linspace(0, 20)])
        plot(linspace(0, 20), [J(2, x) for x in linspace(0, 20)])
        show()

    def b():
        print("This takes a little while to run...")
        max_r = 1e-6
        resolution = 50
        scale = max_r / resolution
        k = 2 * pi / (5e-7)
        I = lambda r: pow(J(1, k * r, 100) / (k * r), 2) if r != 0 else pow(J(1, k * 1e-9, 100) / (k * 1e-9), 2)
        D = lambda x, y: sqrt(x**2 + y**2)
        data = [[
            I(D(x - resolution, y - resolution) * scale)
            for x in range(resolution * 2 + 1)
        ]
                for y in range(resolution * 2 + 1)]
        imshow(data, vmax=0.01)
        # imshow(data)
        show()

    a()
    b()

if __name__ == "__main__":
    p1()
