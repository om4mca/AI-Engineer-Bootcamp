# Importing all functions explicitly from the employee utility module
from employee_utils import (
    calculate_bonus,
    calculate_salary,
    calculate_tax,
    generate_employee_id,
)


def main():
    print("--- Employee Payroll & Identification System ---")
    
    # 1. Generate a new employee ID
    emp_id = generate_employee_id()
    print(f"Generated Employee ID: {emp_id}")
    
    # 2. Set up basic financial details
    base_pay = 5000.00
    perf_score = 5  # Top tier performer
    fixed_deductions = 120.00
    
    # 3. Calculate Bonus based on performance
    bonus_earned = calculate_bonus(performance_score=perf_score, base_salary=base_pay)
    
    # 4. Calculate Tax (applied to gross earnings before other deductions)
    gross_earnings = base_pay + bonus_earned
    tax_withheld = calculate_tax(taxable_income=gross_earnings, tax_rate=0.12)
    
    # 5. Calculate Final Take-Home Net Salary
    # Total deductions include both fixed benefits deductions and taxes
    total_deductions = fixed_deductions + tax_withheld
    net_pay = calculate_salary(base_salary=base_pay, bonus=bonus_earned, deductions=total_deductions)
    
    # Print the Payroll statement summary
    print(f"\n--- Payroll Summary Statement ---")
    print(f"Base Salary:         {base_pay:.2f}")
    print(f"Performance Bonus:  +{bonus_earned:.2f} (Score: {perf_score})")
    print(f"Tax Withheld:       -{tax_withheld:.2f}")
    print(f"Other Deductions:   -{fixed_deductions:.2f}")
    print(f"---------------------------------")
    print(f"Net Take-Home Pay:   {net_pay:.2f}")

if __name__ == "__main__":
    main()