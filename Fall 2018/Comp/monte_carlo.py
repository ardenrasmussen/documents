import numpy as np
import pylab
N = 16
J = 1
k = 1


def ind(x):
    return x if 0 <= x < N else 0 if x >= N else N - 1


def delta_E(A, m, n):
    return 2 * J * A[ind(m), ind(n)] * (
        A[ind(m - 1), ind(n)] + A[ind(m), ind(n - 1)] +
        A[ind(m + 1), ind(n)] + A[ind(m), ind(n + 1)])


def calc(T):
    A = np.ones([N, N])
    z = 0
    M = N**2
    E = -2*J*N**2
    abs_M = 0
    exp_M = 0
    exp_E= 0
    beta = 1 / (k * T)
    steps = int(1e5)
    for i in range(steps):
        if i > 5000 and i % (N**2) == 0:
            abs_M += np.fabs(M)
            exp_M += M**2
            exp_E += E
            z += 1
        m, n = np.random.randint(0, N, 2)
        if np.random.rand() < np.exp(-beta * delta_E(A, m, n)):
            A[m, n] *= -1
            M += (2 * A[m, n])
            E -= delta_E(A,m,n)
    abs_M /= z
    exp_M /= z
    exp_E/= z
    return abs_M, exp_M, exp_E


def main():
    data = []
    exp_E = []
    xi = []

    T_SPACE = np.linspace(0.1,4.0,50)
    for T in T_SPACE:
        M, eM, E = calc(T)
        data.append(M)
        exp_E.append(E)
        xi.append(eM-M**2)
        print("{}->{}  {}  {}".format(T, M, E, xi[-1]))
    pylab.plot(T_SPACE, data)
    pylab.show()
    pylab.plot(T_SPACE, exp_E)
    pylab.show()
    pylab.plot(T_SPACE, xi)
    pylab.show()

if __name__ == "__main__":
    main()
