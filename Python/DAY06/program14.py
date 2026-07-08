# ------------------------------------------
# AI Engineer Bootcamp
# Day 6
# Program: Copy List
# Author: Om Roy
# Date: 08-07-2026
#--------------------------------------------

original = ["Om", "Ram", "Shaym"]

# Create an independent duplicate
cloned_list = original.copy()

# Prove they are independent by modifying the clone
cloned_list.append("Dravid")

print("Original:", original)     
print("Cloned:", cloned_list)

# Output:
# Original: ['Om', 'Ram', 'Shaym']
# Cloned: ['Om', 'Ram', 'Shaym', 'Dravid']


#End of the program