import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(1, 7, 1000)
y = np.random.randint(1, 7, 1000)

counts = [len([x for x in np.concatenate((x, y)) if x == i]) for i in range(1,7)]
count_sum = [len([x for x in (x + y) if x == i]) for i in range(1,13)]
men_std = np.sqrt(counts)
men_std = np.sqrt(count_sum)
width = 1.0
# plt.bar(range(1,6), counts, width=width, yerr=men_std)
plt.bar(range(1,13), count_sum, width=width, yerr=men_std)
plt.show()


