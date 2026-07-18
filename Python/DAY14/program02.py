#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: Getter Method
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class BankAccount:
    def __init__(self, owner, amount):
        self._owner = owner
        self._balance = amount  # Protected variable

    @property
    def balance(self):
        """Getter method to view the balance securely."""
        # You can add logging or audit checks here
        print("Log: Balance accessed by {self._owner}")
        return self._balance

# Usage
account = BankAccount("Alice", 5000)

# Accessing the getter (Notice: No parentheses () used)
print(account.balance)  # Outputs: 5000

