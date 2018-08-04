import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print(titanic.head())
# print(titanic.info())


sns.jointplot('fare', 'age', data=titanic)
plt.show()

sns.distplot(titanic['fare'], kde=False, color='red', bins=30)
plt.show()

sns.boxplot('class', 'age', data=titanic, palette='rainbow')
plt.show()

sns.swarmplot('class', 'age', data=titanic, palette='Set2')
plt.show()

sns.countplot('sex', data=titanic)
plt.show()

titanic_matrix = titanic.corr()
sns.heatmap(titanic_matrix, cmap='coolwarm')
plt.show()

g = sns.FacetGrid(titanic, col='sex')
g.map(plt.hist, 'age')
plt.show()



























