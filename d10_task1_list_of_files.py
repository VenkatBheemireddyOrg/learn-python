import os

folders = input("Please provide list of folder names separated by spaces :").split()
print("Input Folders :", folders)

for folder in folders:
    try:
        files = os.listdir(folder)
        print("Processing Folder is :", folder)
    except FileNotFoundError:
        print("Error:1201 - Given folder name is not present :", folder)
        continue
    except PermissionError:
        print("Error:1202 - No access to the given folder :", folder)
        continue
    for file in files:
        print("File details are :", file)
