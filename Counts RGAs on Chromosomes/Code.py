import pandas as pd

# Read the CSV file
csv_file = 'data.csv'
df = pd.read_csv(csv_file)
# Count the number of each type on each chromosome
count_df = df.groupby(['Chromosomes', 'Type']).size().reset_index(name='Count')
# Display the count dataframe
print(count_df)
count_df.to_csv("RGA_count.csv", index=False)

