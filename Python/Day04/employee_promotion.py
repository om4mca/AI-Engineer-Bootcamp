# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program:Employee Promotion
# Author: Om Roy
# Date: 06-07-2026
#--------------------------------------------

# 1. Take inputs from the user
employee_name = input("Enter Employee Name: ")
experience = float(input("Enter Experience (in years): "))
rating = float(input("Enter Rating (e.g., 1 to 5): "))

# 2. Check conditions using if-else
if experience >= 5 and rating >= 4:
    result = "Promotion"
else:
    result = "Not Eligible"

# 3. Print the formatted output table
print("\n" + "=" * 52)
print(f"{'Employee Name':<15} | {'Experience':<10} | {'Rating':<6} | {'Result'}")
print("-" * 52)
print(f"{employee_name:<15} | {experience:<10} | {rating:<6} | {result}")
print("=" * 52)


#End of the program