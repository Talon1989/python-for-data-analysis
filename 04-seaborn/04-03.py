import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np




tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(
    flights.head()
)
print(); print()

# print(tips.count()['tip'])



# MATRIX PLOTS

# creates a matrix via correlation data
tp = tips.corr()
print(
    tp
)
print()

sns.heatmap(tp, annot=True)
plt.show()

# creates a matrix from the dataset with given axis and values
flights_matrix = flights.pivot_table(index='month'
                    , columns='year', values='passengers')
print(flights_matrix)
print()
sns.heatmap(flights_matrix, cmap='coolwarm', linecolor='black'
            , linewidths=1)
plt.show()

# hierarchical clustermap, standard_scale normalizes the scale 0 tot 1
sns.clustermap(flights_matrix, cmap='coolwarm'
               , standard_scale=1)
plt.show()






