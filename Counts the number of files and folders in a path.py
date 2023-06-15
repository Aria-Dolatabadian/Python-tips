import os

def count_files_and_folders(folder_path):
    num_files = 0
    num_folders = 0

    for _, dirs, files in os.walk(folder_path):
        num_files += len(files)
        num_folders += len(dirs)

    return num_files, num_folders

folder_path = input("Enter the folder path: ")

num_files, num_folders = count_files_and_folders(folder_path)

print("Number of files:", num_files)
print("Number of folders:", num_folders)
