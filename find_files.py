import os
from pathlib import Path
import glob

def path_exist():
    path = r"" #put here you'r path
    try:
        if os.path.exists(path):
            print(f"{path}: path does exist")
            if os.path.isfile(path):
                print("The path is a file")
            elif os.path.isdir(path):
                print("The path is a directory")
        else:
            print("The path does not exist")
    except Exception as e:
        print(f"Couldn't find anything. Error: {e}")

path_exist()

def match_exist():
    try:    # Find all .py files in the current directory and subdirectories
        py_files = glob.glob('**/*.py', recursive=True)
        print(py_files)
    except:
        print("None found")
 
match_exist()


 
