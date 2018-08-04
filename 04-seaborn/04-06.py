import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


tips = sns.load_dataset('tips')
print(
    tips.head()
)
print()

sns.set_style('ticks')
sns.countplot(data=tips, x='sex')
sns.despine(left='True')
plt.show()

plt.figure(figsize=(12,3))
sns.countplot(data=tips, x='sex')
plt.show()

sns.set_context('poster')
sns.countplot(data=tips, x='sex')
plt.show()

sns.set_context('paper')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex'
           , palette='seismic')
plt.show()






























