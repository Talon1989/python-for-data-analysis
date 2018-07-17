import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,5,11)
y = x ** 2



fig = plt.figure()
ax = fig.add_axes([0.1,0.1,.9,.9])
# alpha controls transparency, marker marks the points in the array
ax.plot(x, y, color='purple', linewidth=5, alpha=1/4
        , linestyle='--', marker='o', markersize=10)
ax.plot(y, x, color='black', marker='*', markersize=10
        , markerfacecolor='yellow', markeredgewidth=2)
ax2 = fig.add_axes([.2,.5,.4,.3])
ax2.set_xlim([0,1])
ax2.set_ylim([0,2])
ax2.plot(x,y)
fig.show()

































