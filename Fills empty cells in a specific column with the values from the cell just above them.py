import pandas as pd

# Specify the input and output file paths
input_file_path = 'input.csv'
output_file_path = 'output.csv'

# Specify the column where you want to fill empty cells
column_to_fill = 'Length'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Use the forward-fill method to fill empty cells in the specified column
df[column_to_fill].fillna(method='ffill', inplace=True)

# Write the updated DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)

print("CSV file with empty cells filled and saved to 'output.csv'.")
