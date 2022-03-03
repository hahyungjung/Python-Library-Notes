pandas_io.py

import pandas as pd

# Read and Write to CSV
pd.read_csv('file.csv', header=None, nrows=5)
df.to_csv('myDataFrame.csv')

# Read and Write to Excel
pd.read_excel('file.xlsx')
pd.to_excel('dir/myDataFrame.xlsx', sheet_name='Sheet1')

# Read multiple sheets from the same file
xlsx = pd.ExcelFile('file.xls')
df = pd.read_excel(xlsx, 'Sheet1')

# Read and Write to SQL 