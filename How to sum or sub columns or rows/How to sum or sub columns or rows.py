import pandas as pd

df = pd.read_excel (r'D:\python\Data.xlsx')
print (df)
print('...............................')

sum_column = df.sum(axis=0)
print (sum_column)
print('...............................')
sum_column = df.sum(axis=1)
print (sum_column)
print('...............................')

df['diff'] = df['value'] - df['row']
print("\Difference of value and row :\n", df)
