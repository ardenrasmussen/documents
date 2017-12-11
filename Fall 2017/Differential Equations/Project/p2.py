import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.add_subplot(111)
t = np.linspace(0, 1, 100)
#  t = np.arange(0.0, 2.0, 0.01)
s = np.exp(-6*t)
print(t, s)
ax.plot(t, s)
ax.set(xlabel="t", ylabel="S(t)")
plt.hlines(0, 0, 1, linestyles="dashed", color="lightgrey")
#  min_v = -2
#  max_v = 2
#  for a in range(min_v, max_v):
    #  for b in range(min_v, max_v):
        #  for c in range(min_v, max_v):
            #  print("({},{},{})".format(a,b,c))
            #  x = a*np.exp(-2*t)
            #  y = (b/2 + c/2)*np.exp(-t)+(b/2-c/2)*np.exp(-3*t)
            #  z = (b/2+c/2)*np.exp(-t)-(b/2-c/2)*np.exp(-3*t)
            #  u = -2*x
            #  v = -2*y+z
            #  w = y-2*z
            #  ax.plot(x, y, z)
            #  ax.quiver(x, y, z, u, v, w, length=0, headlength=10)
#  ax.legend()
#  plt.show()
#  plt.show()
plt.savefig("p2.svg")
