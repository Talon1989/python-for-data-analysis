import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np




tips = sns.load_dataset('tips')
print(
    tips.head()
)


# get histogram of sex for std total bill
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
plt.show()

# counts the occurrence of x
sns.countplot(x='sex', data=tips)
plt.show()

# distribution of total_bill per day and per smoker
sns.boxenplot(x='day', y='total_bill', data=tips, hue='smoker')
plt.show()

# same as boxenplot but with current density estimation
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
plt.show()

# scatterplot based on the category
sns.stripplot(x='day', y='total_bill', data=tips)
plt.show()

# same as stripplot but with points adjusted so don't overlap
sns.swarmplot(x='day', y='total_bill', data=tips)
plt.show()

















