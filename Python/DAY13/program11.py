#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Bank → Savings
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------


class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. New Balance: ₹{self.balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f}. New Balance: ₹{self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, initial_balance=0.0, minimum_balance=1000.0, interest_rate=0.035):
        super().__init__(account_holder, account_number, initial_balance)
        self.minimum_balance = minimum_balance
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        print(f"Interest of ₹{interest_earned:.2f} applied! New Balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        # Enforce minimum balance restriction for savings accounts
        if self.balance - amount < self.minimum_balance:
            print(f"Withdrawal denied. You must maintain a minimum balance of ₹{self.minimum_balance:.2f}.")
        else:
            super().withdraw(amount)

# --- Example Usage ---
my_savings = SavingsAccount("Rahul Sharma", "1234567890", initial_balance=5000.0)
my_savings.deposit(2000.0)
my_savings.apply_interest()
my_savings.withdraw(4500.0)
