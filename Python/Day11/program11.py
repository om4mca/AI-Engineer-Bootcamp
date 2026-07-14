#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Delete File (using os)
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import os

file_path = "demofile.txt"

try:
    os.remove(file_path)
    print("File successfully removed.")
except FileNotFoundError:
    print("Error: The specified file could not be found.")
except PermissionError:
    print("Error: You do not have the permissions required to delete this file.")
except IsADirectoryError:
    print("Error: The path points to a directory, not a file.")
