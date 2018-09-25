#!/usr/bin/python3

from pylab import *
from math import *
from numpy import *


def simpson(func, a, b, h=0.1):
    """Approximates integral using simpson method"""
    n = int(abs(b - a) / h)
    n -= 1 if n % 2 == 1 else 0
    return (h / 3.0) * (
        func(a) + func(b) +
        (4.0 * sum([func(a + (k * h)) for k in range(1, n, 2)])) +
        (2.0 * sum([func(a + (k * h)) for k in range(2, n - 1, 2)])))

def adaptive(input_func, a, b, h=0.1, delta=10e-6):
    """Approximates integral using adaptive method"""
    if a > b:
        val = adaptive(input_func, b, a, h=h, delta=delta)
        return (-val[0], val[1])
    if a == -inf and b == inf:
        func = lambda x: (input_func(-x/(1-x))+input_func(x/(1-x))) / pow(1-x,2)
        a = 0
        b = 1
    elif a != -inf and b == inf:
        func = lambda x: input_func((x / (1 - x)) + a) / pow(1 - x, 2)
        a = 0
        b = 1
    else:
        func = input_func
    try:
        func(a)
    except ZeroDivisionError:
        a += 0.00000000000001
    try:
        func(b)
    except ZeroDivisionError:
        b -= 0.00000000000001
    n = int(abs(b - a) / h)
    i0 = h * ((0.5 * (func(a) + func(b))) + sum(
        [func(a + k * h) for k in range(1, int((b - a) / h))]))
    epsilon = delta + 10
    while epsilon > delta:
        h /= 2
        n *= 2
        i1 = (0.5 * i0) + (h * sum([func(a + k * h) for k in range(1, n, 2)]))
        epsilon = abs(i1 - i0) / 3
        i0 = i1
    return i1


class Vec(object):

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        if isinstance(x, list):
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
        elif isinstance(x, Vec):
            self.x = x.x
            self.y = x.y
            self.z = x.z

    def __add__(self, b):
        if isinstance(b, Vec):
            return Vec(self.x + b.x, self.y + b.y, self.z + b.z)
        return Vec(self.x + b, self.y + b, self.z + b)

    def __sub__(self, b):
        if isinstance(b, Vec):
            return Vec(self.x - b.x, self.y - b.y, self.z - b.z)
        return Vec(self.x - b, self.y - b, self.z - b)

    def __mul__(self, b):
        if isinstance(b, Vec):
            return Vec(self.x * b.x, self.y * b.y, self.z * b.z)
        return Vec(self.x * b, self.y * b, self.z * b)

    def __div__(self, b):
        if isinstance(b, Vec):
            return Vec(self.x / b.x, self.y / b.y, self.z / b.z)
        return Vec(self.x / b, self.y / b, self.z / b)


def p2():
    """The potential and electric field of a linear charge distribution"""

    def mag2(x, xp, y, yp, z, zp):
        return (x - xp)**2 + (y - yp)**2 + (z - zp)**2

    def V(x, y, z, rho=lambda x, y, z: 1, epsilon=1, integrate=simpson):
        pre = 1 / (4 * pi * epsilon)

        def func(theta):
            xp = 3 * cos(theta)
            yp = 2 * sin(theta)
            zp = 0
            return rho(xp, yp, zp) / sqrt(mag2(x, xp, y, yp, z, zp)) * sqrt(mag2(xp, 0, yp, 0, zp, 0))

        return pre * integrate(func, 0, 2 * pi)

    def E(x, y, z, rho=lambda x, y, z: 1, epsilon=1, integrate=simpson):
        pre = 1 / (4 * pi * epsilon)

        def func(theta):
            xp = 3 * cos(theta)
            yp = 2 * sin(theta)
            zp = 0
            return (rho(xp, yp, zp) * sqrt(mag2(x, xp, y, yp, z, zp))) / pow(
                mag2(x, xp, y, yp, z, zp), 3 / 2)

        return pre * integrate(func, 0, 2 * pi)

    def two():
        print(V(1, 4, 7, integrate=simpson))
        print(E(1, 4, 7, integrate=simpson))

    def three():
        print(V(1, 2, 5, integrate=adaptive))
        print(E(1, 2, 5, integrate=adaptive))

    def four():
        resolution = 50
        scale = 4.5 / resolution
        data = [[V(x*scale, y*scale, 1) for x in range(-resolution, resolution + 1)] for y in range(-resolution, resolution + 1)]
        imshow(data)
        show()

    two()
    three()
    four()


if __name__ == "__main__":
    p2()
