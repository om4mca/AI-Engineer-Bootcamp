#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: Lambda Maximum
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

employees = [
    {"name": "Om", "salary": 80000},
    {"name": "Rahul", "salary": 60000},
    {"name": "Priya", "salary": 75000},
    {"name": "Amit", "salary": 45000}
]


highest_paid = max(employees, key=lambda e: e["salary"])

print("Highest Paid Employee:", highest_paid)