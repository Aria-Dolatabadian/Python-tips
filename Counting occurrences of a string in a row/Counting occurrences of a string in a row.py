import pandas as pd
df = pd.read_csv (r'Primer.csv')
print (df.columns)
df['count'] = df['Seq'].str.count('GC')
print (df)
print (df.columns)
df['count'] = df['Seq'].str.count('AA')
print (df)
print (df.columns)
df['count'] = df['Seq'].str.count('T')
print (df)
print (df.columns)
df['count'] = df['Seq'].str.count('G')
print (df)
