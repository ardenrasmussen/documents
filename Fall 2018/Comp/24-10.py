import numpy as np
import pylab
from multiprocessing import Pool, cpu_count


def f(x, t):
    return -x**3 + np.sin(t)


def RungeKutta(func, init, a, b, h=0.1):
    # h = abs(b - a) / N
    X = []
    T = np.arange(a, b, h)
    x = init
    for t in T:
        X.append(x)
        k1 = h * func(x, t)
        k2 = h * func(x + k1 / 2, t + h / 2)
        k3 = h * func(x + k2 / 2, t + h / 2)
        k4 = h * func(x + k3, t + h)
        x += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return T, X


def RungeKutta2(f1, f2, x_init, y_init, a, b, h=0.1):
    X = []
    Y = []
    T = np.arange(a, b, h)
    x = x_init
    y = y_init
    for t in T:
        # TODO REmove THis!
        if(x > np.pi):
            x -= 2 * np.pi
        if(x < -np.pi):
            x += 2 * np.pi
        if (2*t/3) % (2*np.pi) <= h and t > 100:
            X.append(x)
            Y.append(y)
        k1 = h * f1(x, y, t)
        l1 = h * f2(x, y, t)
        k2 = h * f1(x + k1 / 2, y + l1 / 2, t + h / 2)
        l2 = h * f2(x + k1 / 2, y + l1 / 2, t + h / 2)
        k3 = h * f1(x + k2 / 2, y + l2 / 2, t + h / 2)
        l3 = h * f2(x + k2 / 2, y + l2 / 2, t + h / 2)
        k4 = h * f1(x + k3, y + l3, t + h)
        l4 = h * f2(x + k3, y + l3, t + h)
        x += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y += (1 / 6) * (l1 + 2 * l2 + 2 * l3 + l4)
    return T, X, Y

def helper(fD):
    g = 9.8
    l = 9.8
    q = 0.5
    t_max = 200
    OmegaD=2/3
    f1 = lambda theta,omega,t: omega
    f2 = lambda theta,omega,t: -(g/l)*np.sin(theta)-q*omega+fD*np.sin(OmegaD*t)
    T, Theta, Omega = RungeKutta2(f1, f2, 0.2, 0, 0, t_max, 0.001)
    return [(fD, x) for x in Theta]


def main():
    print(cpu_count())
    # pylab.subplots_adjust(left=0.25, bottom=0.25)
    # sq = pylab.Slider(axx, 'q', 0.1, 10.0, valinit=0.5)
    FD = np.linspace(0.0, 1.6, 100)
    pool = Pool(4)
    pts  = pool.map(helper, FD)
    pts = [j for i in pts for j in i]
    # print(pts[0])
    # for fD in FD:
    #     T, Theta, Omega = RungeKutta2(f1, f2, 0.2, 0, 0, t_max, 0.001)
    #     PT += [(fD, x) for x in Theta]
    pylab.plot(*zip(*pts), 'ko')
    # pylab.plot(Theta, Omega, '.')

    # fD=1.44
    # T1, Theta1, Omega1 = RungeKutta2(f1, f2, 0.2, 0, 0, t_max, 0.01)
    # fD=1.465
    # T2, Theta2, Omega2 = RungeKutta2(f1, f2, 0.2, 0, 0, t_max, 0.01)
    # Theta2 = [Theta[i] if OmegaD*T[i] % 2*np.pi <= 10e-8 for i in range(len(T))]
    # Omega2 = [Omega[i] if OmegaD*T[i] % 2*np.pi <= 10e-8 for i in range(len(T))]
    # T1, Theta1, Omega1 = RungeKutta2(f1, f2, 0.2+1e-6, 0, 0, t_max)
    # diff = [np.log(np.fabs(Theta[i] - Theta1[i])) for i in range(len(T))]
    # pylab.plot(T, diff)
    # pylab.plot(T, [])
    # pylab.plot(T, Theta)
    # pylab.plot(T1, Theta1)
    # pylab.plot(T2, Theta2)
    # pylab.plot(T1, Theta1)
    # plot, = pylab.plot(Theta, Omega, '.')
    # plot, = pylab.plot(Theta1, Omega1)
    # axl = pylab.axes([0.25, 0.1, 0.65, 0.03])
    # axq = pylab.axes([0.25, 0.15, 0.65, 0.03])
    # axt = pylab.axes([0.25, 0.1,0.65, 0.03 ])
    # axod = pylab.axes([0.25, 0.25,0.65, 0.03 ])
    # axtmax = pylab.axes([0.25, 0.3, 0.65, 0.03])
    # sl = pylab.Slider(axl, 'l', 0.1, 10.0, valinit=9.8)
    # sq = pylab.Slider(axq, 'q', 0.1, 10.0, valinit=9.8)
    # st = pylab.Slider(axt, 't', 0.1, 1000, valinit=50)
    # def update(val):
    #     max_t = st.val
    #     f1 = lambda theta,omega,t: omega
    #     f2 = lambda theta,omega,t: -(g/l)*np.sin(theta)-q*omega+fD*np.sin(OmegaD*t)
    #     T, Theta, Omega = RungeKutta2(f1, f2, 0.2, 0, 0, max_t)
    #     plot.set_data(T, Theta)
    #     plot.set_xlim(0, max_t)
    # st.on_changed(update)
    # sod = pylab.Slider(axod, 'Omega_D', 0.1, 10.0, valinit=0.5)
    # st = pylab.Slider(axtmax, 'T_max', 0.1, 1000, valinit=20)

    pylab.show()
    # pylab.plot(T, Omega)
    # pylab.axes().set_aspect('equal')
    # pylab.plot(Omega, Theta)
    # pylab.show()
    # X, Y = RungeKutta(f, 0, 0, 10)
    # EX, EY = Euler(f, 0, 0, 10)
    # pylab.plot(X, Y)
    # pylab.plot(EX, EY)
    # pylab.show()


if __name__ == "__main__":
    main()
