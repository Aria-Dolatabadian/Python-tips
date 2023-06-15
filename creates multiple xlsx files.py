import openpyxl
directory = 'e:/'
filename = 'New Microsoft Excel Worksheet'

# Ask for the number of files to create
num_files = int(input("How many files do you want to create? "))

for i in range(num_files):
    # Generate a unique filename for each file
    new_filename = f"{filename}_{i + 1}.xlsx"

    # Create a new workbook
    workbook = openpyxl.Workbook()

    # Save the workbook to the specified directory and filename
    workbook.save(f"{directory}/{new_filename}")

    print(f"Excel file '{new_filename}' created successfully.")

print("All Excel files created.")
