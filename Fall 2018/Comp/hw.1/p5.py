#!/usr/bin/python3
from pylab import *
from math import *
from numpy import *

def p5():
    """3.3"""
    print("3.3:")
    data = loadtxt("stm.txt")
    imshow(data, origin="lower")
    set_cmap('Greens_r')
    show()
    imshow(data, origin="lower")
    set_cmap('flag')
    show()
    maps = colormaps()
    # for i in maps:
    #     imshow(data, origin="lower")
    #     xlabel(i)
    #     set_cmap(i)
    #     show()

if __name__ == "__main__":
    p5()
