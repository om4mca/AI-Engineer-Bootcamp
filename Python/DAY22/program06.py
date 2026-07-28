#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:  Employees filter based on department 
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

employees = [
    {"id": "E101", "name": "Aarav", "dept": "IT", "salary": 75000},
    {"id": "E102", "name": "Vihaan", "dept": "HR", "salary": 50000},
    {"id": "E103", "name": "Ananya", "dept": "IT", "salary": 90000},
    {"id": "E104", "name": "Diya", "dept": "Finance", "salary": 65000},
]


it_employees = [emp for emp in employees if emp["dept"] == "IT"]

print("--- IT Department Employees ---")
for emp in it_employees:
    print(f"ID: {emp['id']} | Name: {emp['name']} | Salary: ₹{emp['salary']}")