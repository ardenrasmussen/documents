from pylab import *
from math import *
from numpy import *


def prompt_func(*functions, quit_one=False):
    names = []
    for func in functions:
        names.append((func.__name__, func.__doc__))

    def help():
        print("quit/help")
        print("Functions are:", end='\n')
        for name in names:
            print("{}: {}".format(name[0], name[1]))

    def call(name):
        for func in functions:
            if name == func.__name__:
                func()

    def in_names(name):
        for n in names:
            if name == n[0]:
                return True
        return False

    help()
    value = ''
    while value != 'quit':
        value = input(">>> ")
        if in_names(value):
            call(value)
            if quit_one:
                return
        elif value == "help":
            help()
        elif value != "quit":
            print("Not a valid command/function")


def p1():
    """Fibonacci Sequence: Prints all the sequence from 1 to Max"""
    vmaximum = int(input('Max: '))
    fibs = [1, 1]
    while fibs[-1] < vmaximum:
        fibs.append(fibs[-1] + fibs[-2])
    if fibs[-1] > vmaximum:
        fibs.pop()
    print(*fibs)


def p2():
    """2.9: The Madelung Constant"""
    limit = int(input("L: "))

    def v(i, j, k):
        """Calculates the \"Potential\" created by an atom"""
        return (-1 if
                (i + j + k) % 2 == 1 else 1) * 1 / sqrt(i**2 + j**2 + k**2)

    madelung = 0
    for i in range(-limit, limit + 1):
        for j in range(-limit, limit + 1):
            for k in range(-limit, limit + 1):
                if i == j == k == 0:
                    continue
                madelung += v(i, j, k)
    print(madelung)


def p3():
    """2.10: the Semi-Emperical Mass Formula"""

    def calc_b(A, Z):
        return (15.8 * A) - (18.3 * pow(A, 2 / 3)) - (0.714 * (
            pow(Z, 2) / pow(A, 1 / 3))) - (23.2 * (pow(A - 2 * Z, 2) / A)) + (
                (0 if A % 2 == 1 else
                 (12.0 if Z % 2 == 0 else -12.0)) / pow(A, 1 / 2))

    def a():
        """Stuff"""
        a = int(input("A: "))
        z = int(input("Z: "))
        print(calc_b(a, z))

    def b():
        """More Stuff"""
        a = int(input("A: "))
        z = int(input("Z: "))
        print(calc_b(a, z) / a)

    def c():
        """Part C"""
        z = int(input("Z: "))
        bn = []
        for a in range(z, 3 * z + 1):
            bn.append(calc_b(a,z) / a)
        print(z + bn.index(max(bn)), max(bn))

    def d():
        """More parts"""
        zbn = []
        for z in range(1, 100):
            bn = []
            for a in range(z, 3 * z + 1):
                bn.append(calc_b(a,z)/a)
            print("{}:".format(z), z + bn.index(max(bn)), max(bn))
            zbn.append(max(bn))
        print("Max at:", 1 + zbn.index(max(zbn)), max(zbn))

    prompt_func(a, b, c, d, quit_one=True)

def p4():
    """2.12: Prime Numbers"""
    max_prime = int(input("Max: "))
    primes = [2]

    def is_prime(n):
        sqrt_n = sqrt(n)
        for p in primes:
            if p > sqrt_n:
                return True
            if n % p == 0:
                return False
    for n in range(3, max_prime, 2):
        if is_prime(n):
            primes.append(n)
    print(", ".join([str(x) for x in primes]))

def p5():
    """3.3"""
    data = loadtxt("stm.txt")
    imshow(data, origin="lower")
    maps = colormaps()
    for i in maps:
        imshow(data, origin="lower")
        xlabel(i)
        set_cmap(i)
        show()


if __name__ == "__main__":
    prompt_func(p1, p2, p3, p4, p5)
