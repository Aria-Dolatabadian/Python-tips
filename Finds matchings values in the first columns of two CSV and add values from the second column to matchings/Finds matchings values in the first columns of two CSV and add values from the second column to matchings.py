import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('position.csv')

# Read the second CSV file
df2 = pd.read_csv('position_marker.csv')

# Merge the two dataframes based on matching values in column A and add values from column B to the matching values
merged_df = pd.merge(df1, df2, on='pos', how='left')

# Print the merged dataframe with the added values
print(merged_df)

# Export the merged dataframe to a CSV file
merged_df.to_csv('results.csv', index=False)
