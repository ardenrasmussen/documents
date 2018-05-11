import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
from scipy.special import gamma


def gam(a, b):
    return gamma(a) * (1 - gammainc(a, b))


def gen(n, l=pi):

    def poisson(x):
        if x < 0:
            return 0
        else:
            return ((x - n) / factorial(n)) * pow(x, n - 1) * exp(-x)

    return poisson

def coef(n, l=pi):
    length = (1 + 4 * pow(n, 2)) * gam(2 * n + 1, 2 * l) - (
        4 * n) * gam(2 * n, 2 * l) - (
            1 - 4 * pow(n, 2)) * gam(2 * n + 1, 0) + (4 * n) * gam(2 * n, 0)
    length *= -(pow(2, 2 * n - 1) / pow(factorial(n), 2))
    y = n*gam(n+2,l)-gam(n+3,l)-n*gam(n+2,0)+gam(n+3,0)
    y /= factorial(n)
    return y

def func(n):
    def f(x):
        return coef(n) * gen(n)(x)
    return f

def approx(x):
    return sum([coef(n) * gen(n)(x) for n in range(1, 10)])

def x2(x):
    return pow(x, 2)

def plot(func):
    x = np.linspace(-pi, pi, 500)
    plt.plot(x, [func(_) for _ in x])


print(coef(1))

plot(x2)
plot(func(1))
plot(func(2))
plot(func(3))
plot(func(4))
plot(func(5))
# plot(approx)
# plot(gen(1))
# plot(gen(2))
# plot(gen(3))
# plot(gen(4))
# plot(gen(5))
plt.show()
