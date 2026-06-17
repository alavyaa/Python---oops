'''
Numpy
it is a package to perform mathematical operations

at the top we have to import the package using
import numpy as np 
here np is an alias so that we dont have to use numpy every time
the alias can be anything we want

to check the version
np.__version__

Example:
import numpy as np
np.__version__ 


Array
we create array in python using numpy by using an inbuilt function array()

Example:

import numpy as np
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([7, 8, 9, 10, 11, 12])
print(arr1, arr2)

3 Types of array in numpy
1. Uni-Directional 1D
2. Bi-Directional 2D
3. Multi-Dimensional 3D

1. Uni-Directional 1D
Example:
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([7, 8, 9, 10, 11, 12])
print(arr1, arr2)

2. Bi-Directional 2D
Example:
b = np.array([
    [1,2,3],
    [4,5,6]
])
print(b)

3. Multi-Dimensional 3D
Example:
c = np.array([
   [ [1,2,3],
    [4,5,6]],
   [ 
       [7,8,9],
       [10,11,12]
   ]
]
)
print(c)

ndim()
to check the dimension of the array we use ndim
Syntax: variable.ndim

dtype()
to check the type of data in the array
Syntax: variable.dtype
if the data in integer we get output int64
here 64 is the number of bits
64 bits = 8 bytes
1 byte = 8 bits

astype()
to covert type of data in array from one to other 
Syntax: variable.astype(datatype)

arange()
it accepts 3 arguments start value, ending value and the step size
Syntax: np.arange(1, 20, 2)
this is used when we want to create an array and noot type manually 
starting index should be greater than ending index while passing negative step value

linspace()
to divide the equal no. of space between two values
Syntax: np.linspace(start, end, space)
it means jahan se start hora aur jahan pe end hora un dono numbers ki range jo hai usko space jitne number me divide karo us range ko 
meaning end and start mila ke space number ki array honi chahiye

shape()
it tells the shape of the array 
it returns a tuple which contains the number of elements for 1D
while in others it return a tuple containing number of rows and columns
Syntax: variable.shape

reshape()
to convert the dimension of the array to other 
Syntax: variable.reshape(row, column, no. of elements)
row * multiplication == no. of elements present in the array only then reshape is possible otherwise no
soo if we have to change any 3D or 2D array to 1D array we use reshape(-1)
this is known as flattening of the array

ones()
np.ones(argument)
it will return an array with argument number of 1
to create 2D or 3D just increase number or arguments and put them in double paranthesis
arguments will be number of rows and number of columns

zeroes()
np.zeroes(argument)
it will return an array with argument number of 0
to create 2D or 3D just increase number or arguments and put them in double paranthesis
arguments will be number of rows and number of columns
'''