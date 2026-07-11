# Import the custom AdvancedCalculator class explicitly from our module
from calculator_mod import AdvancedCalculator


def main():
    print("=== Core Engineering Calculator Active ===")
    calc = AdvancedCalculator()
    
    # 1. Execute standard linear arithmetic operations
    print(f"Addition:       {calc.add(10.5, 4.5)}")
    print(f"Multiplication: {calc.multiply(12, 12)}")
    
    # 2. Execute advanced mathematical library integrations
    print(f"Square Root:    {calc.square_root(144)}")
    print(f"Factorial (5!): {calc.factorial(5)}")
    
    # 3. Demonstrate runtime exception handling safeguards
    print("\n--- Testing Operational Guardrails ---")
    try:
        calc.divide(25, 0)
    except ZeroDivisionError as e:
        print(f"Caught Safe Exception: {e}")
        
    try:
        calc.square_root(-9)
    except ValueError as e:
        print(f"Caught Safe Exception: {e}")

    # 4. Display internal processing history logs
    print("\n=== Calculator Transaction Audit Logs ===")
    for log in calc.get_history():
        print(f"[{log['timestamp']}] {log['operation']}: {log['expression']} = {log['result']}")
        
    print("=========================================")

if __name__ == "__main__":
    main()