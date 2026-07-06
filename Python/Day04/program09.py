# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: Leap Year
# Author: Om Roy
# Date: 06-07-2026
# ------------------------------------------


# Get integer input from user
year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#End of the program