#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Handle FileNotFoundError
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------


try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program Finished.")


# end of the program    