#iterate through each sheet in the XLSX file, ask the user for a column header to search based on, and then search for the provided value in that column. 
#It will export the matched rows to separate CSV files named "Search_1.csv", "Search_2.csv", and so on.

import pandas as pd
# Read the XLSX file
file_path = "Inventory.xlsx"
xls = pd.ExcelFile(file_path)
# Initialize the sheet index
sheet_index = 1
# Continue searching until user chooses to exit
while True:
    # Get the column headers from the first sheet
    first_sheet_name = xls.sheet_names[0]
    df_first_sheet = pd.read_excel(file_path, sheet_name=first_sheet_name)
    column_headers = df_first_sheet.columns.tolist()
    # Display column headers as options to choose from
    print("Available column headers:")
    for i, header in enumerate(column_headers):
        print(f"{i+1}. {header}")
    # Get the user input for the column header to search
    column_index = int(input("Enter the number of the column header to search based on (0 to exit): ")) - 1
    # Check if user chose to exit
    if column_index < 0:
        break
    column_header = column_headers[column_index]
    # Get the user input for the search value
    search_value = input(f"Enter the {column_header} value to search for: ")
    # Initialize an empty list to store the matching DataFrames
    matched_dfs = []
    # Iterate through each sheet in the XLSX file
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # Filter the DataFrame for rows containing the case-insensitive search value in the specified column
        matching_rows = df[df[column_header].astype(str).str.lower() == search_value.lower()]
        # Append the matching DataFrame to the list
        matched_dfs.append(matching_rows)
    # Concatenate the matching DataFrames into a single DataFrame
    matched_rows = pd.concat(matched_dfs, ignore_index=True)
    # Export the matched rows to a CSV file
    output_file = f"Search_{sheet_index}.csv"
    matched_rows.to_csv(output_file, index=False)

    print(f"The rows containing '{search_value}' (case-insensitive) in column '{column_header}' have been exported to '{output_file}'.")

    # Increment the sheet index for the next search
    sheet_index += 1

print("Search process completed.")

