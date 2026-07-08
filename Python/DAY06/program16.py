# ------------------------------------------
# AI Engineer Bootcamp
# Day 6
# Program: Remove Duplicates
# Author: Om Roy
# Date: 08-07-2026
#--------------------------------------------


employees = ["Om", "Roy", "Ramesh", "Roy", "Om"]

# Removes duplicates while maintaining order
unique_employees = list(dict.fromkeys(employees))

print(unique_employees)  
# Output: ['Om', 'Roy', 'Ramesh']

#End of the program