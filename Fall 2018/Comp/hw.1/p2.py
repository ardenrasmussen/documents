#!/usr/bin/python3
from pylab import *
from math import *
from numpy import *

def p2():
    """2.9: The Madelung Constant"""
    print("2.9 [The madelung constant]:")
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

if __name__ == "__main__":
    p2()
