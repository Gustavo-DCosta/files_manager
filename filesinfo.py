import os
import time 
path = r""          #chose the path that you want to ipect

# Get the file/directory stats
stat_info = os.stat(path)

# Create a readable output format
print(f"File: {path}")
print(f"Size: {stat_info.st_size} bytes")
print(f"Permissions (Mode): {oct(stat_info.st_mode)}")
print(f"Number of Links: {stat_info.st_nlink}")
print(f"Owner User ID: {stat_info.st_uid}")
print(f"Owner Group ID: {stat_info.st_gid}")
print(f"Last Access Time: {time.ctime(stat_info.st_atime)}")
print(f"Last Modification Time: {time.ctime(stat_info.st_mtime)}")
print(f"Metadata Change Time: {time.ctime(stat_info.st_ctime)}")
