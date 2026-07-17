#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Banking System
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------



class Account:
    """Base class representing a generic bank account."""
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        """Adds money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount:.2f} into Account {self.account_number}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount: float):
        """Basic withdrawal mechanism (to be overridden by subclasses)."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False
        
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: {amount:.2f} from Account {self.account_number}")
            return True
        else:
            print(f"Insufficient funds in Account {self.account_number}")
            return False

    def check_balance(self):
        """Displays the current balance."""
        print(f"Account: {self.account_number} | Holder: {self.account_holder} | Balance: {self.balance:.2f}")
        return self.balance


class SavingsAccount(Account):
    """Subclass representing a Savings Account with a minimum balance rule."""
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0, min_balance: float = 100.0):
        super().__init__(account_number, account_holder, balance)
        self.min_balance = min_balance

    def withdraw(self, amount: float):
        """
        Overrides the base withdraw method.
        Prevents withdrawal if it drops the balance below the minimum limit.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            print(f"[Savings] Withdrew: {amount:.2f}. New Balance: {self.balance:.2f}")
            return True
        else:
            print(f"[Transaction Denied] Savings Account {self.account_number} must maintain a minimum balance of {self.min_balance:.2f}")
            return False


class CurrentAccount(Account):
    """Subclass representing a Business/Current Account with an overdraft allowance."""
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        """
        Overrides the base withdraw method.
        Allows the balance to go negative up to the specified overdraft limit.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        # Total available funds include the balance plus the allowed overdraft room
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"[Current] Withdrew: {amount:.2f}. New Balance: {self.balance:.2f}")
            return True
        else:
            print(f"[Transaction Denied] Exceeds overdraft limit of {self.overdraft_limit:.2f} on Account {self.account_number}")
            return False


# --- Demonstration of the Banking System ---
if __name__ == "__main__":
    print("=== Opening Bank Accounts ===")
    # Create a Savings Account (Min Balance: 100)
    sav_acc = SavingsAccount(account_number="SAV-4001", account_holder="Om Roy", balance=500.0)
    
    # Create a Current Account (Overdraft Limit: 500)
    cur_acc = CurrentAccount(account_number="CUR-9002", account_holder="Sudhir Kumar", balance=200.0)

    sav_acc.check_balance()
    cur_acc.check_balance()
    print("-" * 40)

    print("\n=== Testing Savings Account Rules ===")
    sav_acc.deposit(150.0)
    # Trying to withdraw too much (500 + 150 = 650. 650 - 600 = 50, which is below the 100 min balance)
    sav_acc.withdraw(600.0) 
    # Safe withdrawal
    sav_acc.withdraw(400.0)
    sav_acc.check_balance()
    print("-" * 40)

    print("\n=== Testing Current Account Rules ===")
    # Withdrawing more than the balance (200), using the overdraft facility
    cur_acc.withdraw(450.0)  # Leaves balance at -250.00 (within 500 limit)
    # Trying to exceed the remaining overdraft
    cur_acc.withdraw(300.0)  
    cur_acc.deposit(400.0)   # Settles the negative balance back to positive
    cur_acc.check_balance()