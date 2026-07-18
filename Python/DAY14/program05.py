#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: Abstract Method
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Base Class
    
    @abstractmethod
    def start_engine(self):
        """Abstract method; no body logic here."""
        pass

    def honk(self):  # Concrete method (optional shared behavior)
        return "Beep beep!"
