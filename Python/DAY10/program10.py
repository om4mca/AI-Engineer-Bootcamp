#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Safe Input
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------

def get_safe_age(prompt: str, min_age: int = 0, max_age: int = 120) -> int:
    """Safely prompts for an integer within a specific range."""
    while True:
        try:
            # Step 1: Read the raw string data
            raw_input = input(prompt).strip()
            
            # Step 2: Attempt type conversion
            age = int(raw_input)
            
            # Step 3: Validate specific business rules
            if min_age <= age <= max_age:
                return age
                
            print(f"Error: Age must be between {min_age} and {max_age}.")
            
        except ValueError:
            # Captures cases where the string cannot be parsed as an integer
            print("Error: Invalid entry. Please enter a whole number.")

# Usage Example
user_age = get_safe_age("Please enter your age: ")
print(f"Validated age recorded: {user_age}")



# end of the program     