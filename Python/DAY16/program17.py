#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: Sort Employees by Salary
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

employees = [
    {"name": "Om", "salary": 80000},
    {"name": "Rahul", "salary": 60000},
    {"name": "Priya", "salary": 75000},
    {"name": "Amit", "salary": 45000}
]


employees.sort(
    key=lambda employee: employee["salary"]
)

print(employees)