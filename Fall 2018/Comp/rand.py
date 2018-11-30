import random
import pylab
import math

def distro():
    points = []
    dist = []
    for i in range(10000):
        points.append(random.random())
        dist.append(-0.1*math.log(1-points[-1]))
    pylab.plot(points, '.')
    pylab.show()
    pylab.plot(dist, '.')
    pylab.show()

def gaussian():
    x = []
    y = []
    sigma = 1
    for i in range(10000):
        theta = 2*math.pi*random.random()
        r = math.sqrt(-2*sigma**2*math.log(1-random.random()))
        x.append(r*math.cos(theta))
        y.append(r*math.sin(theta))
    # pylab.plot(x, '.')
    # pylab.plot(y, '.')
    pylab.plot(x, y, 'k')
    pylab.show()


def main():
    gaussian()

if __name__ == "__main__":
    main()
