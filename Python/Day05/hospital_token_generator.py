# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Project: Hospital Token Generator
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------


# Input: Number of patients
number_of_patients = 10

print("Token Number\n")

# Loop through each patient and generate the token
for i in range(1, number_of_patients + 1):   
    token = "HOSP" + str(i).zfill(3)
    print(token)
    print()  

#End of the program