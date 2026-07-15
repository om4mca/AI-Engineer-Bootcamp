#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Bank Account Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to the Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance")

    def display(self):
        print("\nNet Available Balance =", self.balance)


# Driver code
if __name__ == "__main__":
    s = BankAccount()  # Create an object of BankAccount

    s.deposit()        # Deposit money
    s.withdraw()       # Withdraw money
    s.display()        # Display balance1000