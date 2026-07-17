#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Polymorphism Demo
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()