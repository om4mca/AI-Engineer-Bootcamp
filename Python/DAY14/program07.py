#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: __repr__()
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Employee:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Employee('{self.name}')"