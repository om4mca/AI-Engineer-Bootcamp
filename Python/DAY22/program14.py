#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:   Highest-selling product identify
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

sales_data = [
    {"product": "Laptop", "quantity_sold": 120, "revenue": 600000},
    {"product": "Smartphone", "quantity_sold": 450, "revenue": 900000},
    {"product": "Headphones", "quantity_sold": 300, "revenue": 150000},
    {"product": "Smartwatch", "quantity_sold": 210, "revenue": 210000}
]


top_by_quantity = max(sales_data, key=lambda x: x["quantity_sold"])


top_by_revenue = max(sales_data, key=lambda x: x["revenue"])

print(f" Top Product by Quantity: {top_by_quantity['product']} ({top_by_quantity['quantity_sold']} units)")
print(f" Top Product by Revenue:  {top_by_revenue['product']} (₹{top_by_revenue['revenue']:,})")