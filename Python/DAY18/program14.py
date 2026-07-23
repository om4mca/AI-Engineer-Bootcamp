#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Employee Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------
employees = [
    {"id": 101, "name": "Om", "salary": 80000},
    {"id": 102, "name": "Rahul", "salary": 60000},
    {"id": 103, "name": "Priya", "salary": 75000},
    {"id": 104, "name": "Amit", "salary": 45000}
]

### Generator 1    All employees.

def employee_generator(employees):

    for employee in employees:
        yield employee

print("--- All Employees ---")
for employee in employee_generator(employees):
    print(employee)        