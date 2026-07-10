#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Employee Salary Calculator
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------


def calculate_bonus(basic_salary):
    """Prompts for bonus percent and calculates the bonus amount."""
    try:
        bonus_pct = float(input("Bonus % : "))
        return (bonus_pct / 100) * basic_salary
    except ValueError:
        print("Invalid input. Setting bonus to 0.")
        return 0.0

def calculate_tax(basic_salary, bonus):
    """Prompts for tax percent and calculates tax based on gross salary."""
    try:
        tax_pct = float(input("Tax % : "))
        gross_salary = basic_salary + bonus
        return (tax_pct / 100) * gross_salary
    except ValueError:
        print("Invalid input. Setting tax to 0.")
        return 0.0

def calculate_net_salary(basic_salary, bonus, tax):
    """Calculates final take-home pay."""
    return (basic_salary + bonus) - tax

def print_salary_slip():
    """Handles data collection and prints the finalized salary details."""
    print("--- Employee Salary Calculator ---")
    
    try:
        basic_salary = float(input("Basic Salary : "))
    except ValueError:
        print("Invalid salary entered. Exiting.")
        return

    # Call calculation functions
    bonus = calculate_bonus(basic_salary)
    tax = calculate_tax(basic_salary, bonus)
    net_salary = calculate_net_salary(basic_salary, bonus, tax)
    
    # Print formatted output matching your example structure
    print("-" * 25)
    print(f"Basic Salary : {basic_salary:.2f}")
    print(f"Bonus        : {bonus:.2f}")
    print(f"Tax          : {tax:.2f}")
    print("-" * 25)
    print(f"Net Salary   : {net_salary:.2f}")

if __name__ == "__main__":
    print_salary_slip()

# end of the program    