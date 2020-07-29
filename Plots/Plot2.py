import matplotlib.pyplot as plt

ages = [1, 4, 34, 5, 6, 36, 89,65, 54, 76, 139, 9, 56, 31, 45, 74, 39]
bins = [0, 20, 40, 60, 80, 200]

plt.hist(ages, bins, histtype = 'bar', rwidth = 0.5)

plt.xlabel("ages")
plt.ylabel("number")
# plt.legend()
plt.show()