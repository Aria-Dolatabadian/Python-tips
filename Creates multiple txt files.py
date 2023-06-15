import os

directory = 'e:/'
filename = 'New file'

# Ask for the number of files to create
num_files = int(input("How many files do you want to create? "))

for i in range(num_files):
    # Generate a unique filename for each file
    new_filename = f"{filename}_{i + 1}.txt"

    # Create a new TXT file
    file_path = os.path.join(directory, new_filename)
    with open(file_path, 'w') as txtfile:
        txtfile.write("This is a sample text.")

    print(f"TXT file '{new_filename}' created successfully.")

print("All TXT files created.")
