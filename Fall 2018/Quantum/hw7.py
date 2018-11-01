import pylab
import numpy as np
from math import sqrt, pow

a = 1
hb = 1
m = 1
k0 = 1
tau = 2*m*a**2/hb
L = 10

def Psi(x, t):
    return 1/(sqrt(2*np.pi)*a*pow(1+t**2/tau**2, 1.2))*np.exp(-pow(x-hb*k0*t/m,2)/(2*a**2*(1+t**2/tau**2)))

pylab.plot(np.linspace(-L, L, 100), [Psi(x, 0) for x in np.linspace(-L, L, 100)])
pylab.plot(np.linspace(-L, L, 100), [Psi(x, tau) for x in np.linspace(-L, L, 100)])
pylab.plot(np.linspace(-L, L, 100), [Psi(x, 2*tau) for x in np.linspace(-L, L, 100)])
pylab.show()




