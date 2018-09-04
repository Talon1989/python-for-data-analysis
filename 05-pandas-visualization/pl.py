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
print(df2); print()



# df2['a'].plot.hist(bins=len(df2['a']))
# df2.plot.area()
# df2.plot.bar()
# df2.plot.scatter(x='a', y='b')
# df2.plot.box()
# print(sum(df2['b']) / len(df2['b']))

# df = pd.DataFrame(np.random.randn(1000,2), columns=['a','b'])
# df.plot.hexbin(x='a', y='b', gridsize=25)

df2['a'].plot.kde()

plt.show()

