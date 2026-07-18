#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Patient Class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------



class Patient:
    """A class representing a hospital patient profile."""
    
    def __init__(self, patient_id: int, name: str, age: int, diagnosis: str = "Under Evaluation"):
        # Instance attributes
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.status = "Admitted"
        self.medications = []

    def update_diagnosis(self, new_diagnosis: str):
        """Updates the medical diagnosis."""
        self.diagnosis = new_diagnosis

    def add_medication(self, medication: str):
        """Appends a new drug to the prescription history."""
        if medication not in self.medications:
            self.medications.append(medication)

    def discharge(self):
        """Changes status to discharged."""
        self.status = "Discharged"

    def __str__(self):
        """Returns a human-readable summary string."""
        return (f"Patient ID: {self.patient_id} | Name: {self.name} | "
                f"Age: {self.age} | Diagnosis: {self.diagnosis} | "
                f"Status: {self.status} | Meds: {self.medications}")

# Example usage:
patient1 = Patient(101, "Alice Smith", 34, "Flu")
patient1.add_medication("Ibuprofen")
print(patient1)
# Output: Patient ID: 101 | Name: Alice Smith | Age: 34 | Diagnosis: Flu | Status: Admitted | Meds: ['Ibuprofen']
