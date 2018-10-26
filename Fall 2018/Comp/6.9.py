"""
Problem 6.9
"""

from numpy import pi, sin, array, sqrt, linspace
from numpy.linalg import eigh
from pylab import *

L = 5e-10
a = 1.60218e-18
# a = 0
hb = 1.054571800e-34
mass = 9.1094e-31
PSI = None

def simpson(func, a, b, n=100):
    """Approximates integral using simpson method"""
    h = abs(b-a)/n
    return (h / 3.0) * (
        func(a) + func(b) +
        (4.0 * sum([func(a + (k * h)) for k in range(1, n, 2)])) +
        (2.0 * sum([func(a + (k * h)) for k in range(2, n - 1, 2)])))

def H(n,m,v):
    pre_1 = ((hb**2)*(n**2)*(pi**2))/(mass*(L**3))
    pre_2 = 2/L
    int_1 = simpson(lambda x: sin(m*pi*x/L)*sin(n*pi*x/L), 0, L)
    int_2 = simpson(lambda x: v(x)*sin(m*pi*x/L)*sin(n*pi*x/L), 0, L)
    # int_2 = simpson(lambda x: v(x)*sin(m*pi*x/L)*sin(n*pi*x/L), 0, L)
    return pre_1*int_1 + pre_2*int_2
    # int_2

def phi(n, x):
    return sqrt(2/L)*sin(n*pi*x/L)

def psi(p, A):
    return lambda x: sum(A[n]*phi(n,x) for n in range(len(A)))

def B(F_Psi, f_psi):
    return simpson(lambda x: F_Psi(x) * f_psi(x), 0, L)

# def Psi(E,V):
#     return sum([B[n]*exp(-j*E[n]*t/hb
#     )])

def animate(t):
    plot(linspace(0, L), [abs(PSI(x,t))**2 for x in linspace(0,L)])

def main():
    V = lambda x:a*x/L
    print(H(1, 1,V))
    print(H(2, 2,V))
    print(H(3, 3,V))
    arr = array([[H(x, y, V) for x in range(0, 11)] for y in range(0, 11)])
    E, V = eigh(arr)
    print(arr)
    E /= 1.6022e-19
    psis = [psi(p, V[p]) for p in range(len(E))]
    init = lambda x: -1.6e19*abs(x-L/2)+4e9
    global PSI
    PSI = lambda x, t: sum([B(init, psi(n, V[n]))*exp(-1j*E[n]*t/hb)*psi(n,V[n])(x) for n in range(len(E))])
    vals = [PSI(x, 0) for x in linspace(0, L)]
    plot(linspace(0, L), vals)
    show()
    # animation.FuncAnimation(animate, )
    # for i, t in enumerate(arange(0, 0.1, 0.001)):
        # print("{}.png".format(i))
        # plot(linspace(0, L), [abs(PSI(x,t))**2 for x in linspace(0,L)])
        # savefig('animate/{}.png'.format(i))
    # show()
        # clf()
    # print(vals)
    # for f in psis:
        # plot(linspace(0, L), [f(x) for x in linspace(0,L)])
    # show()
    # print(simpson(lambda x: x, 0, 1))
    # for E in E:

    print(E)
    # print(V)


if __name__ == "__main__":
    main()
