import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.linspace(0, 5, 200)
max_v = 2
min_v = -2
max_void = 0
min_void = 0
#  ax.set_xlim(-2, 2)
#  ax.set_ylim(-2, 2)
#  ax.set_zlim(-2, 2)
a_range = range(min_v ,max_v)
#  a_range = np.arange(-1, 1, 0.5)
a_void = range(min_void, max_void)
a_void = [x for x in a_void if x != 0]
#  a_range = [x for x in a_range if x not in a_void]
b_range = range(min_v, max_v)
b_void = range(min_void, max_void)
b_void = [x for x in b_void if x != 0]
#  b_range = [x for x in a_range if x not in a_void]
c_range = range(min_v, max_v)
c_void = range(min_void, max_void)
c_void = [x for x in c_void if x != 0]
#  c_range = [x for x in a_range if x not in a_void]
for a in a_range:
    for b in b_range:
        for c in c_range:
            print("({},{},{})".format(a, b, c))
            x = a * np.exp(4 * t)
            y = (b / 2 + c / 2) * np.exp(-t) + (b / 2 - c / 2) * np.exp(-3 * t)
            z = (b / 2 + c / 2) * np.exp(-t) - (b / 2 - c / 2) * np.exp(-3 * t)
            u = 4*x
            v = -2*x+z
            w = y - 2*z
            x_new = []
            y_new = []
            z_new = []
            u_new = []
            v_new = []
            w_new = []
            for i in range(0, len(x)):
                if x[i] <= max_v and y[i] <= max_v and z[i] <= max_v:
                    if x[i] >= min_v and y[i] >= min_v and z[i] >= min_v:
                        x_new.append(x[i])
                        y_new.append(y[i])
                        z_new.append(z[i])
                        u_new.append(u[i])
                        v_new.append(v[i])
                        w_new.append(w[i])
            #  ax.plot(x_new, y_new, z_new)
            ax.quiver(x, y, z, u, v, w)
            #  ax.plot(x, y, z)
            #  ax.quiver(x_new, y_new, z_new, u_new, v_new, w_new)
#  ax.legend()
plt.show()
#  plt.savefig("ppi1.svg")
