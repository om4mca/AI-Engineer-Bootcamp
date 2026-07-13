#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Custom Exception
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------

class InvalidSalaryError(Exception):
    pass

salary = int(input("Enter Salary: "))

if salary < 0:
    raise InvalidSalaryError("Salary cannot be negative.")

# end of the program     