#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Safe Division
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------
def safe_divide(numerator, denominator):
    # Returns 0 (or None) if the denominator is zero
    if denominator == 0:
        return 0
    return numerator / denominator

# Examples
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: 0



# end of the program     