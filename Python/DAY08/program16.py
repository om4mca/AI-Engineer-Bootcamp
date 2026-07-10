#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Employee Salary Function
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

def calculate_net_salary(basic_salary):
    """
    Calculates net payable salary based on standard corporate breakdown.
    - HRA (House Rent Allowance): 10% of basic
    - DA (Dearness Allowance): 5% of basic
    - PF (Provident Fund): 12% of basic
    - Professional Tax: 2% of gross salary
    """
    if basic_salary < 0:
        raise ValueError("Basic salary cannot be negative.")
        
    hra = basic_salary * 0.10
    da = basic_salary * 0.05
    pf = basic_salary * 0.12
    
    gross_salary = basic_salary + hra + da
    professional_tax = gross_salary * 0.02
    
    net_salary = gross_salary - (pf + professional_tax)
    
    return {
        "Gross Salary": round(gross_salary, 2),
        "HRA": round(hra, 2),
        "DA": round(da, 2),
        "PF Deduction": round(pf, 2),
        "Tax Deduction": round(professional_tax, 2),
        "Net Salary": round(net_salary, 2)
    }

# Example Usage
payroll_details = calculate_net_salary(80000)
print(payroll_details)

# output : {'Gross Salary': 92000.0, 'HRA': 8000.0, 'DA': 4000.0, 'PF Deduction': 9600.0, 'Tax Deduction': 1840.0, 'Net Salary': 80560.0}

# end of the program