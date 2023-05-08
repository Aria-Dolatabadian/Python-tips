import pandas as pd

# Read in the first CSV file
df1 = pd.read_csv('a.csv')

# Read in the second CSV file
df2 = pd.read_csv('b.csv')

# Compare the values in the 'column1' column of both files
shared_values = set(df1['Gene']).intersection(df2['Gene'])

# Filter the first file to exclude the shared values and keep the other columns
df1_unique = df1[~df1['Gene'].isin(shared_values)].drop_duplicates()

# Filter the second file to exclude the shared values and keep the other columns
df2_unique = df2[~df2['Gene'].isin(shared_values)].drop_duplicates()

# Write the two filtered files to disk
df1_unique.to_csv('file_a_unique.csv', index=False)
df2_unique.to_csv('file_b_unique.csv', index=False)
