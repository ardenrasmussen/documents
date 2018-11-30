import numpy as np
import random
import math
import pylab


def gaussian():
    sigma = 1
    theta = 2 * math.pi * random.random()
    r = math.sqrt(-2 * sigma**2 * math.log(1 - random.random()))
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y


def main():
    N = int(10e5)
    z = 79
    le = 1.6e-19
    E = (7.7e6) * le
    ep0 = 8.85e-12
    sig = (5.2e-11) / 100
    bs = 0
    bc = (z * le**2) / (2 * np.pi * ep0 * E)
    print(bc)
    for i in range(N):
        # x, y = gaussian()
        x, y = np.random.normal(0, sig), np.random.normal(0, sig)
        # print(x,y)
        b = (x**2 + y**2)
        # b = np.sqrt(
        #     np.power(np.random.normal(), 2.0) +
        #     np.power(np.random.normal(), 2.0))
        if b < bc:
            # print(b)
            bs += 1
    print(bs)
    # 1500


if __name__ == "__main__":
    main()
