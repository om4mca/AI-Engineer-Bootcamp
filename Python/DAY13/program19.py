#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: isinstance()
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Patient(Person):

    def display(self):
        print(self.name, self.age)

patient = Patient("Om", 42)
patient.display()
print(isinstance(patient, Patient))
print(isinstance(patient, Person))