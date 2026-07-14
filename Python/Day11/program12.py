#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Check File Exists
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

from pathlib import Path

file_path = Path("example.txt")

if file_path.is_file():
    print("File exists")
else:
    print("File does not exist")
