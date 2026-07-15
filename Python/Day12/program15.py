#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Patient Class
# Author: Om Roy
# Date: 15-07-2026
#--------------------------------------------

from datetime import date

class Patient:
    def __init__(self, patient_id: int, name: str, birth_year: int, blood_type: str):
        """Initializes the structural attributes of a patient."""
        self.patient_id = patient_id
        self.name = name
        self.birth_year = birth_year
        self.blood_type = blood_type
        self.medical_history: list[str] = []
        self.is_admitted: bool = False

    def calculate_age(self) -> int:
        """Calculates current approximate age based on the system year."""
        current_year = date.today().year
        return current_year - self.birth_year

    def update_admission_status(self, status: bool):
        """Changes admission state (True for admitted, False for discharged)."""
        self.is_admitted = status

    def add_diagnosis(self, condition: str):
        """Appends a new medical condition to the patient record history."""
        self.medical_history.append(condition)

    def __str__(self) -> str:
        """Returns a clean, human-readable string representation of the record."""
        status = "Admitted" if self.is_admitted else "Discharged"
        return f"ID: {self.patient_id} | {self.name} ({self.calculate_age()}yo) | Type: {self.blood_type} | [{status}]"
# 1. Create instances (objects) of the Patient class
patient_1 = Patient(patient_id=401, name="John Doe", birth_year=1985, blood_type="O+")
patient_2 = Patient(patient_id=402, name="Jane Smith", birth_year=1999, blood_type="A-")

# 2. Access variables and execute behaviors
patient_1.add_diagnosis("Hypertension")
patient_1.update_admission_status(True)

print(patient_1)
# Output: ID: 401 | John Doe (41yo) | Type: O+ | [Admitted]

print(f"Patient History: {patient_1.medical_history}")
# Output: Patient History: ['Hypertension']

# 3. Dynamic age tracking check
print(f"{patient_2.name} is {patient_2.calculate_age()} years old.")
# Output: Jane Smith is 27 years old.
