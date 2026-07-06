# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: ATM Withdrawal
# Author: Om Roy
# Date: 06-07-2026
# ------------------------------------------

print("----------- Welcome to the ATM-------------")

# Simulated bank data (Starting balance and correct PIN)
account_balance = 20000.0
correct_pin = "1234"

# 1. Ask the user for their PIN
user_pin = input("Enter your 4-digit PIN: ")

# 2. Authenticate the PIN
if user_pin != correct_pin:
    print("Error: Invalid PIN. Access Denied.")
else:
    # 3. If PIN is correct, proceed to the withdrawal step
    print(f"Login Successful! Your current balance is: ${account_balance}")
    withdraw_amount = float(input("Enter the amount to withdraw: $"))
    
    # 4. Validate the withdrawal amount
    if withdraw_amount <= 0:
        print("Error: Amount must be greater than 0.")
    elif withdraw_amount > account_balance:
        print("Error: Insufficient balance. You do not have enough funds.")
    else:
        # 5. Deduct the money and update the balance
        account_balance -= withdraw_amount
        
        print("\n--- Transaction Successful ---")
        print(f"Please collect your cash: ${withdraw_amount}")
        print(f"Remaining Balance: ${account_balance:.2f}")

print("\nThank you for using our ATM service!")


#End of the program