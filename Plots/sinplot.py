import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

plt.plot(x, np.tan(x))
plt.ylim(-10, 10)

plt.plot([-7, 7], [0, 0])

plt.show()