import numpy as np
import pylab

def RungeKutta(f1, f2, f3, a_init, b_init, c_init, t0, tf, h=0.1):
    A = []
    B = []
    C = []
    T = np.arange(t0, tf, h)
    a = a_init
    b = b_init
    c = c_init
    for t in T:
        A.append(a)
        B.append(b)
        C.append(c)
        k1 = h * f1(a, b, c, t)
        l1 = h * f2(a, b, c, t)
        m1 = h * f3(a, b, c, t)
        k2 = h * f1(a + k1 / 2, b + l1 / 2, c + m1 / 2, t + h / 2)
        l2 = h * f2(a + k1 / 2, b + l1 / 2, c + m1 / 2, t + h / 2)
        m2 = h * f3(a + k1 / 2, b + l1 / 2, c + m1 / 2, t + h / 2)
        k3 = h * f1(a + k2 / 2, b + l2 / 2, c + m2 / 2, t + h / 2)
        l3 = h * f2(a + k2 / 2, b + l2 / 2, c + m2 / 2, t + h / 2)
        m3 = h * f3(a + k2 / 2, b + l2 / 2, c + m2 / 2, t + h / 2)
        k4 = h * f1(a + k3, b + l3, c + m3, t + h)
        l4 = h * f2(a + k3, b + l3, c + m3, t + h)
        m4 = h * f3(a + k3, b + l3, c + m3, t + h)
        a += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        b += (l1 + 2 * l2 + 2 * l3 + l4) / 6
        c += (m1 + 2 * m2 + 2 * m3 + m4) / 6
    return T, A, B, C

def main():
    sigma = 10
    r = 28
    b = 8/3
    dx = lambda x, y, z, t: sigma*(y-x)
    dy = lambda x,y,z,t: r*x-y-x*z
    dz = lambda x,y,z,t: x*y-b*z
    T, X, Y, Z = RungeKutta(dx, dy, dz, 0, 1, 0, 0, 50, 0.0001)
    pylab.plot(T, Y)
    pylab.savefig("P1_a.png")

    pylab.clf()
    pylab.plot(X,Z)
    pylab.savefig("P1_b.png")

if __name__ == "__main__":
    main()
