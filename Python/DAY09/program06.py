#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Current Date
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

from datetime import date

# 1. Fetch today's date object
today = date.today()
print(f"Raw date object: {today}")  # Output: 2026-07-11

# 2. Format it into standard layouts (MM/DD/YYYY or DD-MM-YYYY)
formatted_us = today.strftime("%m/%d/%Y")
formatted_uk = today.strftime("%d-%m-%Y")
readable_text = today.strftime("%B %d, %Y")

print(f"US Format:   {formatted_us}")   # Output: 07/11/2026
print(f"UK Format:   {formatted_uk}")   # Output: 11-07-2026
print(f"Text Format: {readable_text}") # Output: July 11, 2026

#end of the program