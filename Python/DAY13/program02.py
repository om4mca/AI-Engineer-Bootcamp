#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Multiple Child Classes
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

# The single parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

# Child class 1
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

# Child class 2
class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"

# Independent usage of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.eat())   # Output: Buddy is eating.
print(dog.bark())  # Output: Buddy says Woof!
print(cat.eat())   # Output: Whiskers is eating.
print(cat.meow())  # Output: Whiskers says Meow!
