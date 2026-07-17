#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Hospital → Patient
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

class Patient:
    def __init__(self, patient_id, name, age, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.status = "Admitted"

    def get_info(self):
        return f"ID: {self.patient_id} | Name: {self.name} | Status: {self.status}"

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def admit_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} successfully admitted to {self.name}.")

    def discharge_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                patient.status = "Discharged"
                print(f"Patient {patient.name} has been discharged.")
                return
        print("Patient ID not found.")

    def view_active_patients(self):
        print("\n--- Active Patients ---")
        for patient in self.patients:
            if patient.status == "Admitted":
                print(patient.get_info())

# Example Usage
city_hospital = Hospital("Bhubaneswar City General Hospital")

# Creating patients
p1 = Patient(101, "Amit Patel", 45, "Malaria")
p2 = Patient(102, "Sneha Das", 28, "Observation")

# Hospital takes in patients
city_hospital.admit_patient(p1)
city_hospital.admit_patient(p2)

# View current state
city_hospital.view_active_patients()

# Hospital discharges a patient
city_hospital.discharge_patient(101)
