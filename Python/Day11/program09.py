#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Copy File
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import os
import shutil

def safe_file_copy(source, destination):
    # 1. Structural validation checks
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source path error: '{source}' does not exist.")
        
    if os.path.isdir(source):
        raise IsADirectoryError("Source target must be a file, not an entire folder.")

    # 2. Automatically handle directory destinations
    # If destination is a directory, it retains the original file name inside that directory
    if os.path.isdir(destination):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    try:
        print(f"Initiating transfer: {source} -> {destination}")
        
        # 3. Perform the copy operation (shutil.copy2 preserves file timestamps)
        shutil.copy2(source, destination)
        
    except PermissionError:
        print(f"🚨 [Access Denied]: Insufficient OS privileges to read or write to paths.")
    except IOError as e:
        print(f"🚨 [Storage Exception]: File transfer failed. Details: {e}")
    else:
        print("✅ [Transfer Success]: File copied perfectly with metadata intact.")


# --- Quick Usage Demonstration ---
if __name__ == "__main__":
    # Create a dummy file to test the function
    with open("original.txt", "w", encoding="utf-8") as f:
        f.write("Important backup archive data stream.")

    # Execute safe duplicate process
    safe_file_copy("original.txt", "backup_copy.txt")



# end of the program