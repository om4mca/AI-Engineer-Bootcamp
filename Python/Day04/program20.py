# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program:Cinema Ticket Eligibility
# Author: Om Roy
# Date: 06-07-2026
#--------------------------------------------


print("=== Cinema Ticket Eligibility & Pricing ===")

# Standard Ticket Base Price: 120.00
base_price = 120.00


    # 1. Collect user age
age = int(input("Enter your age: "))
    
    # 2. Base Validation: Check for a realistic age
if age <= 0 or age > 120:
        print("Error: Please enter a valid, realistic age.")
else:
        print("\n--- Processing Ticket Eligibility ---")
        
        # 3. Determine movie rating eligibility and ticket pricing using if-elif-else
        if age < 13:
            ticket_price = base_price * 0.50  # 50% discount for children
            print("Allowed Ratings: G and PG movies only.")
            print("Note: Access to PG-13 and R-rated movies is restricted.")
            category = "Child"
            
        elif age < 17:
            ticket_price = base_price * 0.80  # 20% discount for teens
            print("Allowed Ratings: G, PG, and PG-13 movies.")
            print("Note: Access to R-rated movies requires an adult guardian.")
            category = "Teenager"
            
        elif age < 60:
            ticket_price = base_price          # Full price for adults
            print("Allowed Ratings: All movies (G, PG, PG-13, and R).")
            category = "Adult"
            
        else:
            ticket_price = base_price * 0.70  # 30% discount for seniors
            print("Allowed Ratings: All movies (G, PG, PG-13, and R).")
            category = "Senior Citizen"
            
        # 4. Display the Receipt Summary
        print("\n--- Ticket Receipt ---")
        print(f"Age Category:  {category}")
        print(f"Ticket Price:  {ticket_price:.2f}")

