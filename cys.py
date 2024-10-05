import os

# Define paths
path = r"C:\\"
path2 = r"D:\\"
path3 = r"G:\\Mon Drive"

# Get user input and ensure it's an integer
what_path = int(input("What path do you want? 1, 2, or 3: "))

# List files for each path
files = os.listdir(path)
files2 = os.listdir(path2)
files3 = os.listdir(path3)

# Check the selected path and print the corresponding file list
if what_path == 1:
    print(files)
elif what_path == 2:
    print(files2)
elif what_path == 3:
    print(files3)
else:
    print("Invalid option selected")
