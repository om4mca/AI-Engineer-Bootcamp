#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: Sort Names
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

names = ["Rahul", "amit", "Priya", "Om", "Bhavna"]

# Case-insensitive alphabetical sort
sorted_names = sorted(names, key=lambda n: n.lower())
print(sorted_names)
# Output: ['amit', 'Bhavna', 'Om', 'Priya', 'Rahul']

# Reverse alphabetical (Z to A)
reverse_names = sorted(names, key=lambda n: n.lower(), reverse=True)
print(reverse_names)
# Output: ['Rahul', 'Priya', 'Om', 'Bhavna', 'amit']