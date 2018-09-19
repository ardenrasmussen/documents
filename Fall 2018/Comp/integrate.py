from pylab import *
from numpy import *
from scipy import integrate


def trapazoidal(func, a, b, h):
    return h * ((0.5 * (func(a) + func(b))) + sum(
        [func(a + k * h) for k in range(1, int((b - a) / h))]))


def simpson(func, a, b, h):
    n = int(abs(b - a) / h)
    n -= 1 if n % 2 == 1 else 0
    return (h / 3.0)*(func(a) + func(b) +
                   (4.0 * sum([func(a + (k * h)) for k in range(1, n, 2)])) +
                   (2.0 * sum([func(a + (k * h)) for k in range(2, n - 1, 2)])))


real = 0.135257257949994654568013599782201031869552084055950138982
a = simpson(lambda x: exp(-(x**2)), 1, 2, 0.00001)
print(a)
