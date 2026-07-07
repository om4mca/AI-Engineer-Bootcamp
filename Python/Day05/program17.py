# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Password Retry (Maximum 3 attempts)
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------


# Set the correct password and the limit tracker
CORRECT_PASSWORD = "SecretPython123"
max_attempts = 3
attempts_left = max_attempts

print("--- System Login ---")

while attempts_left > 0:
    user_guess = input("Enter Password: ")
    
    if user_guess == CORRECT_PASSWORD:
        print(" Access Granted! Welcome back.")
        break  # Exit the loop immediately on success
    else:
        attempts_left -= 1
        print(f" Incorrect password.")
        
        if attempts_left > 0:
            print(f"Remaining attempts: {attempts_left}\n")
        else:
            print("\n Access Denied! You have been locked out after 3 failed attempts.")

#End of the program