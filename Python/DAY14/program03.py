#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: Setter Method
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------
class Product:
    def __init__(self, name, price):
        self.name = name
        self.set_price(price) # Uses the setter to establish initial value securely

    # Getter: Allows safe reading of the private variable
    def get_price(self):
        return self.__price

    # Setter: Validates data before altering the private variable
    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("[Validation Error] Price cannot be negative! Operation denied.")