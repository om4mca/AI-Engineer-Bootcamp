#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Countdown Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def countdown_generator(start_num):
    """Yields numbers counting down from start_num to 0."""
    current = start_num
    while current >= 0:
        yield current
        current -= 1

print("===  Countdown (Instant) ===")
for num in countdown_generator(5):
    print(num)