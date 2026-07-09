# ------------------------------------------
# AI Engineer Bootcamp
# Day 7
# Program: Set Example
# Author: Om Roy
# Date: 09-07-2026
#--------------------------------------------

#Set:- Remove the duplicate values

patients = {"Kumar", "Amit", "Kumar", "Soha" ,"Aman"}

print(patients)

# output :
# {'Kumar', 'Aman', 'Amit', 'Soha'}

# Set Operations
print()
print("----Set Operation-----------")
set1 = {"Kumar", "Amit", "Singh"}
set2 = {"Amit", "Ramesh", "Kumar"}

print(set1 | set2) # Union
print(set1 & set2) # Intersection
print(set1 - set2) # Difference


#output :
# ----Set Operation-----------
# {'Ramesh', 'Amit', 'Kumar', 'Singh'}   # Union
# {'Amit', 'Kumar'}   # Intersection
# {'Singh'}  # Difference