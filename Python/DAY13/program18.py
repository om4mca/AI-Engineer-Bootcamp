#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Encapsulation Demo
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------
class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)