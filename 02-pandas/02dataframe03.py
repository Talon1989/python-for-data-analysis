import numpy as np
import pandas as pd

# muti index

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = pd.MultiIndex.from_tuples(
    list(zip(outside, inside))
)
print( hier_index ); print()

df = pd.DataFrame(np.random.randn(6,2), hier_index, columns=['A','B'])
print( df ); print()

print(df.loc['G1'].loc[2]); print()

df.index.names = ['Groups', 'Num']
print( df ); print()

print( df.loc['G1'].loc[3].loc['A'] ); print()

# cross section: can call an internal index
# by giving its name and specifying the internal level
print( df.xs('G1') )
print( df.xs(2, level=1) )  # ==
print( df.xs(2, level='Num') )



