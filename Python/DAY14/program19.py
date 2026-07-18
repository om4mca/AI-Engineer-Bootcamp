#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Hospital Class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Person:
    """Base class for all individuals in the hospital system."""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Patient(Person):
    """Subclass representing a patient, inheriting from Person."""
    def __init__(self, patient_id, name, age, gender, ailment):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.ailment = ailment
        self.assigned_doctor = None

    def assign_doctor(self, doctor_name):
        self.assigned_doctor = doctor_name

    def get_details(self):
        base_info = super().get_details()
        doc_info = self.assigned_doctor if self.assigned_doctor else "None"
        return f"[Patient ID: {self.patient_id}] {base_info} | Ailment: {self.ailment} | Doctor: {doc_info}"


class Doctor(Person):
    """Subclass representing a medical doctor, inheriting from Person."""
    def __init__(self, doctor_id, name, age, gender, specialty):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialty = specialty

    def get_details(self):
        base_info = super().get_details()
        return f"[Doctor ID: {self.doctor_id}] {base_info} | Specialty: {self.specialty}"


class Hospital:
    """Core class that manages all doctors, patients, and operations."""
    def __init__(self, name):
        self.name = name
        self.patients = {}
        self.doctors = {}

    def add_doctor(self, doctor):
        """Registers a new doctor into the hospital records."""
        self.doctors[doctor.doctor_id] = doctor
        print(f"Doctor {doctor.name} successfully registered.")

    def add_patient(self, patient):
        """Registers a new patient into the hospital records."""
        self.patients[patient.patient_id] = patient
        print(f"Patient {patient.name} successfully admitted.")

    def schedule_appointment(self, patient_id, doctor_id):
        """Links a patient to an available doctor for an appointment."""
        if patient_id in self.patients and doctor_id in self.doctors:
            patient = self.patients[patient_id]
            doctor = self.doctors[doctor_id]
            patient.assign_doctor(doctor.name)
            print(f"Appointment booked: Patient '{patient.name}' assigned to Dr. '{doctor.name}'.")
        else:
            print("Error: Invalid Patient ID or Doctor ID.")

    def display_all_records(self):
        """Prints high-level summaries of all registered records."""
        print(f"\n--- {self.name} Central Records ---")
        print("\nRegistered Doctors:")
        for doc in self.doctors.values():
            print(f"  - {doc.get_details()}")
            
        print("\nCurrent Patients:")
        for pat in self.patients.values():
            print(f"  - {pat.get_details()}")
# 1. Initialize the hospital central system
my_hospital = Hospital("City General Medical Center")

# 2. Instantiate and register Doctors
doc1 = Doctor("D101", "Alice Smith", 42, "Female", "Cardiology")
doc2 = Doctor("D102", "Bob Jones", 50, "Male", "Neurology")
my_hospital.add_doctor(doc1)
my_hospital.add_doctor(doc2)

# 3. Instantiate and admit Patients
pat1 = Patient("P501", "John Doe", 29, "Male", "Arrhythmia")
pat2 = Patient("P502", "Jane Evans", 34, "Female", "Migraine")
my_hospital.add_patient(pat1)
my_hospital.add_patient(pat2)

# 4. Bind entities via appointments
my_hospital.schedule_appointment("P501", "D101")
my_hospital.schedule_appointment("P502", "D102")

# 5. Display the system overview
my_hospital.display_all_records()
