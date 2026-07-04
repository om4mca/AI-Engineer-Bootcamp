# ------------------------------------------
# AI Engineer Bootcamp
# Day 3
# Program: Employee Management
# Author: Om Roy
# Date: 04-07-2026
# ------------------------------------------

employee_name=input("Enter Employee Name : ")
department=input("Enter Department : ")
basic_salary=float(input("Enter Basic Salary : "))
bonus=float(input("Enter Bonus : "))
tax=float(input("Enter Tax : "))
# net_salary=basic_salary+bonus-tax
# gross_salary=basic_salary+bonus


gross_salary = basic_salary + bonus

tax_amount = gross_salary * tax / 100

net_salary = gross_salary - tax_amount

print()
print("-------Employee Management System----------")

print(f"Employee Name : {employee_name}")
print(f"Department : {department}")
print(f"Basic Salary : {basic_salary}")
print(f"Bonus : {bonus}")
print(f"Gross Salary : {gross_salary}")
print(f"Tax Amount: {tax_amount}")
print(f"Net Salary : {net_salary}")




# End of the program
