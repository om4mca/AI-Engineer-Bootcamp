
#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Inheritance Ex
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Patient(Person):

    def display(self):
        print(self.name, self.age)


patient = Patient("Om", 42)
patient.display()

print()
print("---------Super----------")
class Person:

    def __init__(self, name):
        self.name = name


class Doctor(Person):

    def __init__(self, name, specialization):
        super().__init__(name)
        self.specialization = specialization

doctor = Doctor("Dr. Sharma", "Cardiology")

print()
print("--------Method Overriding--------------")
class Person:

    def display(self):
        print("Person")


class Patient(Person):

    def display(self):
        print("Patient")

print()
print("----------Encapsulation----------")        
class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)

print()
print("--------Polymorphism---------")        
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

print()
print("-------isinstance()--------")    
print(isinstance(patient, Patient))
print(isinstance(patient, Person))