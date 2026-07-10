#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Fibonacci Function
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

def generate_fibonacci(terms):
    """Generates a list of Fibonacci numbers up to the specified number of terms."""
    if terms <= 0:
        return []
    elif terms == 1:
        return [0]
        
    # Start with the first two numbers
    sequence = [0, 1]
    
    # Loop to calculate the rest of the terms
    while len(sequence) < terms:
        next_num = sequence[-1] + sequence[-2]  # Add last two items
        sequence.append(next_num)
        
    return sequence

# Example usage: Get the first 10 terms
print(generate_fibonacci(10))  
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# end of the program