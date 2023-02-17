import pandas as pd

df = pd.read_csv (r'D:\python\dataframe.csv')
print (df)

df['state_and_code'] = df['State'] + df['State_code']
print(df)

#with space

df['state_and_code'] = df['State'] +' '+ df['State_code']
print(df)
