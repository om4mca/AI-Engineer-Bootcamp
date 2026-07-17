#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Animal → Dog
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------


# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a noise."

# Dog class inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Create instances
generic_animal = Animal("Generic Creature")
my_dog = Dog("Buddy")

# Output
print(generic_animal.speak())  # Output: Generic Creature makes a noise.
print(my_dog.speak())          # Output: Buddy says Woof!


