import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


tips = sns.load_dataset('tips')
print(
    tips.head()
)
print()


# REGRESSION PLOTS
sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'])
plt.show()
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time')
plt.show()





























































