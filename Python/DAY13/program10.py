#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Vehicle → Bike
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        return "Engine started."

# Bike inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, year, bike_type):
        # Call the parent class constructor
        super().__init__(brand, year)  
        self.bike_type = bike_type  # e.g., Mountain, Cruiser, Sport

    def ring_bell(self):
        return "Ring ring!"

# Example usage:
my_bike = Bike("Trek", 2024, "Mountain")

print(my_bike.brand)          # Accesses parent attribute: Trek
print(my_bike.start_engine()) # Accesses parent method: Engine started.
print(my_bike.ring_bell())    # Accesses child method: Ring ring!
