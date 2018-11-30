import pylab

seed = 1
a = 1664525
c = 1013904223
m = 4294967296

def main():
    values = [seed]
    x = seed
    for i in range(100):
        x = (a*x+c) % m
        values.append(x)
    pylab.plot(values, 'k.')
    pylab.show()


if __name__ == "__main__":
    main()
