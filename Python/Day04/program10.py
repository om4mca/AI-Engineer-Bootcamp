# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: Simple Calculator
# Author: Om Roy
# Date: 06-07-2026
# ------------------------------------------

print("--- Simple Python Calculator ---")
print("Choose an operation:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")

# Take input from the user
operation = input("Enter operator (+, -, *, /): ").strip()

# Check if the user entered a valid operator before asking for numbers
if operation in ('+', '-', '*', '/'):
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform calculation based on the operator using if-elif-else
        if operation == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
            
        elif operation == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
            
        elif operation == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
            
        elif operation == '/':
            # Check for division by zero
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
else:
    print("Invalid operator! Please run the program again and choose +, -, *, or /.")


#End of the program