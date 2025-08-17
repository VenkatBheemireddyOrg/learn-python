import os

folders = input("Please provide list of folder names separated by spaces :").split()
print("Input Folders :", folders)

for folder in folders:
    try:
        files = os.listdir(folder)
        print("Processing Folder is :", folder)
    except FileNotFoundError:
        print("Given folder name is not present :", folder)
        break
    except PermissionError:
        print("No access to the given folder :", folder)
        break
    for file in files:
        print("File details are :", file)
