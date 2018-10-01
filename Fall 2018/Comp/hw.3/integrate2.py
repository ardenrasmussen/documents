from numpy import inf, sqrt
from math import pow

def trapazoidal(f, ax, bx, ay, by, h=0.001):
    h2 = h**2
    Nx = int(abs(bx - ax) / h)
    Ny = int(abs(by - ay) / h)
    corner = 0.25*(f(ax, ay) + f(ax, by) + f(bx, ay) + f(bx, by))
    edge = 0.5 * (sum([f(ax, ay + i*h) for i in range(1, Ny)])
                + sum([f(bx, ay + i * h) for i in range(1, Ny)])
                + sum([f(ax + i*h,ay) for i in range(1, Nx)])
                + sum([f(ax+i*h, by) for i in range(1, Nx)]))
    inner = sum([sum([f(ax+i*h, ay+k*h) for k in range(1, Ny)]) for i in range(1, Nx)])
    return (h**2) * (corner + edge + inner)

z = 1
L = 1
