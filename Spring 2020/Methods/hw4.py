import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

x = np.random.randint(1, 7, 1000)
y = np.random.randint(1, 7, 1000)

counts = [
    len([x for x in np.concatenate((x, y)) if x == i]) for i in range(1, 7)
]
count_sum = [len([x for x in (x + y) if x == i]) for i in range(1, 13)]
men_std = np.sqrt(counts)
men_counts_std = np.sqrt(count_sum)
width = 1.0
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3, 4, 5, 6], 6 * np.max(counts) * np.array(6 * [1/6]),
         color='red')
plt.bar(range(1,7), counts, width=width, yerr=men_std)
plt.subplot(1, 2, 2)
plt.plot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 6 * np.max(count_sum) * np.array([
    1 / 36, 2 / 36, 3 / 36, 4 / 36, 5 / 36, 6 / 36, 5 / 36, 4 / 36, 3 / 36,
    2 / 36, 1 / 36
]),
         color='red')
plt.bar(range(1, 13), count_sum, width=width, yerr=men_counts_std)
plt.savefig("hw4.png")
