#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Hospital → Doctor
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_doctors_by_specialty(self, specialty):
        # Maps specialization to a list of matching doctors
        matches = [doc for doc in self.doctors if doc.specialization == specialty]
        return [doc.name for doc in matches]

# 1. Initialize Hospital
city_hospital = Hospital("City General Hospital")

# 2. Add Doctors
doc1 = Doctor("Dr. Sharma", "Cardiology")
doc2 = Doctor("Dr. Patel", "Neurology")
city_hospital.add_doctor(doc1)
city_hospital.add_doctor(doc2)

# 3. Query the Hospital (Hospital → Doctor)
cardio_doctors = city_hospital.get_doctors_by_specialty("Cardiology")
print(f"Cardiologists at {city_hospital.name}: {cardio_doctors}")
