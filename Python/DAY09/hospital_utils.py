#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Mini Project Hospital Utility Library
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import uuid
from datetime import date, datetime

def generate_patient_id() -> str:
    """Generates a unique 8-character alphanumeric patient ID."""
    return f"PAT-{str(uuid.uuid4())[:8].upper()}"

def calculate_age(dob: str) -> int:
    """
    Calculates age based on date of birth.
    Expects dob string format: 'YYYY-MM-DD'
    """
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
        today = date.today()
        # Adjusted for whether the birthday has occurred yet this year
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

def calculate_bill(base_charge: float, tax_rate: float = 0.05, discount: float = 0.0) -> float:
    """
    Calculates the final hospital bill after adding tax and applying any discounts.
    """
    if base_charge < 0 or tax_rate < 0 or discount < 0:
        raise ValueError("Charges, tax rates, and discounts cannot be negative.")
        
    tax_amount = base_charge * tax_rate
    final_bill = (base_charge + tax_amount) - discount
    return max(0.0, round(final_bill, 2))  # Prevents a negative bill

def current_date() -> str:
    """Returns today's date formatted as standard YYYY-MM-DD."""
    return date.today().strftime("%Y-%m-%d")