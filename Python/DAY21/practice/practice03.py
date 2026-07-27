
#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Class + List
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------


class ShoppingCart:
    def __init__(self):
        self.items = []  # List initialized inside the class

    def add_item(self, item_name, price):
        self.items.append({"name": item_name, "price": price})

    def get_total(self):
        return sum(item["price"] for item in self.items)

cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 25.00)

print(cart.get_total())  