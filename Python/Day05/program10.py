# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Fibonacci Series
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------


terms = int(input("How many terms do you want? "))

# First two terms of the series
a, b = 0, 1
count = 0

if terms <= 0:
    print("Please enter a positive integer greater than 0.")
elif terms == 1:
    print(f"Fibonacci series up to {terms} term:")
    print(a)
else:
    print("Fibonacci series:")
    while count < terms:
        print(a, end=" ")
        
        # The Swap Logic: 
        # Calculate the next number and shift the variables forward
        nth = a + b
        a = b
        b = nth
        
        count += 1
    print()  # Moves to a new line at the end


#End of the program