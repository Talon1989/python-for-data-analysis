import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ser = pd.Series([0,1,2,3,5],['a','b','c','d','e'])
# print(ser)
#
# df = pd.DataFrame(np.random.randn(3,2), index=['a','b','c'], columns=['d1','d2'])
# print(df)


df1 = pd.read_csv('df3')
print(df1.head()); print()

# print(df2.loc[2:3,'b':'c'])

plt.style.use('ggplot')

# df1['a'].hist(bins=30)
# plt.show()

# SCATTER-PLOT B VS A
df1.plot.scatter(x='b', y='a', c='red', figsize=(6,3))
plt.show()

df1.ix[:8].plot.area()
plt.show()

# HISTOGRAM OF 'a' COLUMN
df1['a'].plot.hist(bins=20, color='green', alpha=0.3)
plt.show()

# BOXPLOT COMPARING 'a' AND 'b' COLUMNS
df1[['a', 'b']].plot.box()
plt.show()

# KDE PLOT OF 'a' COLUMN
df1['a'].plot.kde(lw=5, ls='--')
plt.show()






























































