import csv

# Input and output file paths
input_file = 'Data.csv'
output_file = 'output.csv'

# Read the CSV file and store its contents in a list of lists
data = []
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data.append(row)

# Create a new list to store the modified data
new_data = []

# Initialize a counter to keep track of replicates
replicate_count = 0

# Initialize a list to store values for averaging
values_to_average = [0.0, 0.0, 0]

# Iterate through the rows in the original data
for row in data:
    gene_name, min_expression, max_expression = row
    replicate_count += 1

    # Append the current row to the new_data list
    new_data.append(row)

    # Add the values to the list for averaging
    values_to_average[0] += float(min_expression)
    values_to_average[1] += float(max_expression)
    values_to_average[2] += 1  # Count the number of values added

    # Check if it's the third replicate for the current gene
    if replicate_count % 3 == 0:
        # Calculate the average values
        avg_min_expression = values_to_average[0] / values_to_average[2]
        avg_max_expression = values_to_average[1] / values_to_average[2]

        # Add an empty row with average values
        new_data.append(['', avg_min_expression, avg_max_expression])

        # Reset the replicate counter and values for averaging
        replicate_count = 0
        values_to_average = [0.0, 0.0, 0]

# Write the modified data to the output CSV file
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(new_data)

print(f'Processed data written to {output_file}')
