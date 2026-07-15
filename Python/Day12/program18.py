#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Display Object Data
# Author: Om Roy
# Date: 15-07-2026
#--------------------------------------------

class Patient:
    def __init__(self, patient_id: int, name: str, blood_type: str):
        self.patient_id = patient_id
        self.name = name
        self.blood_type = blood_type

    def __str__(self) -> str:
        """Executed automatically when print() or str() is called."""
        return f"[Patient Record] ID: {self.patient_id} | Name: {self.name} | Blood: {self.blood_type}"

# Usage
p1 = Patient(901, "Om Roy", "AB-")
print(p1) 
# Output: [Patient Record] ID: 901 | Name: Om Roy | Blood: AB-
