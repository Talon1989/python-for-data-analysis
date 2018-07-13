import numpy as np
import pandas as pd



def missingData():
    d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
    df = pd.DataFrame(d)
    print( df )
    # drops all the rows with at least 1 nan, use axis=1 to columns
    df.dropna(inplace=True, axis=0)
    print( df ); print()
    d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
    df = pd.DataFrame(d)
    print( df.fillna(-1) )  # fills the nan with given argument


def groupby():
    data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
            'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
            'Sales': [200, 120, 340, 124, 243, 350]}
    df = pd.DataFrame(data)
    print( df ); print()
    byComp = df.groupby('Company')
    print( byComp.mean() ); print()
    print( byComp.sum().loc['GOOG'] )  # sum of sales of GOOG
    print( df.groupby('Company').sum().loc['FB'] )  # same for FB concatenated
    # print( df[df['Sales'] > 199] )
    print()
    print( df.groupby('Company').describe() )


def mergingJoiningConcat():
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                       index=[0, 1, 2, 3])
    df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                       index=[4, 5, 6, 7])
    df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                       index=[8, 9, 10, 11])
    print(df1)
    print(df2)
    print(df3); print()
    print( pd.concat([df1, df2, df3]) )


def times2(x):
    return x*2


def operations():
    df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444]
                          , 'col3': ['abc', 'def', 'ghi', 'xyz']})
    print( df.head() )
    # df['banana'] = [33,55,66,77]
    # df.loc[len(df)] = [99,99,99,99]
    print( df['col2'].unique() )  # to have the size w/out len() use nunique()
    print( df['col2'].value_counts() )
    print( df.loc[1].loc['col2'] )
    print()
    print( df )
    print( df[ (df['col1']>2) & (df['col2']==666) ] ); print()
    # apply custom function to dataframe
    print( df['col1'].apply(lambda x: x*2) ); print()
    print( df.index )
    print( df.columns ); print()
    # sorting and ordering
    print(df)
    print( df.sort_values('col2') )  # arg is column to be sort by
    print()
    print( df.isnull() ); print()
    # pivot
    df = pd.DataFrame(
        {'A':['foo','foo','foo','bar','bar','bar'],
         'B':['one','one','two','two','one','one'],
         'C':['x','y','x','y','x','y'],
         'D':[1,3,2,5,4,1]}
    )
    print(df)
    print( df.pivot_table(values='D', index=['A','B'],
                          columns=['C']) )





operations()



