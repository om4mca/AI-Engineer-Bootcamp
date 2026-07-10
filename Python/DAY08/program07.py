#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Function for Area of Circle
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

import math

def calculate_circle_area(radius):
    """Calculates the area of a circle given its radius."""
    area = math.pi * (radius ** 2)
    return area

# Example usage:
r = 7
circle_area = calculate_circle_area(r)

print(f"Radius: {r}")
print(f"Area of Circle: {circle_area:.2f}") 
# Output: Area of Circle:  153.94

# end of the program