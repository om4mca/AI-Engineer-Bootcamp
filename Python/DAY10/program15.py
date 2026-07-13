#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Login Retry
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------

MAX_ATTEMPTS = 3
CORRECT_USER = "admin"
CORRECT_PASS = "admin123"

attempts = 0

while attempts < MAX_ATTEMPTS:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == CORRECT_USER and password == CORRECT_PASS:
        print("Access Granted!")
        break  # Exit loop immediately on success
    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        print(f"Invalid credentials. Attempts remaining: {remaining}\n")
else:
    # This executes ONLY if the loop finishes without hitting 'break'
    print("Locked Out. Too many failed attempts.")


# end of the program