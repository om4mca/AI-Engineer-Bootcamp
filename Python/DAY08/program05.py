#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Function with Default Parameter
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

# 'name' defaults to "Guest" if nothing is provided
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

# Calling without an argument -> uses default
greet_user()        # Output: Hello, Guest!

# Calling with an argument -> overrides default
greet_user("Om")    # Output: Hello, Om!




# end of the program