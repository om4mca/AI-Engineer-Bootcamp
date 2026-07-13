#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Hospital Registration System
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------


import sys

def register_patient():
    print("-------- Hospital Patient Registration ------")
    
    try:
        # 1. Inputs
        name = input("Enter Patient Name: ").strip()
        if not name:
            raise ValueError("Patient name cannot be empty.")
            
        age = int(input("Enter Age: "))
        mobile = input("Enter Mobile Number: ").strip()
        fee = float(input("Enter Consultation Fee : "))
        
        # 2. Validations
        if age <= 0:
            raise ValueError("Age must be a positive number.")
            
        if len(mobile) != 10 or not mobile.isdigit():
            raise ValueError("Mobile number must contain exactly 10 digits.")
            
        if fee < 0:
            raise ValueError("Consultation fee cannot be negative.")
            
    except ValueError as e:
       
        print(f"\n[Registration Error]: {e}")
        
    else:
        
        print("\n-----Registration Successful!-------------")
        print(f"Patient Name : {name}")
        print(f"Age          : {age}")
        print(f"Mobile No    : {mobile}")
        print(f"Fee Paid     : {fee:.2f}")
        
    finally:
        # Always runs, no matter what happened above
        print("=====================================")
        print("Thank you for using the Registration System.\n")

if __name__ == "__main__":
    register_patient()

# end of the program    