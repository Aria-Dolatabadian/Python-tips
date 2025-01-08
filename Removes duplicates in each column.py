import pandas as pd

# Read the CSV file
df = pd.read_csv('input_file.csv')

# Remove duplicates from each column
df_cleaned = df.apply(lambda x: x.drop_duplicates().reset_index(drop=True))

# Export the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('output_file.csv', index=False)
