# AI Engineer Bootcamp
# Day 8
# Program: Hospital Billing Calculator
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------



def calculate_consultation():
    """Prompts for and returns the consultation fee."""
    try:
        fee = float(input("Consultation : "))
        return fee
    except ValueError:
        print("Invalid input. Setting consultation fee to 0.")
        return 0.0

def calculate_medicine():
    """Prompts for and returns the medicine cost."""
    try:
        cost = float(input("Medicine : "))
        return cost
    except ValueError:
        print("Invalid input. Setting medicine cost to 0.")
        return 0.0

def calculate_lab():
    """Prompts for and returns the lab test cost."""
    try:
        cost = float(input("Lab : "))
        return cost
    except ValueError:
        print("Invalid input. Setting lab cost to 0.")
        return 0.0

def calculate_total(consultation, medicine, lab):
    """Calculates the sum of all medical expenses."""
    return consultation + medicine + lab

def print_bill():
    """Handles the user input sequence and prints the final formatted bill."""
    print("--- Hospital Billing System ---")
    patient_name = input("Patient Name : ")
    
    # Gather costs using the respective functions
    consultation_fee = calculate_consultation()
    medicine_cost = calculate_medicine()
    lab_cost = calculate_lab()
    
    # Calculate total
    total_amount = calculate_total(consultation_fee, medicine_cost, lab_cost)
    
    # Print the formatted statement
    print("-" * 20)
    print(f"Total : {total_amount:.0f}")

# This ensures the program runs when you execute the script directly
if __name__ == "__main__":
    print_bill()

#end of the program