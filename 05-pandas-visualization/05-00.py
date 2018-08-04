import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ser = pd.Series([0,1,2,3,5],['a','b','c','d','e'])
# print(ser)
#
# df = pd.DataFrame(np.random.randn(3,2), index=['a','b','c'], columns=['d1','d2'])
# print(df)


df1 = pd.read_csv('df1', index_col=0)
print(df1.head()); print()

df2 = pd.read_csv('df2')
print(df2.head()); print()


def histograms():
    # get histogram for all values in column A
    df1['A'].hist(bins=30)
    plt.show()
    # same
    df1['A'].plot(kind='hist', bins=30)
    plt.show()
    # same
    df1['A'].plot.hist()
    plt.show()


df2.plot.area(alpha=0.5)
plt.show()

df2.plot.bar(stacked=True)
plt.show()

# df1.plot.line(x=df1.index, y='B')
# plt.show()

# color('c') is equal to the value of column c
df1.plot.scatter(x='A', y='B', c='C')
plt.show()
# # size('s') is equals to the value of column c
# df1.plot.scatter(x='A', y='B', s=df1['C'])
# plt.show()

# boxplot
df2.plot.box()
plt.show()

df = pd.DataFrame(np.random.randn(1000,2), columns=['a', 'b'])
print(df.head())
df.plot.hexbin(x='a', y='b', gridsize=25)  # color value represent count
plt.show()

# kernel density estimation
df2['a'].plot.kde()
plt.show()
df2.plot.kde()
plt.show()




































