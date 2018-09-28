from numpy import *
from numpy.linalg import solve

A = array([[4,-1,-1,-1],[-1,0,3,-1],[-1,3,0,-1],[-1,-1,-1,4]], float)
V = array([5, 5, 0,0], float)
X = solve(A,V)
print(X)
