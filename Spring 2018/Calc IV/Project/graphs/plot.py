import numpy as np
import matplotlib.pyplot as plt

def psi(x):
    if x <= 0:
        return 0
    elif x <= 0.5:
        return 1
    elif x <= 1:
        return -1
    else:
        return 0

def plot(j, k):
    x = np.linspace(-2, 2, 200)
    plt.plot(x, [pow(2, j / 2)*psi((pow(2, j)*_)-k) for _ in x])


def iterate_j(begin, end, k):
    for j in range(begin, end):
        plot(j, k)

def iterate_k(begin, end, begin_j, end_j):
    for k in range(begin, end):
        iterate_j(begin_j, end_j, k)

iterate_k(0, 1, -5, 5)
plt.grid()
plt.show()
