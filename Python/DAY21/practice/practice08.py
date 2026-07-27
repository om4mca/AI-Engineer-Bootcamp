#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: File Handling + Exception
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------
try:
    with open("config.json", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: The specified file could not be found.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except OSError as e:
    print(f"An unexpected file system error occurred: {e}")