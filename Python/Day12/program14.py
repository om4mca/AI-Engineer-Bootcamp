#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Product Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------
class Product:
    def __init__(self, product_id: int, name: str, price: float, quantity: int = 0):
        """Initializes the structural attributes of a product."""
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_stock_value(self) -> float:
        """Returns the total financial value of the current stock."""
        return self.price * self.quantity

    def update_stock(self, amount: int):
        """Modifies stock inventory (Positive to restock, negative for sales)."""
        if self.quantity + amount < 0:
            raise ValueError("Operation failed: Stock balance cannot drop below zero.")
        self.quantity += amount

    def __str__(self) -> str:
        """Returns a clean, human-readable string representation of the object."""
        return f"{self.name} (ID: {self.product_id}) - {self.price:.2f} | Stock: {self.quantity}"
# 1. Create instances (objects) of the Product class
laptop = Product(product_id=101, name="ThinkPad L14", price=950.00, quantity=12)
mouse = Product(product_id=102, name="Logitech MX Master", price=99.99, quantity=45)

# 2. Access variables and execute behaviors
print(laptop)  
# Output: ThinkPad L14 (ID: 101) - 950.00 | Stock: 12

print(f"Total Mouse Value: {mouse.calculate_stock_value():.2f}")  
# Output: Total Mouse Value: 4499.55

# 3. Modify state dynamically via methods
laptop.update_stock(-2)  # Sell 2 laptops
print(f"Updated {laptop.name} stock: {laptop.quantity}")  
# Output: Updated ThinkPad L14 stock: 10
