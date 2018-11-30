import numpy as np
import pylab

def monte_carlo(func, a, b, N=1000):
    k = 0
    for i in range(int(N)):
        x,y = np.random.uniform(a, b), np.random.uniform(0,1)
        if y < func(x):
            k += 1
    return (b-a)*(k/N)

def mean_value(func, a, b, N=1000):
    return (b-a)*sum([func(np.random.uniform(a, b)) for i in range(int(N))])/N

def simpson(func, a, b, n=100):
    """Approximates integral using simpson method"""
    h = (b-a)/n
    return (h / 3.0) * (
        func(a) + func(b) +
        (4.0 * sum([func(a + (k * h)) for k in range(1, n, 2)])) +
        (2.0 * sum([func(a + (k * h)) for k in range(2, n - 1, 2)])))

def f(x):
    return np.sin(1/(x*(2-x)))**2

def g(x):
    return np.power(x, -0.5)/(np.exp(x) + 1)

def main():
    pylab.plot([g(x) for x in np.linspace(0, 1, 10000)])
    pylab.show()
    # print("Simpson:", simpson(f, 1e-10, 2-1e-10, 1000))
    # print("Monte Carlo:", monte_carlo(f, 0, 2, 1e6))
    # print("Mean Value:", mean_value(f, 0, 2, 1e6))


    # print("Mean Value:", monte_carlo(g, 0, 1, 1e6))

if __name__ == "__main__":
    main()
