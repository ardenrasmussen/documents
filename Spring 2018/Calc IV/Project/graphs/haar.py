import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save

from label_lines import *

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

def plot(func, min=-math.pi, max=math.pi, color=None, label=None):
    x = np.linspace(min, max, (max - min) * 50)
    plt.plot(x, [func(_) for _ in x], color=color, label=label)


def haar(x):
    if x <= 0:
        return 0
    elif x <= 0.5:
        return 1
    elif x <= 1:
        return -1
    return 0


def func(j, k):
    def wavelet(x):
        return pow(2, j / 2) * haar(pow(2, j) * x - k)

    return wavelet


def wavelet(x):
    return sum([
        sum([
            -(1 / 3) * pow(2, -5 * j / 2) * ((3 * k / 2) + (3 / 4)) *
            (pow(2, j / 2) * haar(pow(2, j) * x - k)) for k in range(-10, 10)
        ]) for j in range(-10, 10)
    ]) + 349525.3333333


def fouier(x):
    return sum(
        [pow(-1, n) * 4 / pow(n, 2) * math.cos(n * x)
         for n in range(1, 10)]) + (10 / 3)


def x2(x):
    return pow(x, 2)


# plot(x2, -5, 5, color='black', label=r'$x^2$')
# plot(wavelet, -5, 5, label=r'$Haar$')
# plot(fouier, -5, 5, label=r'$Fourier$')

# plot(func(0, -2), label=r'$\Psi_{0,-2}$')
# plot(func(0, -1), label=r'$\Psi_{0,-1}$')
# plot(func(0, 0), label=r'$\Psi_{0,0}$')

# plot(func(0, 0), label=r'$\Psi_{0,0}$')
# plot(func(2, 0), label=r'$\Psi_{2,0}$')

# plot(func(0, 1), label=r'$\Psi_{0,1}$')
# plot(func(2, 1), label=r'$\Psi_{2,1}$')

# plot(func(0, -1), label=r'$\Psi_{0,-1}$')
# plot(func(2, -1), label=r'$\Psi_{2,-1}$')

plot(func(0, -2), label=r'$\Psi_{0,-2}$')
plot(func(2, -2), label=r'$\Psi_{2,-2}$')

# plot(func(0, 0), label=r'$\Psi_{0,0}$')
# plot(func(0, 2), label=r'$\Psi_{0,2}$')

plt.legend()
# labelLines(plt.gca().get_lines())
tikz_save('proof_1_2_b.tex')
plt.show()
