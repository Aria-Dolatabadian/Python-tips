#This code reads all CSV files in a specified folder and writes each file to a separate sheet in an Excel file.

import pandas as pd
import glob
# Path to folder containing CSV files
path = 'C:/Users/00090473/PycharmProjects/pythonProject/file'

# Get list of CSV files in folder
all_files = glob.glob(path + "/*.csv")

# Create empty Excel writer object
with pd.ExcelWriter('C:/Users/00090473/PycharmProjects/pythonProject/file/merged.xlsx', engine='xlsxwriter') as writer:
    # Loop through CSV files and write each to a separate sheet in the Excel file
    for filename in all_files:
        # Read CSV file into Pandas DataFrame
        df = pd.read_csv(filename)

        # Extract sheet name from filename (without extension)
        sheet_name = filename.split('\\')[-1].split('.')[0]

        # Replace invalid characters in sheet name with underscore
        sheet_name = sheet_name.replace('[', '_').replace(']', '_').replace('*', '_').replace('?', '_').replace('/', '_').replace('\\', '_').replace(':', '_')

        # Write DataFrame to Excel sheet
        df.to_excel(writer, sheet_name=sheet_name, index=False)
