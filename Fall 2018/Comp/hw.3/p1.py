from numpy import arange
from pylab import *


def trapazoidal(f, ax, bx, ay, by, h=0.001):
    h2 = h**2
    Nx = int(abs(bx - ax) / h)
    Ny = int(abs(by - ay) / h)
    corner = 0.25 * (f(ax, ay) + f(ax, by) + f(bx, ay) + f(bx, by))
    edge = 0.5 * (sum([f(ax, ay + i * h) for i in range(1, Ny)]) + sum([
        f(bx, ay + i * h) for i in range(1, Ny)
    ]) + sum([f(ax + i * h, ay) for i in range(1, Nx)]) + sum(
        [f(ax + i * h, by) for i in range(1, Nx)]))
    inner = sum([
        sum([f(ax + i * h, ay + k * h)
             for k in range(1, Ny)])
        for i in range(1, Nx)
    ])
    return (h**2) * (corner + edge + inner)


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

if __name__ == "__main__":
    p1()
