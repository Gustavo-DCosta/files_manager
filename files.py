import os
import psutil

# Get all disk partitions
partitions = psutil.disk_partitions()

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
