numpy_reading_writing.py



# With no missing values -- numpy.loadtxt

x = np.loadtxt("demo.csv", delimiter=",", dtype = float)


# With missing values -- numpy.genfromtxt


print(open("csv.txt").read())  
# With non-whitespace delimiters

'''
1, 2, 3
4,, 6
7, 8, 9
'''

np.genfromtxt("csv.txt", delimiter=",", usemask=True)
# Masked-array output

'''  
masked_array(
  data=[[1.0, 2.0, 3.0],
        [4.0, --, 6.0],
        [7.0, 8.0, 9.0]],
  mask=[[False, False, False],
        [False,  True, False],
        [False, False, False]],
  fill_value=1e+20)
'''

np.genfromtxt("csv.txt", delimiter=",")  

'''
array([[ 1.,  2.,  3.],
       [ 4., nan,  6.],
       [ 7.,  8.,  9.]])
'''


f = open("fixedwidth.txt").read()  
print(f)  # doctest: +SKIP

'''
1   2      3
44      6
7   88889
'''

# Showing spaces as ^
print(f.replace(" ","^")) 

'''
1^^^2^^^^^^3
44^^^^^^6
7^^^88889
'''

np.genfromtxt("fixedwidth.txt", delimiter=4)  

'''
array([[1.000e+00, 2.000e+00, 3.000e+00],
       [4.400e+01,       nan, 6.000e+00],
       [7.000e+00, 8.888e+03, 9.000e+00]])
'''

print(open("nan.txt").read())  

'''
1 2 3
44 x 6
7  8888 9
'''

np.genfromtxt("nan.txt", missing_values="x")  
# A special value (e.g. “x”) indicates a missing field: Use it as the missing_values argument.

'''
array([[1.000e+00, 2.000e+00, 3.000e+00],
       [4.400e+01,       nan, 6.000e+00],
       [7.000e+00, 8.888e+03, 9.000e+00]])
'''


print(open("skip.txt").read())  

'''
1 2   3
44    6
7 888 9
'''

np.genfromtxt("skip.txt", invalid_raise=False)  
# You want to skip the rows with missing values: Set invalid_raise=False.

'''
__main__:1: ConversionWarning: Some errors were detected !
    Line #2 (got 2 columns instead of 3)
array([[  1.,   2.,   3.],
       [  7., 888.,   9.]])
'''

f = open("tabs.txt").read()  
print(f)  

'''
1       2       3
44              6
7       888     9
'''

# Tabs vs. spaces
print(f.replace("\t","^"))  

'''
1^2^3
44^ ^6
7^888^9
'''

np.genfromtxt("tabs.txt", delimiter="\t", missing_values=" +")  
# The delimiter whitespace character is different from the whitespace that indicates missing data. For instance, if columns are delimited by \t, then missing data will be recognized if it consists of one or more spaces.

'''
array([[  1.,   2.,   3.],
       [ 44.,  nan,   6.],
       [  7., 888.,   9.]])
'''

