pandas_creating_dataframe.py

import pandas as pd
import numpy as np

'''
pd.DataFrame 1) list of dictionries 2) Dictionary of lists

'''

df = pd.DataFrame(
		{"a" : [4, 5, 6],
         "b" : [7, 8, 9],
         "c" : [10, 11, 12]},
         index = [1, 2, 3])
print(df)

'''
   a  b   c
1  4  7  10
2  5  8  11
3  6  9  12
'''

df = pd.DataFrame(
    	[[4, 7, 10],
        [5, 8, 11],
        [6, 9, 12]],
        index=[1, 2, 3],
        columns=['a', 'b', 'c'])
print(df)

'''
   a  b   c
1  4  7  10
2  5  8  11
3  6  9  12
'''

df = pd.DataFrame(
        {"a" : [4 ,5, 6, 6, np.nan],
        "b" : [7, 8, np.nan, 9, 9],
        "c" : [10, 11, 12, np.nan, 12]},
        index = pd.MultiIndex.from_tuples(
        [('d',1),('d',2),('e',2),('e',3),('e',4)],
        names=['n','v']))
print(df)

'''
       a    b     c
n v                
d 1  4.0  7.0  10.0
  2  5.0  8.0  11.0
e 2  6.0  NaN  12.0
  3  6.0  9.0   NaN
  4  NaN  9.0  12.0
'''