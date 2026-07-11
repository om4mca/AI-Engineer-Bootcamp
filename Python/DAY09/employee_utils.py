#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Bonus Project Employee Utility Library
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import uuid

def generate_employee_id() -> str:
    """Generates a unique 6-character alphanumeric employee ID."""
    return f"EMP-{str(uuid.uuid4())[:6].upper()}"

def calculate_bonus(performance_score: int, base_salary: float) -> float:
    """
    Calculates bonus based on a performance score (1 to 5).
    Score 5 = 20%, Score 4 = 10%, Score 3 = 5%, others = 0%.
    """
    if performance_score == 5:
        multiplier = 0.20
    elif performance_score == 4:
        multiplier = 0.10
    elif performance_score == 3:
        multiplier = 0.05
    else:
        multiplier = 0.0
        
    return round(base_salary * multiplier, 2)

def calculate_tax(taxable_income: float, tax_rate: float = 0.15) -> float:
    """Calculates the tax amount based on income and tax rate."""
    if taxable_income < 0 or tax_rate < 0:
        raise ValueError("Income and tax rates cannot be negative.")
    return round(taxable_income * tax_rate, 2)

def calculate_salary(base_salary: float, bonus: float, deductions: float) -> float:
    """Calculates the net take-home salary after adding bonuses and subtracting deductions."""
    if base_salary < 0 or bonus < 0 or deductions < 0:
        raise ValueError("Financial parameters cannot be negative.")
    
    gross_salary = base_salary + bonus
    net_salary = gross_salary - deductions
    return max(0.0, round(net_salary, 2))

#end of the program