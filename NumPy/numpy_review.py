numpy_review.py


import numpy as np

# Scalars (0-D Arrays)

x = np.array(5)
x

'''
output
array(5)
'''

# numpy array from a python list
a1 = np.array([1,2,3])

# numpy array of all zeros, given specified size
a2 = np.zeros(5)

# numpy array given a range of numbers
a3 = np.arange(10) # 0 through 9
a4 = np.arange(2, 10) # 2 through 9
a5 = np.arange(2, 10, 2) # 2 through 9 with jumps of two

# random numpy array drawn from standard normal distribution
a6 = np.random.randn(5)

for i, a in enumerate([a1, a2, a3, a4, a5, a6]): 
  print("a" + str(i+1) + ': ', a)


# Vectors (1-D Arrays)

# numpy array from a python list
a1 = np.array([1,2,3])

# numpy array of all zeros, given specified size
a2 = np.zeros(5)

# numpy array given a range of numbers
a3 = np.arange(10) # 0 through 9
a4 = np.arange(2, 10) # 2 through 9
a5 = np.arange(2, 10, 2) # 2 through 9 with jumps of two

# random numpy array drawn from standard normal distribution
a6 = np.random.randn(5)

for i, a in enumerate([a1, a2, a3, a4, a5, a6]): 
  print("a" + str(i+1) + ': ', a)

'''
output
a1:  [1 2 3]
a2:  [0. 0. 0. 0. 0.]
a3:  [0 1 2 3 4 5 6 7 8 9]
a4:  [2 3 4 5 6 7 8 9]
a5:  [2 4 6 8]
a6:  [ 0.30285351 -0.05456331 -1.05314768  0.11973624  0.27164971]
'''


# Vector Operations
# Vector-Scalar

# vector-scalar (applied element-wise)
x = a1.copy()
print("x + 3 = "  , x + 3)
print("x * 3 = "  , x * 3)
print("x ** 3 = " , x ** 3)
print()

x + 3 =  [4 5 6]
x * 3 =  [3 6 9]
x ** 3 =  [ 1  8 27]

# Vector-vector (must be of same size)
y = np.ones(len(x)) 
print("given: x = ",x, ", y = ", y)
print()
print("1. Addition")
print("x + y = ", x + y)
print()
print("2. Multiplication")
print("x * y = ", x * y)
print()
print("3. Dot product, various ways: ")
print("np.dot(x, y) :", np.dot(x, y))
print("x @ y : "      , x @ y)
print("x.dot(y) : "   , x.dot(y))
print()
print("NOTE!! x * y ≠ x @ y")

'''
output
given: x =  [1 2 3] , y =  [1. 1. 1.]

1. Addition
x + y =  [2. 3. 4.]

2. Multiplication
x * y =  [1. 2. 3.]

3. Dot product, various ways: 
np.dot(x, y) : 6.0
x @ y :  6.0
x.dot(y) :  6.0

NOTE!! x * y ≠ x @ y
'''

#Other cool operations:
a = np.array([1,2,3,4,5,6,7,8])
print(a)
print("sum: ", a.sum())
print("max: ", a.max())
print("argmax: ", a.argmax())
print("min: ", a.min())
print("argmin: ", a.argmin())
print("mean: ", a.mean())
print("a > a.mean():", a > a.mean())

'''
output
[1 2 3 4 5 6 7 8]
sum:  36
max:  8
argmax:  7
min:  1
argmin:  0
mean:  4.5
a > a.mean(): [False False False False  True  True  True  True]
'''

# Matrices (2-D Arrays)

# matrix from list of lists
m1 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
  
# matrix of all zeros
m2 = np.zeros((3,4))
  
m3 = np.concatenate((m1, m2.T), axis = 0)

for i, m in enumerate([m1, m2, m3]): 
	print("m" + str(i+1) + ': ')
    print(m)

'''
output
m1: 
[[1 2 3]
 [4 5 6]
 [7 8 9]]
m2: 
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
m3: 
[[1. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
 '''

# Matrix Operations
# reshape:

m1.flatten() # flattens matrix into a 1-D vector

'''
output
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
'''

m2.reshape(2, 6) #reshape matrix into new dimensions, if possible

'''
output
array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]])
'''

# concatenate vertically
np.concatenate((m1, np.ones((3,3))), axis = 0)

'''
output
array([[1., 2., 3.],
       [4., 5., 6.],
       [7., 8., 9.],
       [1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
'''

# concatenate horizontally
np.concatenate((m1, np.ones((3,3))), axis = 1)

'''
output
array([[1., 2., 3., 1., 1., 1.],
       [4., 5., 6., 1., 1., 1.],
       [7., 8., 9., 1., 1., 1.]])
'''

# Transpose
m1.T

'''
output
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
'''

# Addition & Multiplication
# Same as with vectors

m2 + 1

'''
output
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
'''

m1 * 3

'''
output
array([[ 3,  6,  9],
       [12, 15, 18],
       [21, 24, 27]])
'''

# Matrix-vector multiplication:
# $ M = A x $

A = np.arange(1,9).reshape(4,2) # create some 4 x 2 matrix
x = np.array([2,1]) 
M = A @ x
M

'''
output
array([ 4, 10, 16, 22])
''''
