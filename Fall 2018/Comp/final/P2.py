import numpy as np
import pylab

def integrate(func, a, b, h=1e-2, delta=1e-6):
    """Approximates integral using adaptive method"""
    if a > b:
        val = integrate(func, b, a, h=h, delta=delta)
        return (-val[0], val[1])
    n = int(abs(b - a) / h)
    i0 = h * ((0.5 * (func(a) + func(b))) + sum(
        [func(a + k * h) for k in range(1, int((b - a) / h))]))
    epsilon = delta + 10
    while epsilon > delta:
        h /= 2
        n *= 2
        i1 = (0.5 * i0) + (h * sum([func(a + k * h) for k in range(1, n, 2)]))
        epsilon = abs(i1 - i0) / 3
        i0 = i1
    return i1

def rho(r):
    if (r[0] == 0.5 or r[0] == -0.5) and -0.5 <= r[1] <= 0.5:
        return 1
    elif (r[1] == 0.5 or r[1] == -0.5) and -0.5 <= r[0] <= 0.5:
        return 1
    return 0

def p1(x1,x2, delta=1e-6):
    r = np.array([x1,x2])
    func_a = lambda x: 1.0/(np.linalg.norm(r-np.array([x,-0.5])))
    func_b = lambda y: 1.0/(np.linalg.norm(r-np.array([-0.5,y])))
    func_c = lambda x: 1.0/(np.linalg.norm(r-np.array([x,0.5])))
    func_d = lambda y: 1.0/(np.linalg.norm(r-np.array([0.5,y])))
    int_a = integrate(func_a, -0.5, 0.5, delta=delta)
    int_b = integrate(func_b, -0.5, 0.5, delta=delta)
    int_c = integrate(func_c, -0.5, 0.5, delta=delta)
    int_d = integrate(func_d, -0.5, 0.5, delta=delta)
    return int_a + int_b + int_c + int_d

def p2():
    print("V(0,0) = {}".format(p1(0,0)))
    print("V(0.25,0) = {}".format(p1(1/4,0)))

def p3():
    def e(x1,x2,h=1e-5,delta=1e-6):
        ex = (p1(x1 + h, x2) - p1(x1-h, x2))/(2*h)
        ey = (p1(x1, x2+h) - p1(x1, x2-h))/(2*h)
        return [ex, ey]

    print("E(0,0) = {}".format(e(0,0)))
    print("E(0.25,0) = {}".format(e(0.25,0)))


def p4():
    steps = 100
    data = [[p1(x,y, 1e-3) for x in np.linspace(-1,1, steps)] for y in np.linspace(-1,1, steps)]
    pylab.imshow(data)
    pylab.colorbar()
    pylab.savefig("P2_4.png")

def main():
    p2()
    p3()
    p4()
    pass

if __name__ == "__main__":
    main()
