#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: __str__()
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Patient:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Patient Name : {self.name}"


patient = Patient("Om")

print(patient)

# end of the program