import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np




iris = sns.load_dataset('iris')
print(iris.head())
print()
print(iris['species'].unique())

# GRIDS


def grids():
    sns.pairplot(iris)
    plt.show()
    sns.PairGrid(iris)
    plt.show()
    g = sns.PairGrid(iris)
    # g.map(plt.scatter)
    # plt.show()
    g.map_diag(sns.distplot)
    g.map_upper(plt.scatter)
    g.map_lower(sns.kdeplot)
    plt.show()



print()

tips = sns.load_dataset('tips')
print(tips.head())

g = sns.FacetGrid(tips, col='time', row='smoker')
g.map(sns.distplot, 'total_bill')
plt.show()














