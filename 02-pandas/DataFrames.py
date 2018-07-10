import numpy as np
import pandas as pd


def df():
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data)
    print(pd.DataFrame(data, columns=['state','pop']))  # creates df of given columns only
    frame2 = pd.DataFrame(data, index=['one','two','three','four','five','six']
                          , columns=['year','state','pop','dept'])
    print(frame2)
    print()
    print(frame2['year'])  # == frame2.year
    print()

    print(frame2.loc['three'])
    print(frame2.iloc[:2, :2])

    frame2['dept'] = 16.5  # sets all the dept to 16.5
    frame2['dept'] = np.arange(len(frame2.index))  # sets all from 0 to 6

    print()

    print(frame2)

    val = pd.Series([-1,-2,-3], index=['two', 'four', 'five'])
    frame2['dept'] = val  # puts the values only for the indexes of the series corresponding to the df
    print(frame2)
    print()

    frame2['eastern'] = frame2.state == 'Ohio'
    print(frame2)
    del frame2['eastern']
    print(frame2)

    print(frame2.T)  # transpose the dataframe


## --------------


obj = pd.Series(range(3), index=['a', 'b', 'c'])
print(obj[:2])

print()

population = {'Nevada': {2001: 2.4, 2002: 2.9},
                'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
obj2 = pd.DataFrame(population)
print(obj2)
print('Ohio' in obj2.columns)
print('Ohio' in obj2.index)
print(obj2.loc[:, 'Nevada':])




