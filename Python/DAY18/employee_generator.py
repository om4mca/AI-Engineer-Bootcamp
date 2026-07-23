#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Employee Data Generator
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

### Generator 2   Employees with salary > ₹60,000.    

def sal_generator(employees):

    for employee in employees:

        if employee["salary"] > 60000:
            yield employee  

print("\n--- Senior employees (Salary > 60,000) ---")
for senior in sal_generator(employees):
    print(f"ID: {senior['id']} | Name: {senior['name']} | Salary: {senior['salary']}")   

    

# 3. Generator for Employee Names Only

def employee_names_gen(emp_list):
    for emp in emp_list:
        yield emp["name"]
print("\n--- 3. Employee Names Only ---")
for name in employee_names_gen(employees):
    print(name)        

# 4. Generator for Salary Values Only

def employee_salaries_gen(emp_list):
    for emp in emp_list:
        yield emp["salary"]    

print("\n--- 4. Salary Values Only ---")
for salary in employee_salaries_gen(employees):
    print(f"₹{salary}")        