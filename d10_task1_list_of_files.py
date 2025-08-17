import os

folders = input("Please provide list of folder names separated by spaces :").split()
print("Input Folders :", folders)

for folder in folders:
    files = os.listdir(folder)
    print("Processing Folder is :", folder)

    for file in files:
        print(file)
