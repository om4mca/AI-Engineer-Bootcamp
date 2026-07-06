

# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: Age Category
# Author: Om Roy
# Date: 06-07-2026
# ------------------------------------------


age = int(input("Enter your age: "))


if age < 0:
    print("❌ Error: Age cannot be negative.")
else:
    
    if age <= 2:
        category = "Infant"
    elif age <= 12:
        category = "Child"
    elif age <= 19:
        category = "Teenager"
    elif age <= 65:
        category = "Adult"
    else:
        category = "Senior Citizen"

    
    print("\n--- Results ---")
    print(f"Age: {age} years")
    print(f"Age Category: {category}")