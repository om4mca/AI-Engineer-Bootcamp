#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Billing  Class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Product:
    """Manages separate items in the store inventory."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class BillingSystem:
    """Handles adding purchased items, processing calculations, and generating invoices."""
    def __init__(self, customer_name: str, tax_rate: float = 0.05):
        self.customer_name = customer_name
        self.tax_rate = tax_rate
        self.cart = []  # Holds tuples of (Product, quantity)

    def add_item(self, product: Product, quantity: int = 1):
        """Adds a product and its specific quantity to the current bill."""
        if quantity > 0:
            self.cart.append((product, quantity))
        else:
            print("Quantity must be greater than zero.")

    def calculate_subtotal(self) -> float:
        """Computes total cost before applying any government taxes."""
        return sum(product.price * quantity for product, quantity in self.cart)

    def calculate_tax(self) -> float:
        """Computes the tax amount based on the current subtotal."""
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self) -> float:
        """Returns the final amount payable by the customer."""
        return self.calculate_subtotal() + self.calculate_tax()

    def generate_invoice(self):
        """Prints a highly readable, structured text invoice."""
        if not self.cart:
            print("Cart is empty. Cannot generate invoice.")
            return

        print("\n" + "=" * 45)
        print(f"{'RETAIL STORE RECEIPT':^45}")
        print("=" * 45)
        print(f"Customer Name: {self.customer_name}")
        print("-" * 45)
        print(f"{'Item Name':<20} {'Qty':<5} {'Unit Price':<10} {'Total':<8}")
        print("-" * 45)

        for product, quantity in self.cart:
            item_total = product.price * quantity
            print(f"{product.name:<20} {quantity:<5} ${product.price:<9.2f} ${item_total:<8.2f}")

        print("-" * 45)
        print(f"{'Subtotal:':<35} ${self.calculate_subtotal():.2f}")
        print(f"{f'Tax ({self.tax_rate * 100}%):':<35} ${self.calculate_tax():.2f}")
        print("=" * 45)
        print(f"{'GRAND TOTAL:':<35} ${self.calculate_total():.2f}")
        print("=" * 45)
        print(f"{'Thank you for shopping with us!':^45}\n")


# ==========================================
# EXECUTION & DEMONSTRATION
# ==========================================
if __name__ == "__main__":
    # 1. Establish an available catalog of items
    laptop = Product("Asus ROG Laptop", 1200.00)
    mouse = Product("Wireless Mouse", 25.50)
    keyboard = Product("Mechanical Keyboard", 85.00)

    # 2. Initialize a new billing instance for a shopper (5% state tax)
    invoice_session = BillingSystem(customer_name="Alice Smith", tax_rate=0.05)

    # 3. Add individual selections to the virtual cart
    invoice_session.add_item(laptop, quantity=1)
    invoice_session.add_item(mouse, quantity=2)
    invoice_session.add_item(keyboard, quantity=1)

    # 4. Generate the finalized printed transaction document
    invoice_session.generate_invoice()
