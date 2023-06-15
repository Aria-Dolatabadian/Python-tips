import os
#install python-docx
from docx import Document

directory = 'e:/'
filename = 'New Microsoft Word Document'

# Ask for the number of files to create
num_files = int(input("How many files do you want to create? "))

for i in range(num_files):
    # Generate a unique filename for each file
    new_filename = f"{filename}_{i + 1}.docx"

    # Create a new Document object
    doc = Document()
    # doc.add_paragraph("This is a sample paragraph.")

    # Save the document with the specified filename
    file_path = os.path.join(directory, new_filename)
    doc.save(file_path)

    print(f"DOCX file '{new_filename}' created successfully.")

print("All DOCX files created.")
