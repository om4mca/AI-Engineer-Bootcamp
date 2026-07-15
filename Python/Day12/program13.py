#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: ATM Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class ATM:
    def __init__(self, pin: str, initial_balance: float = 0.0):
        """Initializes the ATM object with a security PIN and opening balance."""
        self.__pin = pin  # Encapsulated (private) attribute
        self.__balance = initial_balance

    def check_balance(self, entered_pin: str) -> str:
        """Verifies identity and returns the current balance."""
        if not self.__verify_pin(entered_pin):
            return "Error: Incorrect PIN. Access Denied."
        return f"Current Balance: {self.__balance:.2f}"

    def deposit(self, amount: float) -> str:
        """Adds verified funds to the balance."""
        if amount <= 0:
            return "Error: Deposit amount must be positive."
        self.__balance += amount
        return f"Successfully deposited {amount:.2f}. New Balance: {self.__balance:.2f}"

    def withdraw(self, amount: float, entered_pin: str) -> str:
        """Verifies identity, checks liquidity, and deducts funds."""
        if not self.__verify_pin(entered_pin):
            return "Error: Incorrect PIN. Access Denied."
        if amount <= 0:
            return "Error: Withdrawal amount must be positive."
        if amount > self.__balance:
            return "Error: Insufficient funds available."
            
        self.__balance -= amount
        return f"Successfully withdrew {amount:.2f}. Remaining Balance: {self.__balance:.2f}"

    def change_pin(self, old_pin: str, new_pin: str) -> str:
        """Validates old security pin and modifies it to a new value."""
        if not self.__verify_pin(old_pin):
            return "Error: Incorrect original PIN."
        if len(new_pin) < 4:
            return "Error: New PIN must be at least 4 characters long."
        self.__pin = new_pin
        return "PIN successfully updated."

    def __verify_pin(self, entered_pin: str) -> bool:
        """Private helper logic to centralize security verification."""
        return self.__pin == entered_pin


# 1. Instantiate the machine with a default configuration
my_atm = ATM(pin="1234", initial_balance=500.0)

# 2. Add cash
print(my_atm.deposit(250.50))
# Output: Successfully deposited 250.50. New Balance: 750.50

# 3. Attempt withdrawal with correct validation
print(my_atm.withdraw(100.0, entered_pin="1234"))
# Output: Successfully withdrew 100.00. Remaining Balance: 650.50

# 4. Attempt withdrawal with faulty validation
print(my_atm.withdraw(50.0, entered_pin="9999"))
# Output: Error: Incorrect PIN. Access Denied.
