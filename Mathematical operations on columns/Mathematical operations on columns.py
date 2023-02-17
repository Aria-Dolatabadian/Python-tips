import pandas as pd

df = pd.read_excel (r'D:\python\Data.xlsx', sheet_name='new')
print (df)
df['c'] = df['a'] + df['b']
print(df)
