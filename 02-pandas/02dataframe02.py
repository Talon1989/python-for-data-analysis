import numpy as np
import pandas as pd



# conditionals
np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,3), ['A','B','C','D','E'], ['X','Y','Z'])
print(df)
print(df < 0)
print(df[df < 0])
# df[df < 0] = 'less 0'
print()
print(df)
print(df['X'] < 0)
print(df.loc['A'] < 0); print()
print(df[df['X'] > 0])  # returns all the rows where column X has no - values
print()
print(df)
print( df[ df['Z']<0 ] ['X'] )  # get column X of df where Z is less than 0
print( df[ df['Z']<0 ] [[ 'X', 'Y' ]] )  # same as above but columns X and Y
print()

# and or conditionals
print(df)
# try:
#     print(df[(df['X'] > 0) and (df['Y'] > 0)])
# except ValueError:
#     print('from ValueError')
#     print(df[(df['X'] > 0) & (df['Y'] > 0)])
print( df[ (df['X']>0 ) & (df['Y']>0) ] )  # if use 'and' it will throw an error
print( df[ (df['X']<0.80) | (df['Z']<0.9) ] )  # same for or use '|'

# reset index
# resets index to default range(0, len(rows)-1)  ;  prev index becomes a col
df.reset_index(inplace=True)
print(df)
df['States'] = 'CA NY WY OR CO'.split(' ')
print( df )
df.drop('index', axis=1, inplace=True)
df.set_index('States', inplace=True)
print( df )





