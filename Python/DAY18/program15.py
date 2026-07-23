#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Employee Salary Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

employees = [
    {"id": 101, "name": "Om", "salary": 80000},
    {"id": 102, "name": "Rahul", "salary": 60000},
    {"id": 103, "name": "Priya", "salary": 75000},
    {"id": 104, "name": "Amit", "salary": 45000}
]

def employee_salaries_gen(emp_list):
    for emp in emp_list:
        yield emp["salary"]    

print("\n--- 4. Salary Values Only ---")
for salary in employee_salaries_gen(employees):
    print(f"₹{salary}")   