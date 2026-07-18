#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---OOP Challenge---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Patient(Person):
    def __init__(self, patient_id, name, age, gender, ailment):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        # Challenge 1: Encapsulation (Private attribute)
        self.__ailment = ailment  
        self.assigned_doctor = None

    # Challenge 1: Getter and Setter
    @property
    def ailment(self):
        return self.__ailment

    @ailment.setter
    def ailment(self, value):
        if isinstance(value, str) and value.strip():
            self.__ailment = value
        else:
            print("Error: Ailment cannot be blank.")

    def assign_doctor(self, doctor_name):
        self.assigned_doctor = doctor_name

    def get_details(self):
        base_info = super().get_details()
        doc_info = self.assigned_doctor if self.assigned_doctor else "None"
        return f"[Patient ID: {self.patient_id}] {base_info} | Ailment: {self.ailment} | Doctor: {doc_info}"


# Challenge 2: Specialized Inheritance
class EmergencyPatient(Patient):
    def __init__(self, patient_id, name, age, gender, ailment, triage_level):
        super().__init__(patient_id, name, age, gender, ailment)
        # Level 1 (highest priority) to 5 (lowest)
        self.triage_level = triage_level  

    # Challenge 2: Polymorphism (Overriding get_details)
    def get_details(self):
        standard_details = super().get_details()
        return f"🚨 CRITICAL [Triage Level {self.triage_level}] -> {standard_details}"


class Doctor(Person):
    def __init__(self, doctor_id, name, age, gender, specialty, max_patients=1):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialty = specialty
        # Challenge 3: Workload tracking attributes
        self.max_patients = max_patients
        self.current_patients = []  

    def get_details(self):
        base_info = super().get_details()
        load = f"{len(self.current_patients)}/{self.max_patients}"
        return f"[Doctor ID: {self.doctor_id}] {base_info} | Specialty: {self.specialty} | Load: {load}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = {}
        self.doctors = {}

    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    # Challenge 3: Business Logic validation
    def schedule_appointment(self, patient_id, doctor_id):
        if patient_id not in self.patients or doctor_id not in self.doctors:
            print("Error: Invalid IDs.")
            return

        patient = self.patients[patient_id]
        doctor = self.doctors[doctor_id]

        if len(doctor.current_patients) >= doctor.max_patients:
            print(f"Booking Failed: Dr. {doctor.name} is at maximum capacity.")
            return

        # Double-bind the relationship safely
        patient.assign_doctor(doctor.name)
        doctor.current_patients.append(patient)
        print(f"Success: {patient.name} assigned to Dr. {doctor.name}.")


# --- Verification Execution ---
hospital = Hospital("Metro ER Center")

# Create a doctor with a hard capacity of 1 patient
busy_doc = Doctor("D88", "Sarah Stone", 38, "Female", "Trauma Surgery", max_patients=1)
hospital.add_doctor(busy_doc)

# Create one regular patient and one critical emergency patient
pat = Patient("P01", "Mark", 19, "Male", "Broken Arm")
er_pat = EmergencyPatient("E02", "Alex", 45, "Non-binary", "Heart Attack", triage_level=1)

hospital.add_patient(pat)
hospital.add_patient(er_pat)

# Try booking both patients to the same doctor
hospital.schedule_appointment("P01", "D88")   # Should succeed
hospital.schedule_appointment("E02", "D88")   # Should fail due to limits

# Test the customized Emergency print format
print(er_pat.get_details())
