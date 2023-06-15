import csv
import os

directory = 'e:/'
filename = 'New CSV Worksheet'

# Ask for the number of files to create
num_files = int(input("How many files do you want to create? "))

for i in range(num_files):
    # Generate a unique filename for each file
    new_filename = f"{filename}_{i + 1}.csv"

    # Create a new CSV file
    file_path = os.path.join(directory, new_filename)
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write some data to the CSV file
        # writer.writerow(['Column 1', 'Column 2', 'Column 3'])
        # writer.writerow(['Data 1', 'Data 2', 'Data 3'])

    print(f"CSV file '{new_filename}' created successfully.")

print("All CSV files created.")
