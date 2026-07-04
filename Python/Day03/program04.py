# ------------------------------------------
# AI Engineer Bootcamp
# Day 3
# Program: Count Vowels
# Author: Om Roy
# Date: 04-07-2026
# ------------------------------------------

name=input("Enter Your Name : ")
vowels_count=0
vowels="aeiouAEIOU"

for char in name:
    if char in vowels:
        vowels_count += 1

print(f"Number of vowels in the name : {vowels_count}")

#End of the program