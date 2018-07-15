import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0,5,11)
y = x ** 2
print(x)
print(y)

# plt.plot(x, y)
# plt.xlabel('X'); plt.ylabel('Y')
# plt.title('Title')

# plt.subplot(1,2,1)  # 1 row, 2 columns, number 1
# plt.plot(x,y, 'r')
# plt.subplot(1,2,2)  # 1 row, 2 columns, number 2
# plt.plot(y,x,'b')


# OO APPROACH

fig = plt.figure()
print(type(fig))
axes = fig.add_axes([0.1,0.1,0.8,0.8])  # left, bottom, width, height
axes.plot(x,y)
axes.set_xlabel('X'); axes.set_ylabel('Y')
axes.set_title('Obj Oriented Approach')
plt.show()

fig = plt.figure()
axes1 = fig.add_axes([.1,.1,.8,.8])
# 20%inFrom left, 50%upFrom bottom , takes 40% of canvas in with, tales 30% of canvas in height
axes2 = fig.add_axes([.2,.5,.4,.3])
axes2.set_title('small')
# axes3 = fig.add_axes([.5,.1,.4,.3])
axes1.plot(x,y)
axes2.plot(y,x)
plt.show()





