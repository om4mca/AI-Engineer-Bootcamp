#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Vehicle → Car
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------


class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        return "Engine started."


# Car inherits from Vehicle
class Car(Vehicle):

    def __init__(self, brand, year, doors):
        # Call the parent class constructor
        super().__init__(brand, year)
        self.doors = doors

    def honk(self):
        return "Beep beep!"


# Create an instance of Car
my_car = Car("Toyota", 2024, 4)

# Access inherited and unique properties
print(my_car.brand)  # Output: Toyota
print(my_car.start_engine())  # Output: Engine started.
print(my_car.honk())  # Output: Beep beep!

   
