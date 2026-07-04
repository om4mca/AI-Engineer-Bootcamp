# ------------------------------------------
# AI Engineer Bootcamp
# Day 3
# Program: Palindrome
# Author: Om Roy
# Date: 04-07-2026
# ------------------------------------------

palindrome=input("Enter a word or phrase to check if it's a palindrome: ")

# Remove spaces and convert to lowercase for comparison
cleaned_string = palindrome.replace(" ", "").lower()

# Check if the cleaned string is equal to its reverse
is_palindrome = cleaned_string == cleaned_string[::-1]

if is_palindrome:
    print(f"'{palindrome}' is a palindrome.")
else:
    print(f"'{palindrome}' is not a palindrome.") 

#End of the program
