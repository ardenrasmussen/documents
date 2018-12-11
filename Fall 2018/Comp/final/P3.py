import numpy as np
import pylab

a = 1

def rho(r):
    if (r[0] == 0.5 or r[0] == -0.5) and -0.5 <= r[1] <= 0.5:
        return 1
    elif (r[1] == 0.5 or r[1] == -0.5) and -0.5 <= r[0] <= 0.5:
        return 1
    return 0

def gauss_seidel(phi, rho, w, tol):
    error = tol + 1000
    N = phi.shape[0]
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
                        phi[i, j - 1]) - w * phi[i, j] + (a**2 / 4) * rho([i, j])
                    diff_max = max(diff_max, np.abs(phi[i,j] - old))
        error = diff_max
    return phi

def main():
    phi = np.zeros([200, 200])
    for i in range(50,150):
        phi[50,i] = 1
        phi[150,i] = 1
        phi[i,50] = 1
        phi[i,150] = 1
    phi = gauss_seidel(phi, rho, 0.8, 1e-4)

    print("V(0,0) = {}".format(phi[100, 100]))
    print("V(0.25,0) = {}".format(phi[125,100]))

    pylab.imshow(phi)
    pylab.colorbar()
    pylab.savefig("P3_3.png")

    def e(x1,x2, h = 2/200):
        ex = (phi[x1+1, x2] - phi[x1-1,x2])/(2*h)
        ey = (phi[x1, x2+1] - phi[x1,x2-1])/(2*h)
        return [ex, ey]
    print("E(0,0) = {}".format(e(100,100)))
    print("E(0.25,0) = {}".format(e(125,100)))

if __name__ == "__main__":
    main()
