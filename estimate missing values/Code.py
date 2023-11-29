import pandas as pd
# Read CSV into Python
read_data = pd.read_csv('data_with_missing_values.csv')
# Estimate missing values (for simplicity, using mean)
mean_values = read_data.mean()
# Fill missing values with mean
filled_data = read_data.fillna(mean_values)
#Export new CSV file
filled_data.to_csv('data_filled.csv', index=False)
