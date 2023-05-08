import pandas as pd

# read first CSV file
df1 = pd.read_csv('1.csv')

# read second CSV file
df2 = pd.read_csv('2.csv')

# get intersection of values in column 'column1' in both dataframes
shared_values = set(df1['Gene']).intersection(set(df2['Gene']))

# create a new dataframe with rows from both files that have shared values in column1
merged_df = pd.merge(df1[df1['Gene'].isin(shared_values)], df2[df2['Gene'].isin(shared_values)], on='Gene')

# write merged dataframe to a new CSV file
merged_df.to_csv('shared values.csv', index=False)
