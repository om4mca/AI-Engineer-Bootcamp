# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program:Discount Calculator
# Author: Om Roy
# Date: 06-07-2026
# ------------------------------------------

total_amount = float(input("Enter the total shopping bill amount : "))

    # 2. Check for invalid negative or zero values
if total_amount <= 0:
        print("Error: The bill amount must be greater than 0.")
else:
# 3. Apply conditional logic to determine the discount percentage
    if total_amount < 100:
            discount_percentage = 0     # 0% discount for bills under $100
    elif total_amount <= 500:
            discount_percentage = 10    # 10% discount for bills between $100 and $500
    elif total_amount <= 1000:
            discount_percentage = 20    # 20% discount for bills between $501 and $1000
    else:
            discount_percentage = 30    # 30% discount for bills over $1000

        # 4. Perform math operations to get final prices
discount_amount = (discount_percentage / 100) * total_amount
final_bill = total_amount - discount_amount

        # 5. Display the calculation breakdown
print(f"\n--- Invoice Breakdown ---")
print(f"Original Bill:   {total_amount:.2f}")
print(f"Discount Rate:   {discount_percentage}%")
print(f"Saved Amount:    {discount_amount:.2f}")
print(f"Final Amount:    {final_bill:.2f}")



#End of the program