#--------------------------------------------
# AI Engineer Bootcamp
# Day 15
# Program: Billing module
# Author: Om Roy
# Date: 20-07-2026
#--------------------------------------------

from dataclasses import dataclass, field
from typing import List

@dataclass
class BillItem:
    item_name: str
    price: float
    qty: int = 1

    @property
    def total(self) -> float:
        return self.price * self.qty


@dataclass
class Bill:
    bill_id: str
    customer_id: str
    items: List[BillItem] = field(default_factory=list)
    is_paid: bool = False

    def add_item(self, item_name: str, price: float, qty: int = 1):
        self.items.append(BillItem(item_name, price, qty))

    @property
    def total_amount(self) -> float:
        return sum(item.total for item in self.items)


# Example Usage
if __name__ == "__main__":
    bill = Bill(bill_id="B-101", customer_id="CUST-404")
    bill.add_item("X-Ray Scan", 120.00)
    bill.add_item("Antibiotics", 15.50, 2)
    
    print(f"Bill ID: {bill.bill_id} | Total Due: ${bill.total_amount:.2f} | Paid: {bill.is_paid}")