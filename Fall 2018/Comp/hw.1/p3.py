#!/usr/bin/python3
from pylab import *
from math import *
from numpy import *

def p3():
    """2.10: the Semi-Emperical Mass Formula"""

    print("2.10 [The semi-emperical mass formula]:")
    def calc_b(A, Z):
        return (15.8 * A) - (18.3 * pow(A, 2 / 3)) - (0.714 * (
            pow(Z, 2) / pow(A, 1 / 3))) - (23.2 * (pow(A - 2 * Z, 2) / A)) + (
                (0 if A % 2 == 1 else
                 (12.0 if Z % 2 == 0 else -12.0)) / pow(A, 1 / 2))

    def a():
        print("2.10.a)")
        a = int(input("A: "))
        z = int(input("Z: "))
        print(calc_b(a, z))

    def b():
        print("2.10.b)")
        a = int(input("A: "))
        z = int(input("Z: "))
        print(calc_b(a, z) / a)

    def c():
        print("2.10.c)")
        z = int(input("Z: "))
        bn = []
        for a in range(z, 3 * z + 1):
            bn.append(calc_b(a,z) / a)
        print(z + bn.index(max(bn)), max(bn))

    def d():
        print("2.10.d)")
        zbn = []
        for z in range(1, 100):
            bn = []
            for a in range(z, 3 * z + 1):
                bn.append(calc_b(a,z)/a)
            print("{}:".format(z), z + bn.index(max(bn)), max(bn))
            zbn.append(max(bn))
        print("Max at:", 1 + zbn.index(max(zbn)), max(zbn))
    a()
    b()
    c()
    d()

if __name__ == "__main__":
    p3()
