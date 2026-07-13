#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Calculator with Exception Handling
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------

def calculator():
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            op = input("Enter operator (+, -, *, /) or 'exit': ").strip()
            if op.lower() == 'exit': break
            num2 = float(input("Enter second number: "))
            
            if op == '+': print(f"Result: {num1 + num2}")
            elif op == '-': print(f"Result: {num1 - num2}")
            elif op == '*': print(f"Result: {num1 * num2}")
            elif op == '/': print(f"Result: {num1 / num2}")
            else: print("Invalid operator.")
        except ValueError:
            print("Error: Invalid numeric input.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    calculator()
