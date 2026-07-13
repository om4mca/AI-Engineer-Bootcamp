#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Bank Withdrawal
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------


class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        # Using a private attribute to protect the balance from direct external changes
        self.__balance = initial_balance 

    def get_balance(self) -> float:
        """Returns the current balance safely."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited {amount:.2f}. New Balance: {self.__balance:.2f}")
        else:
            print("⚠️ Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        """Withdraws a validated amount from the account balance."""
        # Condition 1: Check if the transaction amount is valid
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than zero.")
            return
        
        # Condition 2: Check for sufficient funds
        if amount > self.__balance:
            print(f"❌ Insufficient funds. Current Balance: {self.__balance:.2f}")
            return
        
        # Execution of the withdrawal
        self.__balance -= amount
        print(f"💸 Successfully withdrew {amount:.2f}. Remaining Balance: {self.__balance:.2f}")


# --- Example Execution ---
if __name__ == "__main__":
    # Initialize an account with 500
    account = BankAccount("Om", 500.0)
    print(f"Account Holder: {account.owner} | Initial Balance: {account.get_balance():.2f}")

    # 1. Test a successful withdrawal
    account.withdraw(150.0)

    # 2. Test an invalid withdrawal amount
    account.withdraw(-20.0)

    # 3. Test an overdraft attempt
    account.withdraw(400.0)



# end of the program