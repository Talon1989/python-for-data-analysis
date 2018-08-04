import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df3 = pd.read_csv('df3')
print(df3.info()); print(df3.head())


df3.plot.scatter(x='a', y='b',s=50, figsize=(12,3), c='red')
plt.show()

plt.style.use('ggplot')
df3['a'].plot.hist(bins=20, alpha=0.5)
plt.show()

df3[['a','b']].plot.box()
plt.show()

df3['d'].plot.kde()
plt.show()

df3['d'].plot.kde(lw=5, ls='--')
plt.show()

# first 30 items, can also use .head(30)
df3.ix[0:30].plot.area()
plt.show()





























