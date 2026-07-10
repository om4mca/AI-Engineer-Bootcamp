#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Calculator Function
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Handles division by zero gracefully."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator_app():
    """Main terminal interface to run calculations loop."""
    print("=============================")
    print("     SIMPLE PYCALCULATOR     ")
    print("=============================")
    print("Operations: \n1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)")
    print("=============================")
    
    try:
        choice = input("Select operation (1/2/3/4): ").strip()
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid selection. Aborting.")
            return

        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        
        print("-----------------------------")
        
        # Execute the calculation based on user selection
        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {result}")
            
        print("=============================")
        
    except ValueError:
        print("Invalid character input. Please type numbers only.")

# --- EXECUTION ---
if __name__ == "__main__":
    calculator_app()


# end of the program