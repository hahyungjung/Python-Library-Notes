numpy_creation.py

"""
Syntax

1D array
np.array([0.5, 1.5, 2.5]) --- ([0.5, 1.5, 2.5])
np.empty([2, 3]) 2 by 3
np.arrange(10, 30, 5) --- ([10, 15, 20, 25])

2D array
np.array([[0, 1, 2], [3, 4, 5]])
np.zeros((3, 4)) 3 by 4
np.linspace(0, 4, 5) --- ([0, 1, 2, 3, 4, 5])

3D array
np.ones((2, 3, 4))

"""


import numpy as np


a = np.array([2,3,4]) # numpy.ndarray

# a = [2, 3, 4] list 
# np.array(a, dtype = int) -- numpy.ndarray
# dtype -- If not given, then the type will be determined as the minimum type required to hold the objects in the sequence.


print(a)
# [2 3 4]

print(a.dtype)
# int64

b = np.array([1.2, 3.5, 5.1])

print(b.dtype)
# float64

a = np.array(1,2,3,4)    # WRONG

print(a)
# ValueError: only 2 non-keyword arguments accepted

a = np.array([1,2,3,4])  # RIGHT
print(a)


print(np.zeros((3,4)))
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]


print(np.ones((2,3,4), dtype=np.int16))
# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]

#  [[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]]


print(np.empty((2,3)))
# [[1.39069238e-309 1.39069238e-309 1.39069238e-309]
#  [1.39069238e-309 1.39069238e-309 1.39069238e-309]]

print(np.arange(10, 30, 5))
# [10 15 20 25]

print(np.arange(0, 2, 0.3))
# [0.  0.3 0.6 0.9 1.2 1.5 1.8]

x = np.linspace(0, 99, 100)
print(x)
# [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17.
#  18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35.
#  36. 37. 38. 39. 40. 41. 42. 43. 44. 45. 46. 47. 48. 49. 50. 51. 52. 53.
#  54. 55. 56. 57. 58. 59. 60. 61. 62. 63. 64. 65. 66. 67. 68. 69. 70. 71.
#  72. 73. 74. 75. 76. 77. 78. 79. 80. 81. 82. 83. 84. 85. 86. 87. 88. 89.
#  90. 91. 92. 93. 94. 95. 96. 97. 98. 99.]


x = np.random.normal(loc=0, scale=1, size=(100, 2))
# Generating 2D numpy arrays with 200 $Normal(0, 1)$ random numbers to simulate data.

