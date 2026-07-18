#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: Abstraction
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def display(self):
        pass


class Patient(Person):

    def display(self):
        print("Patient Details")

# end of the program