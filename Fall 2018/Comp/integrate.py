# from pylab import *
# from numpy import *
# from scipy import integrate
from numpy import inf
from math import *
import re


def trapazoidal(func, a, b, h=0.001):
    """Approximates integral using trapazoidal method"""
    return h * ((0.5 * (func(a) + func(b))) + sum(
        [func(a + k * h) for k in range(1, int((b - a) / h))]))


def simpson(func, a, b, h=0.001):
    """Approximates integral using simpson method"""
    # n = int(abs(b - a) / h)
    # n -= 1 if n % 2 == 1 else 0
    n = 100
    h = (b-a)/n
    print(sum([func(a + (k * h)) for k in range(1, n, 2)]))
    print(sum([func(a + (k * h)) for k in range(2, n-1, 2)]))
    return (h / 3.0) * (
        func(a) + func(b) +
        (4.0 * sum([func(a + (k * h)) for k in range(1, n, 2)])) +
        (2.0 * sum([func(a + (k * h)) for k in range(2, n - 1, 2)])))


def adaptive(input_func, a, b, h=0.001, delta=10e-4):
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
    return i1, epsilon


def input_func(prompt):
    """Generates lambda from user input"""
    func_string = input(prompt)
    return eval("lambda x: " + re.sub(r'(\d)(\w)', r'\1*\2', func_string.strip().replace('^', '**')))


def main():
    """Main function"""
    func = input_func("Enter f(x): ")
    start, end = input("Enter domain (a,b): ").split()
    start = float(start) if start not in ('-inf', 'inf') else (
        inf if start == 'inf' else -inf)
    end = float(end) if end not in ('-inf',
                                    'inf') else (inf if end == 'inf' else -inf)
    # print(adaptive(func, start, end, 0.001))
    print(simpson(func, start, end))
    # d = adaptive(lambda x: exp(-x**2), 0, inf, 0.001, 1e-12)


if __name__ == "__main__":
    main()
