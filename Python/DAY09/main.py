#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Import Module
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import calculator

print(calculator.add(10,20))
print(calculator.subtract(50,30))

# Import Specific Function
print()
print("************Import Specific Function**********")
from calculator import add
print(add(20,30))


# Alias
print()
print("************Alias**********")
import calculator as calc
print(calc.add(90,30))

# Built-in Modules
print()
print("************Built-in Modules - math**********")

import math

print(math.sqrt(256))
print(math.pi)
print(math.factorial(6))

import random
print()
print("**********Random**********")
print(random.randint(1,100))

print()
print("**********datetime************")
from datetime import datetime

print(datetime.now())



from hospital.billing import calculate_total

print(calculate_total(500, 1200))



# Importing all functions from the utility module
from hospital_utils import calculate_age, calculate_bill, current_date, generate_patient_id


def main():
    print("--- Hospital Management System Simulation ---")
    
    # 1. Generate a new patient ID
    patient_id = generate_patient_id()
    print(f"Generated Patient ID: {patient_id}")
    
    # 2. Get current system date
    today = current_date()
    print(f"Current Date: {today}")
    
    # 3. Calculate Patient Age (Assuming a DOB of March 15, 1994)
    dob = "1994-03-15"
    age = calculate_age(dob)
    print(f"Patient DOB: {dob} | Calculated Age: {age} years old")
    
    # 4. Calculate Bill
    # Example: $500.00 base cost, 5% standard tax (default), and a $25.00 insurance discount
    base_cost = 500.00
    insurance_discount = 25.00
    total_bill = calculate_bill(base_charge=base_cost, discount=insurance_discount)
    
    print(f"\n--- Billing Breakdown ---")
    print(f"Base Treatment Charge: {base_cost:.2f}")
    print(f"Insurance Discount:   -{insurance_discount:.2f}")
    print(f"Total Amount Due:      {total_bill:.2f}")

if __name__ == "__main__":
    main()


    from hospital.billing import calculate_total

print(calculate_total(500, 1200))
#end of the program