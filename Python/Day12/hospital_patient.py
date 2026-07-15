#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Hospital Patient Management
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class Patient:
    def __init__(self, patient_id: str, name: str, age: int, gender: str):
        """Initializes a new patient record."""
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

    def display_patient(self):
        """Prints the patient's current details in a clean format."""
        print(f"\n--- Patient Record: {self.patient_id} ---")
        print(f"Name:    {self.name}")
        print(f"Age:     {self.age}")
        print(f"Gender:  {self.gender}")

    def update_age(self, new_age: int):
        """Updates the patient's age after validation."""
        if isinstance(new_age, int) and new_age >= 0:
            print(f"[Update] Changing {self.name}'s age from {self.age} to {new_age}.")
            self.age = new_age
        else:
            print("[Error] Invalid age provided. Age must be a positive integer.")

    def update_name(self, new_name: str):
        """Updates the patient's name after validation."""
        if new_name and isinstance(new_name, str) and new_name.strip():
            print(f"[Update] Changing name from '{self.name}' to '{new_name.strip()}'.")
            self.name = new_name.strip()
        else:
            print("[Error] Invalid name provided. Name cannot be empty.")


# --- Demonstration & Object Creation ---
if __name__ == "__main__":
    print("Initializing Patient Management System...")

    # Create multiple patient objects
    patient1 = Patient(patient_id="P101", name="Om Roy", age=34, gender="Male")
    patient2 = Patient(patient_id="P102", name="Priya Kumari", age=45, gender="Female")
    patient3 = Patient(patient_id="P103", name="Sudhir", age=12, gender="male")

    # Display initial patient records
    patient1.display_patient()
    patient2.display_patient()
    patient3.display_patient()

    print("\n" + "="*40 + "\nModifying Patient Records...")

    # Update patient details using the methods
    patient1.update_age(35)
    patient2.update_name("Robert C. Chen")
    
    # Intentionally testing validation with an invalid age
    patient3.update_age(-5) 

    # Display updated records to verify changes
    print("\n" + "="*40 + "\nFinal Patient Directory:")
    patient1.display_patient()
    patient2.display_patient()
    patient3.display_patient()