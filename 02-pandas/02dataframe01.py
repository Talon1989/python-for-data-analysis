import numpy as np
import pandas as pd



np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,3), ['A','B','C','D','E'], ['X','Y','Z'])
print(df); print()  # each column is a pd.Series, each row is a pd.Series
print( type(df['X']) ); print(type(df.loc['A'])); print()


df['Y+Z'] = df['Y'] + df['Z']  # create
print(df)
# to delete columns need to specify axis=1, obviously we want to mostly delete rows / entries on default axis=0
df.drop('Y+Z', axis=1, inplace=True)  # inplace == save
print(df)
print(df.shape)


# indexing
print(df[ ['X', 'Z'] ])  # a list inside the brackets returns the given columns
print()  # last two cols of last two rows:
print( df.iloc[-2:, -2:] ); print()
print( df.loc['B':'D', :'Y'] )  # rows from B to D, of cols Y and before
print( df.loc[ ['A','E'] ] )












