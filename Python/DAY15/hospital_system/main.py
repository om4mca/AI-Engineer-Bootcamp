"""Main entry point driver for the Hospital Management System."""

from manager import HospitalManager
from models import Patient
from exceptions import HospitalSystemException

def prompt_int(prompt: str) -> int:
    """Helper function to validate integer numeric input."""
    while True:
        try:
            val = int(input(prompt).strip())
            if val <= 0:
                print("⚠️ Value must be a positive number.")
                continue
            return val
        except ValueError:
            print("⚠️ Invalid entry. Please enter a numeric integer.")


def prompt_string(prompt: str) -> str:
    """Helper function to validate non-empty string input."""
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("⚠️ Input cannot be left blank.")


def main():
    manager = HospitalManager()

    while True:
        print("\n" + "=" * 45)
        print("     🏥 HOSPITAL MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Register Patient")
        print("2. Search Patient")
        print("3. Display All Patients")
        print("4. Update Patient")
        print("5. Exit")
        print("=" * 45)

        choice = input("Enter choice (1-5): ").strip()

        try:
            if choice == '1':
                print("\n--- Register New Patient ---")
                pid = prompt_string("Patient ID (e.g., P101): ")
                name = prompt_string("Full Name: ")
                age = prompt_int("Age: ")
                gender = prompt_string("Gender (Male/Female/Other): ")
                contact = prompt_string("Contact Number: ")
                ailment = prompt_string("Ailment/Diagnosis: ")
                doctor = prompt_string("Assigned Doctor: ")

                patient = Patient(pid, name, age, gender, contact, ailment, doctor)
                manager.register_patient(patient)
                print(f"\n✅ Patient '{name}' (ID: {patient.patient_id}) successfully registered!")

            elif choice == '2':
                print("\n--- Search Patient ---")
                pid = prompt_string("Enter Patient ID: ")
                patient = manager.search_patient(pid)
                print("\n✅ Record Found:")
                print(f"ID       : {patient.patient_id}")
                print(f"Name     : {patient.name}")
                print(f"Age      : {patient.age}")
                print(f"Gender   : {patient.gender}")
                print(f"Contact  : {patient.contact}")
                print(f"Ailment  : {patient.ailment}")
                print(f"Doctor   : {patient.doctor}")

            elif choice == '3':
                print("\n--- All Patient Records ---")
                patients = manager.get_all_patients()
                if not patients:
                    print("ℹ️ No patient records found.")
                else:
                    for idx, patient in enumerate(patients, start=1):
                        print(f"{idx}. {patient}")

            elif choice == '4':
                print("\n--- Update Patient Record ---")
                pid = prompt_string("Enter Patient ID to update: ")
                # Validates patient existence before prompting update details
                manager.search_patient(pid)

                print("(Press Enter to keep current value)")
                ailment = input("New Ailment: ").strip()
                doctor = input("New Assigned Doctor: ").strip()
                contact = input("New Contact Number: ").strip()

                updated_patient = manager.update_patient(
                    pid, 
                    ailment=ailment if ailment else None, 
                    doctor=doctor if doctor else None, 
                    contact=contact if contact else None
                )
                print(f"\n✅ Patient ID '{updated_patient.patient_id}' successfully updated!")

            elif choice == '5':
                print("\n👋 Exiting Hospital Management System. Good luck!")
                break

            else:
                print("⚠️ Invalid choice. Please select an option between 1 and 5.")

        except HospitalSystemException as e:
            print(f"\n🛑 Domain Error: {e}")
        except Exception as e:
            print(f"\n🛑 Unexpected Error: {e}")


if __name__ == "__main__":
    main()