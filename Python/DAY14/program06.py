#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: --str--
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
