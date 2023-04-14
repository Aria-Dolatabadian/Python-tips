import pandas as pd
df = pd.read_csv (r'Rgene.csv')
print (df)
print('................')
df = df[df.duplicated(subset=['Genes'], keep=False)]
print (df)
