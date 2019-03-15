#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

w0=2*np.pi
v0=0
dt=0.01
X=[5, 5]
for t in np.arange(0,2, dt):
    X.append(((1-(w0**2*dt**2)/4)/(1+(w0**2*dt**2)/4))*(2*X[-1]) - X[-2])

plt.plot(np.arange(0,2,dt), X[2:])
plt.show()
