#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Hospital Patient Record System
# Author: Om Roy
# Date: 14-07-2026
#--------------------------------------------


import os

class PatientNotFoundError(Exception):
    """Raised when a requested Patient ID does not exist in the database."""
    pass

class InvalidPatientDataError(Exception):
    """Raised when data fields violate validation constraints."""
    pass


class HospitalRegistry:
    FILE_NAME = "patients.txt"

    @classmethod
    def add_patient(cls, patient_id, name, age, gender):
        # 1. Basic Structural Validations
        patient_id = str(patient_id).strip().upper()
        name = str(name).strip().title()
        gender = str(gender).strip().title()
        
        if not patient_id or not name or not gender:
            raise InvalidPatientDataError("All patient registry fields are completely mandatory.")
            
        if not patient_id.startswith('P') or len(patient_id) < 2:
            raise InvalidPatientDataError("System Error: Patient ID must start with a capital 'P' followed by a number (e.g., P001).")

        try:
            age = int(age)
            if age <= 0 or age > 125:
                raise ValueError()
        except ValueError:
            raise InvalidPatientDataError("Validation Failure: Age must be a realistic whole positive integer.")

        if gender not in ["Male", "Female", "Other"]:
            raise InvalidPatientDataError("Validation Failure: Gender must be registered as 'Male', 'Female', or 'Other'.")

        # 2. Check for Duplicate IDs before appending to file
        if cls._id_exists(patient_id):
            raise InvalidPatientDataError(f"Conflict Alert: A record with ID '{patient_id}' already exists.")

        # 3. Save directly to file using standard storage format
        record_line = f"{patient_id},{name},{age},{gender}\n"
        
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: Record saved for {name} under reference {patient_id}.")
        except IOError as e:
            print(f"\n[File Access Error]: Unable to write record entry to disk. Details: {e}")

    @classmethod
    def read_all_patients(cls):
        records = cls._load_file_records()
        if not records:
            print("\n[Registry Status]: The medical database ledger is currently empty.")
            return

        print("\n📋 === REGISTERED PATIENT LEDGER ===")
        print(f"{'ID':<8} | {'Patient Name':<18} | {'Age':<4} | {'Gender':<8}")
        print("-" * 48)
        for pid, name, age, gender in records:
            print(f"{pid:<8} | {name:<18} | {age:<4} | {gender:<8}")
        print("=" * 48)

    @classmethod
    def search_patient(cls, search_id):
        search_id = str(search_id).strip().upper()
        records = cls._load_file_records()
        
        for pid, name, age, gender in records:
            if pid == search_id:
                print(f"\n🎯 [Match Found for ID: {search_id}]")
                print(f" -> Name   : {name}")
                print(f" -> Age    : {age} years old")
                print(f" -> Gender : {gender}")
                return
                
        raise PatientNotFoundError(f"Search Query Failed: No matching charts found for ID '{search_id}'.")

    @classmethod
    def count_total_patients(cls):
        records = cls._load_file_records()
        total = len(records)
        print(f"\n📊 Total Registered Patient Count: {total} Active Record(s)")
        return total

    # --- Structural Internal Helper Methods ---
    @classmethod
    def _load_file_records(cls):
        """Helper method to load and parse file data safely into structured lists."""
        if not os.path.exists(cls.FILE_NAME):
            return []

        parsed_records = []
        try:
            with open(cls.FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    cleaned_line = line.strip()
                    if cleaned_line: # Skips empty lines smoothly
                        parts = cleaned_line.split(",")
                        if len(parts) == 4:
                            parsed_records.append(parts)
        except IOError as e:
            print(f"[Critical System Error]: Cannot parse data file safely. {e}")
            
        return parsed_records

    @classmethod
    def _id_exists(cls, check_id):
        """Internal helper to trace duplicate primary ID constraints."""
        records = cls._load_file_records()
        return any(pid == check_id for pid, *rest in records)


def main():
    print("=== Secure Hospital Records Engine ===")
    
    while True:
        print("\n" + "="*35)
        print("          REGISTRY MENU")
        print("="*35)
        print("1. Add New Patient Profile")
        print("2. Display All Patients Ledger")
        print("3. Search Patient by Chart ID")
        print("4. Summary Statistics (Count Total)")
        print("5. Terminate Session Node")
        print("="*35)
        
        choice = input("Select operation (1-5): ").strip()

        try:
            if choice == "1":
                pid = input("Enter Patient ID (e.g. P001): ")
                name = input("Enter Patient Full Name: ")
                age = input("Enter Patient Age: ")
                gender = input("Enter Gender (Male/Female/Other): ")
                HospitalRegistry.add_patient(pid, name, age, gender)

            elif choice == "2":
                HospitalRegistry.read_all_patients()

            elif choice == "3":
                search_id = input("Enter Patient ID to search: ")
                HospitalRegistry.search_patient(search_id)

            elif choice == "4":
                HospitalRegistry.count_total_patients()

            elif choice == "5":
                print("\nSession safely closed. All file pointers unlinked cleanly.")
                break
            else:
                print("\n[Invalid Option]: Please choose a menu command between 1 and 5.")

        except InvalidPatientDataError as e:
            print(f"\n🚨 [Policy Violation]: {e}")
            
        except PatientNotFoundError as e:
            print(f"\n🚨 [Lookup Error]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [Unexpected Runtime Exception]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()




# end of the program