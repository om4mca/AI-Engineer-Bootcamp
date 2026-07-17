#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Product → Mobile
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
        """Displays base product specifications."""
        print(f"Product ID : {self.product_id}")
        print(f"Item Name  : {self.name}")
        print(f"Price      : {self.price:.2f}")
        print(f"In Stock   : {self.stock} units")

    def update_stock(self, quantity: int):
        """Adjusts the inventory stock levels (positive for restock, negative for sales)."""
        new_stock = self.stock + quantity
        if new_stock >= 0:
            self.stock = new_stock
            print(f"[Stock Update] {self.name} inventory changed by {quantity}. Current: {self.stock}")
            return True
        else:
            print(f"[Stock Error] Insufficient inventory to complete sale of {abs(quantity)} units.")
            return False


class Mobile(Product):
    """Child class representing a smartphone variant of a product."""
    def __init__(self, product_id: str, name: str, price: float, stock: int, 
                 storage_gb: int, ram_gb: int, has_5g: bool):
        # Forward generic product parameters up to parent initializers
        super().__init__(product_id, name, price, stock)
        # Handle unique mobile device traits
        self.storage_gb = storage_gb
        self.ram_gb = ram_gb
        self.has_5g = has_5g

    def display_details(self):
        """Overrides parent method to list catalog details + technical specifications."""
        print(r"=== Smartphone Specs ===")
        super().display_details()  # Prints foundational price and inventory metrics
        print(f"Storage    : {self.storage_gb} GB")
        print(f"RAM        : {self.ram_gb} GB")
        print(f"5G Network : {'Yes' if self.has_5g else 'No'}")
        print("-" * 25)


# --- Demonstration ---
if __name__ == "__main__":
    print("--- Catalog Registration ---")
    # Initialize a smartphone item entry
    phone1 = Mobile(
        product_id="MOB-XYZ9", 
        name="Quantum Phone 5X", 
        price=8999.99, 
        stock=50, 
        storage_gb=256, 
        ram_gb=8, 
        has_5g=True
    )

    # 1. Inspect total profile data
    phone1.display_details()

    # 2. Process an order/sale (Reduces stock levels)
    print("\n--- Processing Transaction ---")
    phone1.update_stock(-2)  # Selling 2 phones
    
    # 3. Restock inventory shipment
    phone1.update_stock(15)  # Restocking 15 phones

    # 4. Confirm baseline numbers changed while keeping technical specs intact
    print("\n--- Updated Inventory Verification ---")
    phone1.display_details()