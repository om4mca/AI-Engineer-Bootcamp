#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Handle ZeroDivisionError
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------


try:
    num = int(input("Enter Number: "))
    result = 100 / num
    print(result)


except ZeroDivisionError:
    print("Cannot divide by zero.")


# end of the program    