import matplotlib.pyplot as plt
import seaborn as sns




tips = sns.load_dataset('tips')

print(
    tips.head()
)

# sns.distplot(tips['total_bill'], kde=False, bins=30)
# plt.show()

# combines distribution plots
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
plt.show()

# makes a joinplot for every combination of columns
# for hue use only categorical column, not numerical or continuous
sns.pairplot(tips, hue='sex', palette='coolwarm')
plt.show()

# basically an histogram that plots a single unique point for value
sns.rugplot(tips['total_bill'])
plt.show()

















