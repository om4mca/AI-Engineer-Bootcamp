#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:  Employee salary data process
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

employees = [
    {"id": "E101", "name": "Aarav", "dept": "IT", "salary": 75000},
    {"id": "E102", "name": "Vihaan", "dept": "HR", "salary": 50000},
    {"id": "E103", "name": "Ananya", "dept": "IT", "salary": 90000},
    {"id": "E104", "name": "Diya", "dept": "Finance", "salary": 65000},
    {"id": "E105", "name": "Kabir", "dept": "HR", "salary": 55000},
]


salaries = [emp["salary"] for emp in employees]
total_payout = sum(salaries)
avg_salary = total_payout / len(salaries)

# Minimum और Maximum Salary
highest_paid = max(employees, key=lambda x: x["salary"])
lowest_paid = min(employees, key=lambda x: x["salary"])

print(f"💰 Total Salary Payout: ₹{total_payout:,}")
print(f"📊 Average Salary: ₹{avg_salary:,.2f}")
print(f"🥇 Highest Salary: {highest_paid['name']} (₹{highest_paid['salary']:,})")
print(f"🥉 Lowest Salary: {lowest_paid['name']} (₹{lowest_paid['salary']:,})")