import numpy as np



np.array([1, 2, 3])
my_mat = [[1,2,3], [4,5,6], [7,8,9]]
print(my_mat) ; print()
np.arange(10, 20, 2)  # from 10 to 19 with increments of 2
print( np.arange(20).reshape(5,4) ) ; print()
print( np.zeros((2,3)) ) ; print()
np.ones((5,3))  # similar to np.zeroes by for ones
print( np.linspace(0, 5, 10) ) ; print()  # 10 evenly spaced points from 0 to 5
print( np.identity(4) ) ; print()  # identity matrix 4 by 4

print( np.random.rand(5) ) ; print()  # 5 rand numbers from uniform distribution
print( np.random.randn(5) ) ; print()  # 5 rand numbers from normal distribution
nums = np.random.randint(5, 100, 3)  # 3 rand numbers between 5 and 99
print( nums.argmax() )  # returns position of max number in the array
print( nums.dtype )  # returns data-type of the array
print()


def indexing1d():
    arr = np.arange(0,10)
    print(arr[2:4])
    print(arr[:2])
    print(arr[7:])
    print(arr[-1:])
    print(arr * 2)
    # np.copy(arr[:5])
    fives = arr[:5].copy()  # if not copy changing part will change main one
    print(fives)
    fives[:2] = 100  # broadcasting
    print(fives)
    print(arr)


def indexing2d():
    arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
    print( arr_2d )
    print( arr_2d[0,2] )  # == arr_2d[0][2]
    print( arr_2d[-2:, -2:] )  # bottom right values
    arr_2d = np.arange(1, 11)
    evens = arr_2d % 2 == 0
    print( evens )
    print( arr_2d[evens] )
    arr_2d = np.arange(50).reshape(5,10)
    print( arr_2d )
    print( arr_2d[1:3, 3:5] )


def operations():
    arr = np.arange(20)
    print( arr*2 )
    print( np.sqrt(arr) )




operations()


