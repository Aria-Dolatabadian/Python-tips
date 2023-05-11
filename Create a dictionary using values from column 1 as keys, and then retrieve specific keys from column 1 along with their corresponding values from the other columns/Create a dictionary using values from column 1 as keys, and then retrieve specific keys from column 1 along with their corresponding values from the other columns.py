import csv

# Read the CSV file and create a dictionary
my_dict = {}
with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        key = row[0]
        values = row[1:]  # Retrieve values from column 2 onwards
        my_dict[key] = values

# Retrieve specific keys from the dictionary
keys_to_retrieve = ["Bn-A07-p14273852", "Bn-A07-p12578940"]
output_data = [[key] + my_dict[key] for key in keys_to_retrieve]

# Export the data as CSV
output_file = "output.csv"
with open(output_file, mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(output_data)

# Optional: Read and print the output CSV file using pandas
import pandas as pd
df = pd.read_csv(output_file)
print(df)
