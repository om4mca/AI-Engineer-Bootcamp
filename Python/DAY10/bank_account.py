#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Bank Account Simulator
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------



class InsufficientBalanceError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    pass

class InvalidAmountError(Exception):
    """Raised when an amount is negative or non-numeric."""
    pass


class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.__balance = float(initial_balance)

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise InvalidAmountError("Deposit amount must be greater than zero.")
        except ValueError:
            raise InvalidAmountError("Invalid input. Amount must be a valid number.")
        
        self.__balance += amount
        print(f"\n[Success] Deposited {amount:.2f}")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise InvalidAmountError("Withdrawal amount must be greater than zero.")
        except ValueError:
            raise InvalidAmountError("Invalid input. Amount must be a valid number.")
            
        if amount > self.__balance:
            raise InsufficientBalanceError(
                f"Insufficient funds. Available balance is {self.__balance:.2f}."
            )
            
        self.__balance -= amount
        print(f"\n[Success] Withdrew {amount:.2f}")

    def check_balance(self):
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Current Balance: {self.__balance:.2f}")


def main():
    print("----- Welcome to the Banking Portal -----")
    name = input("Enter your name to open an account: ").strip()
    if not name:
        name = "Valued Customer"
        
    # Initialize the account
    user_account = BankAccount(name, initial_balance=100.0)
    print(f"Account created successfully for {name} with a 100.00 bonus balance!")

    # Interactive Loop Menu
    while True:
        print("\n" + "="*30)
        print("          MAIN MENU")
        print("="*30)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Log Out")
        print("="*30)
        
        choice = input("Select an option (1-4): ").strip()

        try:
            if choice == "1":
                user_account.check_balance()
                
            elif choice == "2":
                amount_input = input("Enter deposit amount: ")
                user_account.deposit(amount_input)
                user_account.check_balance()
                
            elif choice == "3":
                amount_input = input("Enter withdrawal amount: ")
                user_account.withdraw(amount_input)
                user_account.check_balance()
                
            elif choice == "4":
                print(f"\nThank you for banking with us, {name}. Goodbye!")
                break
                
            else:
                print("\n[Invalid Selection] Please choose a valid option from 1 to 4.")
                
        except (InvalidAmountError, InsufficientBalanceError) as e:
            # Safely catch transaction errors, inform the user, and keep the menu looping
            print(f"\n[Transaction Denied]: {e}")
            
        except Exception as e:
            # Catch-all for unexpected edge cases to prevent app crashes
            print(f"\n[An unexpected error occurred]: {e}")


if __name__ == "__main__":
    main()



# end of the program