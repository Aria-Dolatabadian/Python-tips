import pandas as pd

# Set the input file path
input_file = 'genes.xlsx'

# Read the Excel file into a Pandas DataFrame object
xl = pd.ExcelFile(input_file)

# Loop through each sheet in the Excel file
for sheet_name in xl.sheet_names:
    # Read the sheet into a Pandas DataFrame object
    df = xl.parse(sheet_name)

    # Set the output file path
    output_file = f'{sheet_name}.csv'

    # Write the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
