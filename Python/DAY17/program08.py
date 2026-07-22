#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Handle StopIteration
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

patients = iter(["Patient 101", "Patient 102", "Patient 103"])

while True:
    try:
        # Fetch the next item
        patient = next(patients)
        print("Processing:", patient)
    except StopIteration:
        # Handle the end of the iterator gracefully
        print("All patients processed!")
        break