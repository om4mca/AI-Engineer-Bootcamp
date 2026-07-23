#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: String Character Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def char_generator(text):
    """Yields each character in a string one by one."""
    for char in text:
        yield char


sample_text = "Hello World"

print("===  Basic Character Generator ===")
for char in char_generator("Python"):
    print(char, end=" -> ")
print("END")        