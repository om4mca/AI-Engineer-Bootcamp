#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: map() Salary Increase
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

employees = [
    {"name": "Om", "salary": 80000},
    {"name": "Rahul", "salary": 60000},
    {"name": "Priya", "salary": 75000},
    {"name": "Amit", "salary": 45000}
]


updated_employees = list(map(
    lambda e: {**e, "salary": round(e["salary"] * 1.10)}, 
    employees
))

print(updated_employees)