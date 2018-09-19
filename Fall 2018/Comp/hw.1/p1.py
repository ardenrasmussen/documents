#!/usr/bin/python3
from pylab import *
from math import *
from numpy import *

def p1():
    """Fibonacci Sequence: Prints all the sequence from 1 to Max"""
    print("Fibonacci Sequence:")
    vmaximum = int(input('Max: '))
    fibs = [1, 1]
    while fibs[-1] < vmaximum:
        fibs.append(fibs[-1] + fibs[-2])
    if fibs[-1] > vmaximum:
        fibs.pop()
    print(*fibs)

if __name__ == "__main__":
    p1()
