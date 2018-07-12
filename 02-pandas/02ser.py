import numpy as np
import pandas as pd




labels = ['a', 'b', 'c']
arr = np.array([10, 20, 30])
d = {'x':2.5, 'y':3, 'z':5.6}

ser1 = pd.Series(arr)  # created with list (np.array() in this case)
print(ser1); print()
ser1 = pd.Series(data=arr, index=labels)  # created with data and index
print(ser1); print()
ser1 = pd.Series(d)  # created with dictionary as argument
print(ser1); print()
print(pd.Series([1, 'b', sum, True]))  # a series can hold any type of data obj
print()
# indexing
ser1 = pd.Series([41,39,41,41], ['usa', 'ger', 'ussr', 'jap'])
print(ser1)
print(ser1.loc['ger':'ussr'])  # the last argument in pandas is inclusive unlike np
ser2 = pd.Series([1,2,3,4], ['usa', 'italy', 'ussr', 'jap'])
print( ser1 + ser2 )





