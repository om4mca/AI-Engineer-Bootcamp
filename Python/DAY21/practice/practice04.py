
#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Class + Exception
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

class InsufficientFundsError(Exception):
    """Raised when an account balance is too low for a withdrawal."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        # Pass a descriptive error message to the parent Exception class
        super().__init__(f"Cannot withdraw {amount}. Current balance: {balance}")

# Usage
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(50, 100)
except InsufficientFundsError as e:
    print(e)  