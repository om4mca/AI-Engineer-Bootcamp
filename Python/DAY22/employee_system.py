#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:  Employee Data Analysis System
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------


# Input Dataset
employees = [
    {
        "name": "Om",
        "department": "IT",
        "salary": 50000
    },
    {
        "name": "Raj",
        "department": "HR",
        "salary": 40000
    },
    {
        "name": "Amit",
        "department": "IT",
        "salary": 60000
    }
]


# ======================================================
# 10 Functions Implementation
# ======================================================

# 1. Total Employees
def get_total_employees(data):
    return len(data)


# 2. Average Salary
def get_average_salary(data):
    if not data:
        return 0
    total_salary = sum(emp["salary"] for emp in data)
    return total_salary / len(data)


# 3. Highest Salary
def get_highest_salary(data):
    if not data:
        return 0
    return max(emp["salary"] for emp in data)


# 4. Lowest Salary
def get_lowest_salary(data):
    if not data:
        return 0
    return min(emp["salary"] for emp in data)


# 5. Filter IT Employees
def filter_it_employees(data):
    return [emp for emp in data if emp["department"].upper() == "IT"]


# 6. Filter HR Employees
def filter_hr_employees(data):
    return [emp for emp in data if emp["department"].upper() == "HR"]


# 7. Department-wise Employee Count
def get_dept_employee_count(data):
    counts = {}
    for emp in data:
        dept = emp["department"]
        counts[dept] = counts.get(dept, 0) + 1
    return counts


# 8. Department-wise Average Salary
def get_dept_average_salary(data):
    dept_salaries = {}
    for emp in data:
        dept = emp["department"]
        if dept not in dept_salaries:
            dept_salaries[dept] = []
        dept_salaries[dept].append(emp["salary"])
    
    dept_averages = {
        dept: sum(salaries) / len(salaries) 
        for dept, salaries in dept_salaries.items()
    }
    return dept_averages


# 9. Highest Paid Employee
def get_highest_paid_employee(data):
    if not data:
        return None
    return max(data, key=lambda emp: emp["salary"])


# 10. Generate Summary Report
def generate_summary_report(data):
    total_emp = get_total_employees(data)
    avg_salary = get_average_salary(data)
    highest_sal = get_highest_salary(data)
    lowest_sal = get_lowest_salary(data)
    dept_counts = get_dept_employee_count(data)
    dept_avg_sal = get_dept_average_salary(data)
    top_paid_emp = get_highest_paid_employee(data)

    print("====== EMPLOYEE DATA ANALYSIS ======")
    print()
    print(f"Total Employees: {total_emp}")
    print()
    print(f"Average Salary: ₹{avg_salary:,.2f}")
    print()
    print(f"Highest Salary: ₹{highest_sal:,.2f}")
    print()
    print(f"Lowest Salary: ₹{lowest_sal:,.2f}")
    print()
    print(f"Highest Paid Employee: {top_paid_emp['name']} (₹{top_paid_emp['salary']:,})")
    print()
    print("Department-wise Employee Count:")
    for dept, count in dept_counts.items():
        print(f"  {dept}: {count}")
    print()
    print("Department-wise Average Salary:")
    for dept, avg_sal in dept_avg_sal.items():
        print(f"  {dept}: ₹{avg_sal:,.2f}")


# ======================================================
# Execution
# ======================================================
if __name__ == "__main__":
    generate_summary_report(employees)