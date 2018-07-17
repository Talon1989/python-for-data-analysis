import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,100)
y = x*2
z = x**2


# fig = plt.figure()
# ax = fig.add_axes([0.1,.1,.9,.9])
# ax.plot(x,y)
# ax.set_title('title')
# ax.set_ylabel('y')
# ax.set_xlabel('x')
# fig.show()


# fig = plt.figure()
# ax1 = fig.add_axes([0,0,1,1])
# ax2 = fig.add_axes([.2,.5,.2,.2])
# ax1.plot(x,y)
# ax2.plot(x,y)
# fig.show()

# fig, axes = plt.subplots(nrows=2, ncols=1)
# axes[0].plot(y, color='blue', lw=4)
# axes[0].set_ylabel('Y')
# axes[0].set_xlabel('X')
# axes[1].plot(z, color='red', linestyle='--')
# axes[1].set_ylabel('Z')
# axes[1].set_xlabel('X')
# fig.show()


# fig = plt.figure()
# ax1 = fig.add_axes([0,0,1,1])
# ax1.plot(z)
# ax1.set_xlabel('X')
# ax1.set_ylabel('Z')
# ax2 = fig.add_axes([.2,.5,.4,.4])
# ax2.plot(y)
# ax2.set_xlabel('X')
# ax2.set_ylabel('Y')
# ax2.set_title('zoom')
# ax2.set_xlim([20,22])
# ax2.set_ylim([30,50])
# fig.show()


def linespacer(start, end, pieces):
    increment = (end-start) / pieces
    counter = start
    while counter < end:
        print(counter)
        counter += increment


linespacer(5, 15, 10)




