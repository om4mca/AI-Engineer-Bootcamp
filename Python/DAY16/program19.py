#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: Calculate Total Hospital Bill
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------


from functools import reduce

patients = [
    {"id": 101, "name": "Om", "age": 42, "bill": 5000},
    {"id": 102, "name": "Rahul", "age": 35, "bill": 7000},
    {"id": 103, "name": "Priya", "age": 28, "bill": 4500},
    {"id": 104, "name": "Amit", "age": 50, "bill": 9000}
]

# Accumulate the total bill using reduce
total_bill = reduce(lambda acc, p: acc + p["bill"], patients, 0)

print("Total Hospital Bill (reduce):", total_bill)