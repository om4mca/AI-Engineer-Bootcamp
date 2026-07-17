#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Bank → Current
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

# banking_current.py

class BankAccount:
    """Base class representing a generic bank account."""
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        """Standard deposit logic shared by all accounts."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount:.2f} into Account {self.account_number}")
        else:
            print("Deposit amount must be greater than zero.")

    def check_balance(self):
        """Displays the account balance."""
        print(f"Account: {self.account_number} | Holder: {self.account_holder} | Balance: {self.balance:.2f}")


class CurrentAccount(BankAccount):
    """Child class representing a Current/Business Account with an overdraft limit."""
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0, overdraft_limit: float = 500.0):
        # Initialize basic banking attributes via parent class
        super().__init__(account_number, account_holder, balance)
        # Unique attribute specific only to current accounts
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        """
        Overrides the standard withdrawal process.
        Allows the balance to drop below 0.00 up to the designated overdraft limit.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        # Total available liquidity = Current Balance + Overdraft Limit Room
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"[Current] Withdrew: {amount:.2f}. New Balance: {self.balance:.2f}")
            return True
        else:
            print(f"[Transaction Denied] Exceeds overdraft limit of {self.overdraft_limit:.2f}")
            return False


# --- Demonstration ---
if __name__ == "__main__":
    # Create a Current Account with a starting balance of 200 and a default 500 overdraft pool
    business_acc = CurrentAccount(account_number="CUR-8821", account_holder="Om Roy", balance=200.0)
    
    business_acc.check_balance() # Balance: 200.00
    
    # 1. Withdraw more than the current balance (Uses 150 of the overdraft cushion)
    business_acc.withdraw(350.0) 
    business_acc.check_balance() # Balance: -150.00
    
    # 2. Attempting a withdrawal that exceeds the remaining overdraft capability
    business_acc.withdraw(400.0) # Denied! (Remaining limit is 350, needs 400)
    
    # 3. Pay back into the account to clear the overdraft deficit
    business_acc.deposit(500.0)
    business_acc.check_balance() # Balance: 350.00