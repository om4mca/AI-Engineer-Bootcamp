# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Multiplication Table
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------

# Convert the input string into a whole number (integer)
number = int(input("Enter Number:- "))

print(f"--- Multiplication Table of {number} ---")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#End of the program