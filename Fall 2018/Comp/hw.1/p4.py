#!/usr/bin/python3
from pylab import *
from math import *
from numpy import *

def p4():
    """2.12: Prime Numbers"""
    print("2.12 [Prime Numbers]:")
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

if __name__ == "__main__":
    p4()
