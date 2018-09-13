from pylab import *
import scipy
# from scipy import *
from numpy import *

def integrate(func, a, b, h):
    return h * ((0.5 * (func(a) + func(b))) +
            sum([func(a+k*h) for k in range(1, int((b-a)/h))]))

a = integrate(lambda x: exp(-x**2), 1, 2, 0.00001)
# b = scipy.integrate.quad(lambda x: exp(-x**2), 1, 2)
# b = scipy.integrate(lambda x: exp(-(x**2)), 1, 2)
print(a)
# print(b)
