#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: filter() Salary > 50000
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

employees = [
    {"name": "Om", "salary": 80000},
    {"name": "Rahul", "salary": 60000},
    {"name": "Priya", "salary": 75000},
    {"name": "Amit", "salary": 45000}
]


employee_salary = list(filter(lambda p: p["salary"] > 50000, employees))

print(employee_salary)
