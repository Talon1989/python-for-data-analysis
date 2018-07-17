import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,5,11)
y = x ** 2

# plt.interactive(True)  # removes requirement for plt.show
# SUBPLOTS

fig, axes = plt.subplots(nrows=1, ncols=2)  # does fig.add_axes automatically based on how many rows, cols
# plt.show()

for ax in axes:
    ax.plot(x, y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

axes[0].set_title('First Plot')
axes[1].set_title('Second Plot')
plt.tight_layout()  # takes care of overlapping figures

# plt.show()


# FIGURE SIZE AND DPI
# fig = plt.figure(figsize=(8,2))
# ax = fig.add_axes([0.1,0.1,1,1])
# ax.plot(x,y)
# # plt.tight_layout()
# fig.show()

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
plt.show()



# SAVE FIGURE
# fig.savefig('my_picture.png', dpi=200)



# --------------------

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,.9,.9])
ax.plot(x, x**2, 'r--', label='squared')
ax.plot(x, x**3, 'b--', label='cubed')
ax.legend(loc='best')

ax.set_title('Title')
ax.set_ylabel('Y')
ax.set_xlabel('X')
fig.show()














