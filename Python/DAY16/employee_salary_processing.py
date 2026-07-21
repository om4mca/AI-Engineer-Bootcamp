#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: Employee Salary Processing System
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

employees = [
    {"name": "Om", "salary": 80000},
    {"name": "Rahul", "salary": 60000},
    {"name": "Priya", "salary": 75000},
    {"name": "Amit", "salary": 45000}
]

# Task 1
# Employees with salary > ₹60,000. using filter()

print()
print("******* Employees with salary > ₹60,000 ***********")
employee_salary = list(filter(lambda p: p["salary"] > 60000, employees))

print(employee_salary)

# Task 2
# Increase salary by 10%. using Map()
print()
print("******* Increase salary by 10% ***********")
updated_employees = list(map(lambda e: {**e, "salary": int(e["salary"] * 1.1)}, employees))

print(updated_employees)

# Task 3
# Sort employees by salary. using sort()

print()
print("****** Sort employees by salary **********")
employees.sort(
    key=lambda employee: employee["salary"]
)

print(employees)

# Task 4
# Calculate total salary expense. using Reduce()
print()
print("****** Total Salary Expense **********")
from functools import reduce
total_salary_expense = reduce(lambda acc, e: acc + e["salary"], employees, 0)

print("Total Salary Expense:", total_salary_expense)