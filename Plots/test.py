import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import numpy as np

LIMITS = -10, 10

plt.axis([*LIMITS] * 2)  # границы для X и Y одинаковы
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ticks = np.linspace(*LIMITS, len(ax.xaxis.get_ticklabels()))
# array([-10. ,  -7.5,  -5. ,  -2.5,   0. ,   2.5,   5. ,   7.5,  10. ])

ticks = ticks[ticks != 0]

ff = FixedLocator(ticks)

ax.xaxis.set_major_locator(ff)
ax.yaxis.set_major_locator(ff)

plt.show()