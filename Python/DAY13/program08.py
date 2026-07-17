#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Animal → Cat
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"


# Cat inherits from Animal
class Cat(Animal):

    def make_sound(self):
        return "Meow"


# Creating an instance
my_cat = Cat("Whiskers")

print(my_cat.name)
print(my_cat.make_sound())
