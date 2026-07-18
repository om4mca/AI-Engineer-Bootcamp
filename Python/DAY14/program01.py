#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: Private Variable
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Account:
    def __init__(self, owner, amount):
        self.owner = owner
        self.__balance = amount  # Private variable

acc = Account("Alice", 1000)
# Attempting direct access will fail
print(acc.__balance)  # Raises AttributeError
