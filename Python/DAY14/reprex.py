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


print()
print("------Class Method--------")
class Employee:

    company = "OpenAI"

    @classmethod
    def show_company(cls):
        print(cls.company)


Employee.show_company()

print()
print("-------Static Method------")
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
# end of the program