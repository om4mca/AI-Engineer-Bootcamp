#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: billing Module
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import uuid
import math
from datetime import datetime
from dataclasses import dataclass

@dataclass
class LineItem:
    """Represents a single billable product item or service."""
    name: str
    unit_price: float
    quantity: int = 1

class Invoice:
    def __init__(self, customer_name: str, tax_rate: float = 0.08):
        """Initializes a secure commercial retail transaction account."""
        self.invoice_id = f"INV-{str(uuid.uuid4())[:8].upper()}"
        self.customer_name = customer_name
        self.tax_rate = tax_rate
        self.items = []
        self.transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def add_item(self, name: str, unit_price: float, quantity: int = 1):
        """Appends a new billing line item ledger mapping structure."""
        if unit_price < 0 or quantity <= 0:
            raise ValueError("Pricing fields must be positive; quantities must exceed zero threshold.")
        self.items.append(LineItem(name=name, unit_price=unit_price, quantity=quantity))

    def calculate_subtotal(self) -> float:
        """Sums up the gross absolute baseline financial item quantities."""
        return round(sum(item.unit_price * item.quantity for item in self.items), 2)

    def calculate_discount(self) -> float:
        """
        Applies automated tiered loyalty volume threshold deductions:
        - Spent over $500 -> 10% cash discount deduction
        - Spent over $200 -> 5% cash discount deduction
        """
        subtotal = self.calculate_subtotal()
        if subtotal >= 500.00:
            return round(subtotal * 0.10, 2)
        elif subtotal >= 200.00:
            return round(subtotal * 0.05, 2)
        return 0.00

    def calculate_tax(self) -> float:
        """Computes region-specific sales tax allocations applied to discounted totals."""
        taxable_base = self.calculate_subtotal() - self.calculate_discount()
        return round(taxable_base * self.tax_rate, 2)

    def calculate_total_due(self) -> float:
        """
        Calculates ultimate settlement balance due.
        Uses math.ceil to standardize structural processing thresholds.
        """
        discounted_base = self.calculate_subtotal() - self.calculate_discount()
        final_balance = discounted_base + self.calculate_tax()
        return float(math.ceil(final_balance))

    def compile_statement(self) -> dict:
        """Generates system logs ready for payment integrations or interface elements."""
        return {
            "Invoice ID": self.invoice_id,
            "Customer": self.customer_name,
            "Date": self.transaction_date,
            "Subtotal": self.calculate_subtotal(),
            "Discount Applied": self.calculate_discount(),
            "Tax Amount": self.calculate_tax(),
            "Total Due": self.calculate_total_due()
        }