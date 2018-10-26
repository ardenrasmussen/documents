from math import pow
import numpy as np
import pylab

m = 1
omega = 1
h_bar = 1

const = pow(m*omega/(np.pi*h_bar), 1/4)

def exp(x):
    return np.exp(-m*omega*(x**2)/(2*h_bar))


def psi_0(x):
    return const*exp(x)

def psi_1(x):
    return 2*m*omega*x/np.sqrt(2*m*omega*h_bar)*const*exp(x)

def psi_2(x):
    return 1/(h_bar*np.sqrt(2))*const*(2*m*omega*(x**2)*exp(x)-h_bar*exp(x))

X = np.linspace(-7, 7, 200)

pylab.plot(X, [np.fabs(psi_0(x))**2 for x in X])
pylab.plot(X, [np.fabs(psi_1(x))**2 for x in X])
pylab.plot(X, [np.fabs(psi_2(x))**2 for x in X])
# pylab.show()
pylab.savefig("TEST.png")
