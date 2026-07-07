
# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Prime numbers
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------

number = int(input("Enter Number:- "))

# Prime numbers must be greater than 1
if number > 1:
    is_prime = True
    
    # Check for factors from 2 up to the number itself
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break  # We found a factor, so it's not prime. Stop looping!

    if is_prime:
        print(f"{number} is a Prime Number.")
    else:
        print(f"{number} is NOT a Prime Number.")
        
else:
    print(f"{number} is NOT a Prime Number.")