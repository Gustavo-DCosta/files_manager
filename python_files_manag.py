import os 
import time
import psutil

# Get all disk partitions
partitions = psutil.disk_partitions()

def look_partitions():
# Loop through each partition and print its info
    for partition in partitions:
        try:
            # Get the partition's mount point (e.g., C:\\, D:\\, etc.)
            mountpoint = partition.mountpoint
            
            # Get disk usage (free, total space)
            usage = psutil.disk_usage(mountpoint)
            
            # Get type of filesystem (e.g., NTFS, FAT32)
            fstype = partition.fstype
            
            # Label the type of drive
            if 'removable' in partition.opts:
                drive_type = 'Removable drive'
            elif 'cdrom' in partition.opts:
                drive_type = 'CD-ROM drive'
            elif 'cloud' in partition.opts:  # Hypothetical check for cloud drives
                drive_type = 'Cloud drive'
            else:
                drive_type = 'Local drive'
            
            print(f"Drive: {mountpoint} - Type: {drive_type} - Filesystem: {fstype} - Total: {usage.total // (1024**3)} GB")
        
        except PermissionError:
            # Handle cases where permission is denied (like system partitions)
            print(f"Drive: {mountpoint} - Permission denied")

look_partitions()

path = input("What's the path you want to use? Please insert with example r'G:\\Mon Drive': ")

try:
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

except FileNotFoundError:
    print(f"The path '{path}' does not exist. Please check and try again.")

# List files for each path
files = os.listdir(path)

# Check the selected path and print the corresponding file list
print(files)
print("Invalid option selected")