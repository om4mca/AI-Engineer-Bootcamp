#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Doctor Class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Doctor:
    def __init__(self, name, specialization, fee):
        """Initializes the Doctor object with specific attributes."""
        self.name = name                 # Public attribute
        self.specialization = specialization
        self.fee = fee
        self.patients = []               # Keeps track of assigned patients

    def book_appointment(self, patient_name):
        """Adds a new patient to the doctor's roster."""
        if patient_name not in self.patients:
            self.patients.append(patient_name)
            return f"Appointment scheduled with {self.name}."
        return f"{patient_name} is already scheduled with this doctor."

    def display_details(self):
        """Returns structured information about the doctor."""
        return (f"Doctor: {self.name} | "
                f"Specialty: {self.specialization} | "
                f"Fee: ${self.fee}")
