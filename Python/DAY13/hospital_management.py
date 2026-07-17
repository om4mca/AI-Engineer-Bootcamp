#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Hospital Management System
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------



class Person:
    """Base class representing a general person in the hospital."""
    def __init__(self, name: str, age: int, mobile: str):
        self.name = name
        self.age = age
        self.mobile = mobile

    def display_details(self):
        """Displays common personal details."""
        print(r"--- Personal Details ---")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Mobile : {self.mobile}")

    def update_details(self, name: str = None, age: int = None, mobile: str = None):
        """Updates common personal details if new values are provided."""
        if name:
            self.name = name
        if age:
            self.age = age
        if mobile:
            self.mobile = mobile


class Patient(Person):
    """Subclass representing a hospital patient."""
    def __init__(self, name: str, age: int, mobile: str, patient_id: str, disease: str):
        super().__init__(name, age, mobile)
        self.patient_id = patient_id
        self.disease = disease

    def display_details(self):
        super().display_details()
        print(f"ID     : {self.patient_id} (Patient)")
        print(f"Disease: {self.disease}")
        print("-" * 24)

    def update_details(self, name: str = None, age: int = None, mobile: str = None, disease: str = None):
        # Update common details using the parent method
        super().update_details(name, age, mobile)
        # Update patient-specific details
        if disease:
            self.disease = disease


class Doctor(Person):
    """Subclass representing a medical doctor."""
    def __init__(self, name: str, age: int, mobile: str, doctor_id: str, specialization: str):
        super().__init__(name, age, mobile)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display_details(self):
        super().display_details()
        print(f"ID     : {self.doctor_id} (Doctor)")
        print(f"Specialty: {self.specialization}")
        print("-" * 24)

    def update_details(self, name: str = None, age: int = None, mobile: str = None, specialization: str = None):
        super().update_details(name, age, mobile)
        if specialization:
            self.specialization = specialization


class Employee(Person):
    """Subclass representing a general hospital employee (e.g., admin, nurse)."""
    def __init__(self, name: str, age: int, mobile: str, employee_id: str, department: str):
        super().__init__(name, age, mobile)
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"ID     : {self.employee_id} (Employee)")
        print(f"Dept   : {self.department}")
        print("-" * 24)

    def update_details(self, name: str = None, age: int = None, mobile: str = None, department: str = None):
        super().update_details(name, age, mobile)
        if department:
            self.department = department


# --- Demonstration of the System ---
if __name__ == "__main__":
    print("=== Creating Hospital Records ===\n")
    
    # 1. Create instances
    patient1 = Patient("Sudhir Kumar", 29, "555-0192", "P1001", "Flu")
    doctor1 = Doctor("Dr. Ranjeet Sahoo", 45, "555-0143", "D5002", "Cardiology")
    employee1 = Employee("Mark Waugh", 34, "555-0177", "E8009", "HR")

    # 2. Display initial details
    patient1.display_details()
    doctor1.display_details()
    employee1.display_details()

    # 3. Update records
    print("\n=== Updating Sudhir's & Dr. Ranjeet's Records ===\n")
    patient1.update_details(disease="Recovered / Routine Checkup", mobile="555-9999")
    doctor1.update_details(name="Dr. Ranjeet Sahoo Jr.", specialization="Interventional Cardiology")

    # 4. Display updated details
    patient1.display_details()
    doctor1.display_details()