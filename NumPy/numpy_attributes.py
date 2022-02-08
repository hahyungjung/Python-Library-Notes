numpy_attributes.py

import numpy as np

"""
Commands 

np.shape
np.ndim
np.dtype
np.itemsize
np.size

"""

# Ex 1

vector = [1,2,3,4]
print("shape:", np.array(vector, int).shape, 
      ", dimension:", np.array(vector, int).ndim,
      ", size:", np.array(vector, int).size )

matrix = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print("shape:", np.array(matrix, int).shape, 
      ", dimension:", np.array(matrix, int).ndim,
      ", size:", np.array(matrix, int).size)

tensor = [[[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
           [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
           [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
           [[1,2,5,8],[1,2,5,8],[1,2,5,8]]]
print("shape:", np.array(tensor, int).shape, 
      ", dimension:", np.array(tensor, int).ndim, 
      ", size:", np.array(tensor, int).size)


'''
Output
	shape: (4,) , dimension: 1 , size: 4
	shape: (3, 4) , dimension: 2 , size: 12
	shape: (4, 3, 4) , dimension: 3 , size: 48
'''

# Ex 2

a = np.arange(15).reshape(3, 5)
print(a)

# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

print(a.shape)
# (3, 5)
print(a.ndim)
# 2
print(a.dtype)
# int64
print(a.itemsize)
# 8
print(a.size)
# 15
print(type(a))
# <class 'numpy.ndarray'>
