import pandas as pd

df = pd.read_excel (r'Data.xlsx', sheet_name='new')
print (df)
df['c'] = df['a'] + df['b']
print(df)
