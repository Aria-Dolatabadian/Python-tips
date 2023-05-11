#reads a CSV file ("data.csv"), prompts the user to enter a value to search for,
# and then searches for rows in the file that contain the search value.
# If matching rows are found, it prints the header row and the matching rows.
# It also exports the matching data to a new CSV file ("output.csv").
import csv

input_file = "data.csv"
output_file = "output.csv"

with open(input_file, mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)
    search_value = input('Enter the value to search for:')
    matching_data = []
    for row in reader:
        if search_value in row:
            matching_data.append(row)

    if matching_data:
        print(f'Matching data for {search_value}:')
        print(header)
        for row in matching_data:
            print(row)

        with open(output_file, mode="w", newline='') as output:
            writer = csv.writer(output)
            writer.writerow(header)
            writer.writerows(matching_data)

        print(f"The matching data has been exported to '{output_file}'.")
    else:
        print(f"No matching data for {search_value}.")
