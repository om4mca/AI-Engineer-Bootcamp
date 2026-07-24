#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Employee Salary Audit Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

from functools import wraps

# Audit Decorator Definition
def audit_salary(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Salary calculation started")
        result = func(*args, **kwargs)
        print("Salary calculation completed")
        return result
    return wrapper


# Function using the Decorator
@audit_salary
def calculate_salary(basic, bonus):
    return basic + bonus


# --- Execution ---

salary = calculate_salary(50000, 10000)
print(salary)