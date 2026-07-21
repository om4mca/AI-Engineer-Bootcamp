#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: Combined map() + filter() + reduce()
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

# Chained Functional Pipeline
total_senior_revenue = reduce(
    lambda acc, bill: acc + bill,                             
    map(
        lambda p: p["bill"] * 0.90,                           
        filter(lambda p: p["age"] > 40, patients)              
    )
)

print("Total Senior Revenue (after discount):", total_senior_revenue)