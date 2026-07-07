# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: ATM PIN Verification
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------

# Set the correct 4-digit ATM PIN and attempt counter
CORRECT_PIN = "5521"
attempts_left = 3

print("-------- WELCOME TO THE HDFC BANK ATM -------")

while attempts_left > 0:
    # Read the PIN as a string to preserve leading zeros (like 0072)
    user_pin = input("Enter your 4-Digit PIN: ")
    
    if user_pin == CORRECT_PIN:
        print("\n PIN Verified Successfully!")
        print("Please choose your transaction: [1] Withdraw  [2] Deposit  [3] Balance")
        break  # Exit the loop immediately
    else:
        attempts_left -= 1
        print(" Invalid PIN Code.")
        
        if attempts_left > 0:
            print(f"You have {attempts_left} attempts remaining.\n")
        else:
            print("\n CARD BLOCKED! You have exceeded the maximum of 3 attempts.")
            print("Please contact your branch customer care for assistance.")

#End of the program