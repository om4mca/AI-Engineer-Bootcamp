#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Prime Number Function
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

import math

def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # Exclude all other even numbers quickly
    if n % 2 == 0:
        return False
    
    # Check odd factors up to the square root of n
    limit = int(math.isqrt(n))  # isqrt gets the integer square root
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False  # Found a factor, so it's not prime
            
    return True

# Example Usage:
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False
print(is_prime(1))   # Output: False

# end of the program