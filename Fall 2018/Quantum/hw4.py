from math import *
from pylab import *
from numpy import *

hbar = 1.0545718 * 10**-34
L = 1e-10
m = 9.109 * 10**-31
T = 4 * m * L**2 / (pi * hbar)

m = 1
hbar = 1
L = 1e-10


def E(n):
    return n**2 * pi**2 * hbar**2 / (2 * m * L**2)


def A(n):
    return 8 * sqrt(15) * (-1)**((n - 1) / 2) / ((n)**3 * pi**3)


def Psi(n, x, t):
    return A(n)*cos(n*pi*x/L)*( cos(E(n)*t/hbar ) - 1j * sin(E(n)*t/hbar))


def PsiStar(n, x, t):
    return A(n)*cos(n*pi*x/L)*( cos(E(n)*t/hbar ) + 1j * sin(E(n)*t/hbar))


def modPsi(x, t):
    s1 = 0
    for i in range(1, 30, 2):
        s2 = 0
        for j in range(1, 30, 2):
            s2 += PsiStar(j, x, t)
        s1 += s2 * Psi(i, x, t)
    return s1


def expX(t):
    a = -L / 2
    b = L / 2
    N = 100
    h = (b - a) / N
    s = 0
    for i in range(1, N):
        x = a + i * h
        s += x * modPsi(x, t) * h / 2
    s += h * (a * modPsi(a, t) + b * modPsi(b, t))
    return s


def expX2(t):
    a = -L / 2
    b = L / 2
    N = 100
    h = (b - a) / N
    s = 0
    for i in range(1, N):
        x = a + i * h
        s += x**2 * modPsi(x, t) * h / 2
    s += h * (a**2 * modPsi(a, t) + b**2 * modPsi(b, t))
    return s


t = [0, T / 4, T / 2, 3 * T / 4, T]

for t1 in t:
    plot(
        linspace(-L / 2, L / 2),
        [modPsi(x, t1) for x in linspace(-L / 2, L / 2)])
    plot(
        linspace(-L / 2, L / 2, 2),
        [expX(t1) for x in linspace(-L / 2, L / 2, 2)])
# show()
ylim(0.0, 1.5)
savefig("hw4(a).png")
clf()
print("We're doing <x^2>(t) now:")
# ylim(0.0, 1.5)
plot(linspace(0, T, 100), [expX2(t) for t in linspace(0, T, 100)])
savefig("hw4(b).png")
clf()
for i, t in enumerate(linspace(0, T, 200)):
    ylim(0.0, 1.5)
    plot(linspace(0, T), [modPsi(x, t) for x in linspace(-L/2,L/2)], linewidth=2.0)
    savefig("anim/hw4(c){:03}.png".format(i))
    clf()
# show()
