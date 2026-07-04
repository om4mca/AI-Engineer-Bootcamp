# ------------------------------------------
# AI Engineer Bootcamp
# Day 3
# Program: Employee ID Generator Hint: Department ke first 2 letters  Name ke initials  Fixed Number
# Author: Om Roy
# Date: 04-07-2026
# ------------------------------------------


department = input("Enter Your Department : ")
name = input("Enter Your Name : ")
fixed_number = input("Enter Fixed Number : ")

employee_id = department[:2].upper() + '-' + name[:2].upper() + '-' + fixed_number
print(f"Your Employee ID is: {employee_id}")

#End of the program
