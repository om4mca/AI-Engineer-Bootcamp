#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: try & except
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------


try:
    age = int(input("Enter Age: "))
    print("Age:", age)

except ValueError:
    print("❌ Please enter a valid number.")

print()
print("-----------Handling Multiple Exceptions---------")
try:
    num = int(input("Enter Number: "))
    result = 100 / num
    print(result)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

print()
print("----------else------------")
try:
    number = int(input("Enter Number: "))

except ValueError:
    print("Invalid Input")

else:
    print("Square =", number ** 2)

print()
print("--------finally----------")

try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program Finished.")

    print()
    print("----------raise----------")

    age = int(input("Enter Age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print(age)

print()
print("-----Custom Exception (Introduction)--------")

class InvalidSalaryError(Exception):
    pass

salary = int(input("Enter Salary: "))

if salary < 0:
    raise InvalidSalaryError("Salary cannot be negative.")
    # end of the program25