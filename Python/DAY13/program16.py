#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Product → Laptop
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------



class Product:
    """Base class representing a generic retail product."""
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display_details(self):
        """Displays standard inventory information."""
        print(f"Product ID : {self.product_id}")
        print(f"Item Name  : {self.name}")
        print(f"Price      : {self.price:.2f}")
        print(f"In Stock   : {self.stock} units")

    def update_stock(self, quantity: int):
        """Adjusts inventory counts (positive for restock, negative for sales)."""
        new_stock = self.stock + quantity
        if new_stock >= 0:
            self.stock = new_stock
            print(f"[Stock Update] {self.name} inventory changed by {quantity}. Current: {self.stock}")
            return True
        else:
            print(f"[Stock Error] Insufficient stock to process sale of {abs(quantity)} units.")
            return False


class Laptop(Product):
    """Child class specializing in notebook/laptop hardware systems."""
    def __init__(self, product_id: str, name: str, price: float, stock: int, 
                 processor: str, ram_gb: int, battery_hours: int):
        # Route generic product properties directly up to parent initializer
        super().__init__(product_id, name, price, stock)
        # Capture specialized computing attributes
        self.processor = processor
        self.ram_gb = ram_gb
        self.battery_hours = battery_hours

    def display_details(self):
        """Overrides parent method to layer computer hardware specs over basic retail info."""
        print(r"=== Laptop Hardware Specs ===")
        super().display_details()  # Renders price, identity, and inventory metrics
        print(f"Processor  : {self.processor}")
        print(f"RAM Size   : {self.ram_gb} GB")
        print(f"Battery Life: Up to {self.battery_hours} hours")
        print("-" * 29)


# --- Demonstration ---
if __name__ == "__main__":
    print("--- Registering System Unit ---")
    # Instantiating a specialized workstation laptop
    laptop1 = Laptop(
        product_id="LAP-880X",
        name="ApexBook Pro 16",
        price=149999.99,
        stock=25,
        processor="Intel Core i7 / Apple M3",
        ram_gb=16,
        battery_hours=14
    )

    # 1. Output comprehensive hardware profile details
    laptop1.display_details()

    # 2. Simulate inventory shifts (a sale occurs)
    print("\n--- Dispatching Unit ---")
    laptop1.update_stock(-1)

    # 3. Confirm inventory state reflects changes without breaking spec tracking
    print("\n--- Verifying Active Stock Details ---")
    laptop1.display_details()