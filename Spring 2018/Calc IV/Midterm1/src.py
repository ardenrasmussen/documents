from math import *


def calc_a(k):
    if k == 0 or k == 1:
        return 1
    return ((k+1)*(k-4))/((k*(k-1))) * calc_a(k - 2)


def print_a(k):
    if k % 2 == 0:
        print(calc_a(k), "a_0")
    else:
        print(calc_a(k), "a_1")
