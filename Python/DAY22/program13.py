#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:    total and  average of Sales data
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------


sales = [12500, 18000, 15500, 21000, 9500, 14000]


total_sales = sum(sales)


avg_sales = total_sales / len(sales)

print(f" Total Sales: ₹{total_sales:,}")      
print(f" Average Sales: ₹{avg_sales:,.2f}")   