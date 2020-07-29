import matplotlib.pyplot as plt
from math import *


def g(l):
	x = []
	i = 0.0
	while i < l:
		x.append(i)
		x.insert(0, -i)
		i += 0.1
	return x


def f(i):
	c = []
	for x in i:
		y = x**2
		c.append(y)
	return c


x2 = [-10, 10]
y2 = [10, 10]

x = [-10, 10]#g(10)
y = [20, 20]#f(x)

plt.xlabel("This is X")
plt.ylabel("This is Y")

plt.title("Mr Graph\nand\nMrs Graph")

plt.plot(x, y, label = "Mr Graph")
plt.plot(x2, y2, label = "Mrs Graph")
plt.legend()
plt.show()