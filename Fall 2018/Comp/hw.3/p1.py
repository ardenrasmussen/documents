from integrate2 import trapazoidal
from numpy import arange
from pylab import *
from pprint import pprint


def p1():

    def force(z):
        return lambda x, y: 0 if x == y == z == 0 else pow(x**2+ y**2+z**2,-3/2)

    def b():
        G = 6.674e-11
        sigma = 100
        fz = [
            G * sigma * z * trapazoidal(force(z), -5, 5, -5, 5, 0.1)
            for z in arange(0, 10, 0.1)
        ]
        plot(arange(0, 10, 0.1), fz)
        show()

    b()


def p2():
    ep = 8.854187871e-12

    # ep=1

    def dist(p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 +
                    (p1[2] - p2[2])**2)

    def diff(a, b):
        return abs(a - b) >= 1e-5

    def V(q, r):
        return q / (4 * pi * ep * r)

    def E(q, r):
        return q / (4 * pi * ep * r**2)

    def potential(x, y, z):
        return V(-1, dist([-0.05, 0, 0], [x, y, z])) + V(
            1, dist([0.05, 0, 0], [x, y, z]))

    def Ex(x, y, z):
        return ((1 * (x + 0.05)) / (dist([-0.05, 0, 0], [x, y, z])**3)
               ) if diff(x, -0.05) and diff(y, 0) else 0 + (
                   (1 * (x - 0.05)) / (dist([0.05, 0, 0], [x, y, z])**3)
               ) if diff(x, 0.05) and diff(y, 0) else 0
        # return ((-1 * (x + 0.05)) / (dist([-0.05, 0, 0], [x, y, z])**3)) if x + 0.05 >= 1e-5 and y-0>= 1e-5 else 0 + (
        #     (1 * (x - 0.05)) / (dist([0.05, 0, 0], [x, y, z])**3)) if x - 0.05 >= 1e-5 and y-0 >= 1e-5 else 0

    def Ey(x, y, z):
        return ((1 * y) / (dist([-0.05, 0, 0], [x, y, z])**3)
               ) if diff(x, -0.05) and diff(y, 0) else 0 + (
                   (1 * y) / (dist([0.05, 0, 0], [x, y, z])**3)
               ) if diff(x, 0.05) and diff(y, 0) else 0
        # return ((-1 * y) / (dist([-0.05, 0, 0], [x, y, z])**3)
        #        ) if x + 0.05 >= 1e-5 and y - 0 >= 1e-5 else 0 + (
        #            (1 * y) / (dist([0.05, 0, 0], [x, y, z])**3)
        #        ) if x - 0.05 >= 1e-5 and y - 0 >= 1e-5 else 0

    def Emag(x, y, z):
        # print(dist([-0.05, 0, 0], [x, y, z]), dist([0.05, 0, 0], [x, y, z]))
        # print(
        #     E(1, dist([-0.05, 0, 0], [x, y, z])),
        #     E(1, dist([0.05, 0, 0], [x, y, z])))
        return E(1, dist([-0.05, 0, 0], [x, y, z])) + E(
            1, dist([0.05, 0, 0], [x, y, z]))
        # return (-1)/(4*pi*ep*r**2)
        # return sqrt(Ex(x, y, z)**2 + Ey(x, y, z))

    def a():
        data = [[potential(x, y, 0)
                 for x in arange(-0.5, 0.5, 0.01)]
                for y in arange(-0.5, 0.5, 0.01)]
        imshow(data, vmax=1e10, vmin=-1e10)
        # imshow(data, vmax=0.7, vmin=-0.7)
        show()

    def b():
        data = [[Emag(x, y, 0)
                 for x in arange(-0.5, 0.5, 0.01)]
                for y in arange(-0.5, 0.5, 0.01)]
        # data = [[Emag(x, y, 0) for x in arange(-5, 5, 0.1)] for y in arange(-5, 5, 0.1)]
        vec_u = [[Ex(x, y, 0)
                  for x in arange(-0.5, 0.5, 0.01)]
                 for y in arange(-0.5, 0.5, 0.01)]
        vec_v = [[Ey(x, y, 0)
                  for x in arange(-0.5, 0.5, 0.01)]
                 for y in arange(-0.5, 0.5, 0.01)]
        # pprint(vec_u)
        imshow(data, vmax=1e11, vmin=-1e11)
        quiver(vec_u, vec_v)
        show()

    a()
    b()


if __name__ == "__main__":
    # p1()
    p2()
