

#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Function + List Integration
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

def calculate_total(prices):
    # Sum up all elements in the list
    total = 0
    for price in prices:
        total += price
    return total

items = [12.99, 5.50, 23.00]
print(calculate_total(items))  