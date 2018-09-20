from pylab import *
from numpy import *
from scipy import integrate


def trapazoidal(func, a, b, h=0.001):
    return h * ((0.5 * (func(a) + func(b))) + sum(
        [func(a + k * h) for k in range(1, int((b - a) / h))]))


def simpson(func, a, b, h=0.001):
    n = int(abs(b - a) / h)
    n -= 1 if n % 2 == 1 else 0
    return (h / 3.0) * (
        func(a) + func(b) +
        (4.0 * sum([func(a + (k * h)) for k in range(1, n, 2)])) +
        (2.0 * sum([func(a + (k * h)) for k in range(2, n - 1, 2)])))


def adaptive(input_func, a, b, h=0.001, delta=10e-4):
    if a == inf and b == inf:
        func = lambda x: (input_func(-x/(1-x))+input_func(x/(1-x))) / pow(1-x,2)
        a = 0
        b = 1
    elif a != inf and b == inf:
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
    return i1, epsilon

real = 0.135257257949994654568013599782201031869552084055950138982
a = adaptive(lambda x: exp(-(x**2)), 1, 2, 0.001)
print(a)
# b = adaptive(lambda x: exp(-((x / (1 - x))**2)) / pow(1 - x, 2), 0,
#              1 - 0.0000001, 0.001, 1e-12)
# c = adaptive_a_to_inf(lambda x: exp(-x**2), 0, 0.001, 1e-12)
d = adaptive(lambda x: exp(-x**2), 0, inf, 0.001, 1e-12)
print(d)
