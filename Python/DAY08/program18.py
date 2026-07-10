#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Hospital Bill Function
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

def generate_hospital_bill(patient_name, patient_type, days_stayed, doctor_fee, medicine_total):
    """
    Calculates and prints a detailed hospital invoice.
    Accepts 'inpatient' or 'outpatient' patient types.
    """
    # 1. Base Configurations
    ROOM_RATE_PER_DAY = 1500.00
    TAX_RATE = 0.05  # 5% service tax
    
    # 2. Calculate Room Charges
    if patient_type.lower() == "inpatient":
        room_charges = ROOM_RATE_PER_DAY * days_stayed
    else:
        room_charges = 0.00
        days_stayed = 0  # Force zero if outpatient
        
    # 3. Summing Up the Totals
    subtotal = room_charges + doctor_fee + medicine_total
    tax_amount = subtotal * TAX_RATE
    grand_total = subtotal + tax_amount
    
    # 4. Format and Print the Invoice
    print("\n" + "="*40)
    print(f"{'SUM HOSPITAL RECEIPT':^40}")
    print("="*40)
    print(f"Patient Name : {patient_name}")
    print(f"Patient Type : {patient_type.capitalize()}")
    print(f"Days Stayed  : {days_stayed}")
    print("-"*40)
    print(f"Room Charges ({days_stayed} days) : {room_charges:,.2f}")
    print(f"Doctor/Consultant Fee: {doctor_fee:,.2f}")
    print(f"Pharmacy/Medications : {medicine_total:,.2f}")
    print("-"*40)
    print(f"Subtotal             : {subtotal:,.2f}")
    print(f"Service Tax (5%)     : {tax_amount:,.2f}")
    print("="*40)
    print(f"GRAND TOTAL DUE      : {grand_total:,.2f}")
    print("="*40)
    
    return grand_total

# --- Demonstration ---
# Inpatient example (Stayed 4 days)
generate_hospital_bill("Sudhakar Kumar", "inpatient", days_stayed=4, doctor_fee=2500, medicine_total=850)

# Outpatient example (No stay)
generate_hospital_bill("Rajeev Ranjan", "outpatient", days_stayed=0, doctor_fee=1200, medicine_total=300)




# end of the program