#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Age Verification
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------

from datetime import date

def calculate_age(birth_date: date) -> int:
    """Calculates exact age based on today's date."""
    today = date.today()
    # Subtract 1 if the birthday hasn't occurred yet this year
    has_birthday_passed = (today.month, today.day) < (birth_date.month, birth_date.day)
    return today.year - birth_date.year - has_birthday_passed

def verify_age(required_age: int = 18):
    """Prompts for birthdate, validates input, and verifies age limit."""
    print(f"--- Age Verification System (Required Age: {required_age}+) ---")
    
    while True:
        try:
            # Gather individual inputs to prevent standard formatting typos
            year = int(input("Enter birth year (e.g., 1995): ").strip())
            month = int(input("Enter birth month (1-12): ").strip())
            day = int(input("Enter birth day (1-31): ").strip())
            
            # This handles invalid calendar dates automatically (e.g., June 31st)
            user_birthdate = date(year, month, day)
            
            if user_birthdate > date.today():
                print("Error: Birthdate cannot be in the future. Try again.\n")
                continue
                
            break
        except ValueError:
            print("Invalid input! Please check your dates and enter whole numbers.\n")

    # Final calculation and threshold checks
    user_age = calculate_age(user_birthdate)
    print(f"\nCalculated Age: {user_age} years old.")
    
    if user_age >= required_age:
        print("✅ Access Granted: You meet the age restriction.")
        return True
    else:
        print(f"❌ Access Denied: You must be at least {required_age} years old.")
        return False

if __name__ == "__main__":
    verify_age(required_age=18)



# end of the program