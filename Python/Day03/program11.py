# ------------------------------------------
# AI Engineer Bootcamp
# Day 3
# Program: Initials Example    Om Roy Output OR
# Author: Om Roy
# Date: 04-07-2026
# ------------------------------------------


full_name = "Om Roy" 
name_words = full_name.split()
initials = ""

for word in name_words:
    initials += word[0].upper()

print(initials)


#End of the program