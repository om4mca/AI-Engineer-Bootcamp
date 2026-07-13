#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: ATM PIN Validation
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------


def atm_login_system():
    CORRECT_PIN = "4321"  # Stored as a string to handle leading zeros safely
    max_attempts = 3
    attempts = 0

    print("=== Welcome to the Python ATM ===")

    while attempts < max_attempts:
        # Prompt user for input
        entered_pin = input("Please enter your 4-digit PIN: ").strip()

        # Step 1: Validate format first
        if not (len(entered_pin) == 4 and entered_pin.isdigit()):
            print("❌ Invalid format. The PIN must be exactly 4 digits long.\n")
            continue

        # Step 2: Check matching credentials
        if entered_pin == CORRECT_PIN:
            print("\n✅ Access Granted. Welcome to your account!")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"❌ Incorrect PIN. You have {remaining} attempts left.\n")
            else:
                print("\n🚨 Account Locked. Too many incorrect attempts. Please contact customer support.")
                return False

# Execute simulation
atm_login_system()



# end of the program     