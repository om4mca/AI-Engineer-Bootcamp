# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: Loan Approval
# Author: Om Roy
# Date: 06-07-2026
# ------------------------------------------

print("------------Loan Approval Eligibility System-------------")

# 1. Collect Applicant Information
try:
    age = int(input("Enter your age: "))
    income = float(input("Enter your monthly income (e.g., 35000)"))
    credit_score = int(input("Enter your credit score (300 - 850): "))
    
    # 2. Base Validation: Ensure inputs are realistic
    if age <= 0 or income < 0 or credit_score < 300 or credit_score > 850:
        print("Error: Invalid input values. Please check your data and try again.")
    else:
        print("\n--- Processing Application ---")
        
        # 3. Check Eligibility Criteria using Nested Conditions
        if age < 18:
            print("Status: Denied")
            print("Reason: Applicant must be at least 18 years old.")
            
        elif income < 2500:
            print("Status: Denied")
            print("Reason: Minimum monthly income required is $2,500.")
            
        elif credit_score < 650:
            print("Status: Denied")
            print("Reason: Credit score is too low. Minimum required is 650.")
            
        else:
            # If all criteria are met, the loan is approved
            print("Status: APPROVED!")
            print("Congratulations! You meet all the eligibility requirements.")
            
            # Offer a loan amount based on income level
            max_loan = income * 15
            print(f"Based on your income, you qualify for a loan up to: {max_loan:,.2f}")

except ValueError:
    print("Error: Please enter numbers only.")

print("\nThank you for applying with us.")