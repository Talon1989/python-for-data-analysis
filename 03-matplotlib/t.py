import matplotlib.pyplot as plt
import numpy as np
ax = plt.subplot()
x = np.linspace(0, 10, 100)
y = np.exp(x)
ax.plot(x, y)
plt.show()
input()


