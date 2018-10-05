from numpy import arange
from pylab import *

def p3():

    def deriv(f, x, h=0.1):
        return (f(x + h) - f(x)) / h

    data = loadtxt('data1.txt')
    T_plot = data[0]
    E3 = data[5]
    C = [(E3[x + 1] - E3[x]) / 0.1 for x in range(len(T_plot) - 1)]
    m = len(T_plot) - 1
    C.append((E3[m] - E3[m - 1]) / 0.1)
    i, C_max = max(enumerate(C), key=lambda x: x[1])
    print(T_plot[i], C_max, i)
    plot(T_plot, C)
    show()

if __name__ == "__main__":
    p3()
