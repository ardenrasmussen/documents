import numpy as np

def rand():
    return np.random.random() ** 2

def f(x):
    return (1/(np.exp(x)+1))

def w(x):
    return np.power(x,-0.5)

def main():
    N = int(1e7)
    I = (1/N)*sum([2.0/(np.exp(rand()) + 1) for i in range(N)])
    print(I)

if __name__ == "__main__":
    main()
