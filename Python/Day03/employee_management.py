# ------------------------------------------
# AI Engineer Bootcamp
# Day 3
# Program: Employee Management Add :  Designation HRA = 20%  DA = 10% PF = 12%
# Author: Om Roy
# Date: 04-07-2026
# ------------------------------------------

employee_name=input("Enter Employee Name : ")
department=input("Enter Department : ")
designation=input("Enter Designation : ")
basic_salary=float(input("Enter Basic Salary : "))
bonus=float(input("Enter Bonus : "))
tax=float(input("Enter Tax : "))


hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100 
pf = basic_salary * 12 / 100   

gross_salary = basic_salary + bonus

tax_amount = gross_salary * tax / 100

net_salary = gross_salary - tax_amount

print()
print("-------Employee Management System----------")

print(f"Employee Name : {employee_name}")
print(f"Department : {department}")
print(f"Designation : {designation}")
print(f"Basic Salary : {basic_salary}")
print(f"Bonus : {bonus}")
print(f"Gross Salary : {gross_salary}")
print(f"HRA : {hra}")
print(f"DA : {da}")
print(f"PF : {pf}")
print(f"Tax Amount: {tax_amount}")
print(f"Net Salary : {net_salary}")





# End of the program
