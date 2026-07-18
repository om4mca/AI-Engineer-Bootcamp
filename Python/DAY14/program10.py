
#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Bank class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------



class BankAccount:
    """A class to represent a user's bank account."""

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.holder = account_holder
        # Private attribute to prevent direct, unauthorized modification
        self.__balance = float(initial_balance)

    def deposit(self, amount: float) -> str:
        """Add money to the account."""
        if amount <= 0:
            return "Error: Deposit amount must be positive."
        
        self.__balance += amount
        return f"Deposited ${amount:.2f}. New Balance: ${self.__balance:.2f}"

    def withdraw(self, amount: float) -> str:
        """Subtract money from the account if funds are sufficient."""
        if amount <= 0:
            return "Error: Withdrawal amount must be positive."
        if amount > self.__balance:
            return "Error: Insufficient funds."
        
        self.__balance -= amount
        return f"Withdrew ${amount:.2f}. New Balance: ${self.__balance:.2f}"

    def get_balance(self) -> float:
        """Securely view the current balance."""
        return self.__balance

    def display_account_info(self) -> str:
        """Return account details as a formatted string."""
        return f"Account Holder: {self.holder} | Balance: ${self.__balance:.2f}"


# --- Example Usage ---
if __name__ == "__main__":
    # 1. Create a new account
    my_account = BankAccount("Alice Smith", 500.00)
    print(my_account.display_account_info())

    # 2. Deposit money
    print(my_account.deposit(150.50))

    # 3. Try to withdraw too much cash
    print(my_account.withdraw(1000.00))

    # 4. Successful withdrawal
    print(my_account.withdraw(200.00))
    
    # 5. Direct access protection check
    # Printing my_account.__balance directly here would crash the script (AttributeError)
