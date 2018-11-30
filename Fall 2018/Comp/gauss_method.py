#!/usr/bin/python3

import numpy as np
import pylab
import time

a = 1


def gaussidal_method(phi, rho, w, tol):
    start = time.time()
    error = tol + 1000
    N = phi.shape[0]
    # phi_new = np.zeros([N, N], float)
    phi_min = 0
    while error > tol:
        diff_max = 0
        for i in range(N):
            for j in range(N):
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    phi[i, j] = phi[i, j]
                else:
                    old = phi[i,j]
                    phi[i, j] = (1 + w) / 4 * (
                        phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] +
                        phi[i, j - 1]) - w * phi[i, j] + (a**2 / 4) * rho(i, j)
                    diff_max = max(diff_max, np.abs(phi[i,j] - old))
        error = diff_max
        print(error)
    return phi, time.time() - start


def main():
    N = 100
    V = 10
    rho = lambda x, y: 1 if (20 <= x <= 40 and 60 <= y <= 80) else (-1 if (60 <= x <= 80 and 20 <= y <= 40) else 0)
    tolerance = 1e-4
    times = []
    for w in np.linspace(0.2, 1.0, 10):
        phi = np.zeros([N, N], float)
        phi, time = gaussidal_method(phi, rho, w, tolerance)
        times.append(time)
        print(time)
    print(np.linspace(0.5, 1.0, 5))
    print(times)
    # phi_new = np.zeros([N, N], float)
    # phi[0, :] = V
    # while error > tolerance:
    #     for i in range(N):
    #         for j in range(N):
    #             if i == 0 or i == N - 1 or j == 0 or j == N - 1:
    #                 phi_new[i, j] = phi[i, j]
    #             else:
    #                 phi_new[i, j] = 0.25 * (phi[i + 1, j] + phi[i - 1, j] +
    #                                         phi[i, j + 1] + phi[i, j - 1]) + (
    #                                             a**2 / 4) * rho(i, j)
    #     error = np.max(np.abs(phi - phi_new))
    #     phi, phi_new = phi_new, phi
    pylab.imshow(phi)
    pylab.show()


if __name__ == "__main__":
    main()
