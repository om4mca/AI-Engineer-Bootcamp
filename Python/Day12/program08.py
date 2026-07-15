#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Employee Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class Patient:
    """Represents an individual patient in the hospital database."""
    def __init__(self, patient_id: str, name: str, age: int, condition: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition

    def display_details(self):
        print(f"  [{self.patient_id}] {self.name} | Age: {self.age} | Condition: {self.condition}")


class Hospital:
    """Manages the directory of patients and basic administrative operations."""
    def __init__(self, hospital_name: str):
        self.hospital_name = hospital_name
        self.patients = {}  # Dictionary mapping patient_id -> Patient object for quick O(1) lookups

    def admit_patient(self, patient: Patient):
        """Adds a new patient object to the hospital tracking system."""
        if patient.patient_id in self.patients:
            print(f"[Alert] Patient ID {patient.patient_id} is already registered.")
        else:
            self.patients[patient.patient_id] = patient
            print(f"[Admission] {patient.name} has been successfully admitted to {self.hospital_name}.")

    def discharge_patient(self, patient_id: str):
        """Removes a patient from the system by their unique ID."""
        if patient_id in self.patients:
            removed = self.patients.pop(patient_id)
            print(f"[Discharge] {removed.name} (ID: {patient_id}) has been discharged.")
        else:
            print(f"[Error] Discharge failed: Patient ID {patient_id} not found.")

    def find_patient(self, patient_id: str):
        """Searches for and displays a single patient's record."""
        print(f"\nSearching for Patient ID: {patient_id}...")
        if patient_id in self.patients:
            self.patients[patient_id].display_details()
        else:
            print(f"  [Result] No record found matching ID: {patient_id}")

    def display_all_patients(self):
        """Lists all active patients currently admitted to the facility."""
        print(f"\n--- {self.hospital_name} Current Census ---")
        if not self.patients:
            print("  No patients currently checked in.")
            return
            
        for patient in self.patients.values():
            patient.display_details()
        print(f"Total Active Patients: {len(self.patients)}")


# --- System Demonstration ---
if __name__ == "__main__":
    # 1. Initialize the central Hospital node
    st_jude = Hospital("St. Jude Medical Center")

    print("--- Phase 1: Processing Admissions ---")
    # 2. Instantiate individual patient records
    p1 = Patient("P501", "Mukul Roy", 67, "Recovering from Surgery")
    p2 = Patient("P502", "Sudha Kumari", 29, "Observation")
    p3 = Patient("P503", "Priya Dutt", 42, "Acute Migraine")

    # 3. Register the objects into the hospital database
    st_jude.admit_patient(p1)
    st_jude.admit_patient(p2)
    st_jude.admit_patient(p3)

    # 4. Show the updated internal census state
    st_jude.display_all_patients()

    print("\n--- Phase 2: Queries & Updates ---")
    # 5. Search operation showcase
    st_jude.find_patient("P502")
    st_jude.find_patient("P999") # Testing invalid search edgecase

    print("\n--- Phase 3: Processing Discharges ---")
    # 6. Discharge logic demonstration
    st_jude.discharge_patient("P503")
    
    # Final display check to ensure cleanup
    st_jude.display_all_patients()