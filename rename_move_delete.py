import os
import shutil

# Define the path for the file to modify
path_changes = r"" #the path you chose

def create_files(): # Try to open or create a new Python file, handling errors
    try:
        f = open("newfile1a.py", "x")  # 'x' mode will create the file, raise an error if it already exists
        print("File 'newfile.py' created successfully.")
    except FileExistsError:
        print("File 'newfile.py' already exists.")

def read_files():
    # Handle reading an existing file
    try:
        with open(path_changes, "r") as file:  # 'r' mode to read the file
            print(file.read())
    except FileNotFoundError:
        print("The file 'myfile.txt' could not be found.")

def remove_files():
    try:
        os.remove(r"C:\Users\veraf\Desktop\VsCode\newfile.py")
        print("the file has been eliminated")
    except:
        print("Something went wrong, The file hasn't been removed!!")

def moving_path():
    try:    
        start = r""    #the folder/file you want to move
        destination = r"" #the path in wich the file/directory will be moved into
        shutil.move(start, destination)
    except:
        print("something went wrong, couldn't move you'r files")

create_files()
read_files()
remove_files()
