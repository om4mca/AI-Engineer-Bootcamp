#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: Abstract Class
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

from abc import ABC, abstractmethod

# 1. Define the Abstract Class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        """Abstract method; must be implemented by subclasses."""
        pass

    def honk(self):
        """Concrete method; optional to override, shared by all subclasses."""
        return "Beep beep!"

# 2. Create a Subclass
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started. Vroom!"

# --- Usage ---
# my_vehicle = Vehicle()  # ❌ Raises TypeError: Can't instantiate abstract class

my_car = Car()            #  Succeeds
print(my_car.start_engine()) # Output: Car engine started. Vroom!
print(my_car.honk())         # Output: Beep beep!
