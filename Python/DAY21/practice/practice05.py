#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Inheritance + Method Overriding
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    # Method Overriding: Replacing Animal.speak() with a specific Dog sound
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    # Method Overriding: Replacing Animal.speak() with a specific Cat sound
    def speak(self):
        return "Meow!"

generic_animal = Animal()
dog = Dog()
cat = Cat()

print(generic_animal.speak())  
print(dog.speak())             
print(cat.speak())            