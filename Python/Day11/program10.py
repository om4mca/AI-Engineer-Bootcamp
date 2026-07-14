#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Rename File (using os)
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import os

src = "docs/old_name.csv"
dst = "docs/new_name.csv"

try:
    os.rename(src, dst)
    print("File renamed successfully.")
except FileNotFoundError:
    print(f"Error: The file '{src}' was not found.")
except FileExistsError:
    print(f"Error: A file named '{dst}' already exists.")
except PermissionError:
    print("Error: Insufficient permissions to rename this file.")
