import pyreadr
import pandas as pd
# Read the RDS file
result = pyreadr.read_r('gene_expression.rds')
print(result)
# Access the data frame from the result object
data = result[None]
# Convert the data frame to a pandas DataFrame
df = pd.DataFrame(data)
# Export the DataFrame to a CSV file
df.to_csv('gene_expression.csv', index=False)
