# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Count Vowels
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------


text = input("Enter a sentence: ")

# Define what we are looking for
vowels = "aeiou"
vowel_count = 0

# Loop through each letter in the text
for char in text.lower():
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels: {vowel_count}")


#End of the program