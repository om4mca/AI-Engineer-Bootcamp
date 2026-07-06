# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program:Blood Donation
# Author: Om Roy
# Date: 06-07-2026
#--------------------------------------------

print("=== Blood Donation Eligibility Check ===")


    # 1. Collect Donor Information
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms (kg): "))
hemoglobin = float(input("Enter your hemoglobin level (g/dL): "))
    
    # 2. Base Validation: Check for realistic numbers
if age <= 0 or weight <= 0 or hemoglobin <= 0:
        print("Error: Input values must be greater than zero.")
else:
        print("\n--- Verifying Medical Criteria ---")
        
        # 3. Check criteria sequentially using if-elif-else
        if age < 18 or age > 65:
            print("Status: NOT ELIGIBLE")
            print("Reason: Donors must be between 18 and 65 years of age.")
            
        elif weight < 50:
            print("Status: NOT ELIGIBLE")
            print("Reason: Minimum weight requirement for donation is 50 kg.")
            
        elif hemoglobin < 12.5:
            print("Status: NOT ELIGIBLE")
            print("Reason: Hemoglobin level is too low. Minimum required is 12.5 g/dL.")
            
        else:
            # If all criteria are successfully met
            print("Status: ELIGIBLE TO DONATE!")
            print("Thank you! You meet all the basic medical requirements to donate blood.")
            print("Please proceed to the registration desk.")


#End of the program