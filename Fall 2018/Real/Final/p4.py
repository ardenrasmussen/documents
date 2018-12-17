from math import *

sexp = [pow(3.0, n)/factorial(n) for n in range(10)]
se = [1.0/factorial(n) for n in range(10)]
print(sexp)
print(se)
print(sum(sexp))
print(pow(sum(se),3))
