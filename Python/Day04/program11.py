# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: Bonus Eligibility
# Author: Om Roy
# Date: 06-07-2026
# ------------------------------------------

# Step 1: Accept user inputs
salary = float(input("Enter base monthly salary: "))
years_of_service = int(input("Enter total years of service: "))

# Step 2: Establish the conditional rules
if years_of_service > 5:
    bonus_percentage = 0.10  # 10% bonus for seasoned staff
elif years_of_service >= 3:
    bonus_percentage = 0.05  # 5% bonus for mid-tier staff
else:
    bonus_percentage = 0.02  # 2% baseline bonus

# Step 3: Compute calculations
bonus_amount = salary * bonus_percentage
total_salary = salary + bonus_amount

# Step 4: Display the breakdown
print(f"\n--- Salary Breakdown ---")
print(f"Base Salary:    ${salary:,.2f}")
print(f"Bonus Rate:     {bonus_percentage * 100}%")
print(f"Bonus Payout:   ${bonus_amount:,.2f}")
print(f"Total Net Pay:  ${total_salary:,.2f}")
 


#End of the program.