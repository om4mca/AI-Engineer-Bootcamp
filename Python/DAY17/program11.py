#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Reverse Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

patients = ["Patient 101", "Patient 102", "Patient 103"]

# 1. Get built-in list_reverseiterator
rev_iter = reversed(patients)

print(type(rev_iter))  # <class 'list_reverseiterator'>

# 2. Consume items backwards
print(next(rev_iter))  # Patient 103
print(next(rev_iter))  # Patient 102
print(next(rev_iter))  # Patient 101