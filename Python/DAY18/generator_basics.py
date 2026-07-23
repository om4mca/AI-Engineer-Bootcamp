
#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program:  Generator Basics
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def generate_numbers():
    for number in range(1, 6):
        yield number


numbers = generate_numbers()

for number in numbers:
    print(number)