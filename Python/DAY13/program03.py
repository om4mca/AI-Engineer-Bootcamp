#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: super()
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------


class Person:

    def __init__(self, name):
        self.name = name


class Doctor(Person):

    def __init__(self, name, specialization):
        super().__init__(name)
        self.specialization = specialization

doctor = Doctor("Dr. Sharma", "Cardiology")