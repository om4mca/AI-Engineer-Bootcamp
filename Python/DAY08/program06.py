#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Function Returning Two Values
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

def split_name(full_name):
    # Splits string by spaces
    parts = full_name.split() 
    first_name = parts[0]
    last_name = parts[-1]
    
    # Return both values separated by a comma
    return first_name, last_name

# Unpacking the two returned values into two separate variables
first, last = split_name("Om Roy")

print(f"First: {first}") # Output: First: Om
print(f"Last: {last}")   # Output: Last: Roy



# end of the program