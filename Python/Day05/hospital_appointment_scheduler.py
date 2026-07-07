# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Bonus Challenge Hospital Appointment Scheduler
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------


# Input configuration
patients = 15  # You can change this number to test higher amounts (like 12 or 25)

print("=== Hospital Appointment Scheduler ===\n")

# Loop from 1 up to the total number of patients
for i in range(1, patients + 1):
    # Print the current patient's appointment slot
    print(f"Appointment {i} → Patient {i}")
    
    # Bonus Rule: Check if the current patient index is a multiple of 10
    # i % 10 == 0 evaluates to True only for 10, 20, 30, etc.
    if i % 10 == 0:
        print("\n☕ [BREAK] Doctor Break (10 Minutes)\n")


#End of the program