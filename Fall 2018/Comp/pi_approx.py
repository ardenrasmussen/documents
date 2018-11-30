import numpy as np

def func(pt):
    return 1 if sum(x**2 for x in pt)<=1 else 0

def monte(dim, N=1000):
    return 2**dim*sum([func(np.random.uniform(-1,1, dim)) for i in range(int(N))])/N

def main():
    for i in range(10):
        print(i, monte(i, 1e6))

if __name__ == "__main__":
    main()
