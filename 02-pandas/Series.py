import numpy as np
import pandas as pd



# def yielder():
#     for i in range(10):
#         yield i

# for asd in yielder():
#     print(asd)



obj = pd.Series([4,7,-5,3])
print(obj)
for n in obj.index:  # same as in range(len(obj)), also works with obj.data
    print(n)
obj2 = pd.Series(data=[4,7,-5,3], index=['a','b','c','d'])
print(obj2)
obj2[ obj2 > 0 ]
print(np.exp(obj2))

# can also create data from dictionaries
dic = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(dic)
print(obj3)
obj4 = pd.Series(dic, index=['California', 'Ohio', 'Oregon', 'Texas'])
print(obj4)
print( obj4.isnull() )  # == pd.isnull(obj4)
print( obj3 + obj4 )
obj2.index = ['z','x','y','k']  # changed the original index to new
print(obj2)






