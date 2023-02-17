import pandas as pd

df = pd.read_excel (r'D:\python\Data.xlsx')
print (df)

df['c'] = df.a.astype(str) + df.b.astype(str)
print (df)
