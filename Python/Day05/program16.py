# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Guess Number
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------

import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
print("Can you guess what it is?\n")

# Loop until the player guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try a higher number.\n")
    elif guess > secret_number:
        print("Too high! Try a lower number.\n")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break  # Exit the game loop

#End of the program