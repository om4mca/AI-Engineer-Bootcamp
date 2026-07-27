#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Context Manager + File
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

# Writing to a file
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)