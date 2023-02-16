import pandas as pd
df = pd.read_excel (r'D:\python\Data.xlsx')
print (df)
df["row*value"] = df["row"] * df["value"]
print(df)
