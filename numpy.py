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

to check the dimension of the array we use ndim
Syntax: variable.ndim
'''