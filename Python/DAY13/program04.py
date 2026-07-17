#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Method Overriding
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

class Person:

    def display(self):
        print("Person")


class Patient(Person):

    def display(self):
        print("Patient")