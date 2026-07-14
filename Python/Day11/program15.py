#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Hospital Record
# Author: Om Roy
# Date: 14-07-2026
#--------------------------------------------

import os

class DuplicatePatientError(Exception):
    """Raised when trying to register a medical chart ID that is already assigned."""
    pass

class PatientNotFoundError(Exception):
    """Raised when a specific Patient ID cannot be found in the system database."""
    pass

class InvalidPatientDataError(Exception):
    """Raised when incoming clinical data violates system constraints."""
    pass


class HospitalRecordsSystem:
    FILE_NAME = "patients.txt"
    VALID_WARD_UNITS = ["Emergency", "ICU", "Pediatrics", "General Ward", "Outpatient"]

    @classmethod
    def add_and_save_patient(cls, patient_id, name, diagnosis, ward_unit):
        # 1. Sanitize and normalize string values
        patient_id = str(patient_id).strip().upper()
        name = str(name).strip().title()
        diagnosis = str(diagnosis).strip().title()
        ward_unit = str(ward_unit).strip().title()

        # 2. Strict Input Boundary Validations
        if not patient_id or not name or not diagnosis or not ward_unit:
            raise InvalidPatientDataError("All operational fields (ID, Name, Diagnosis, Ward) are strictly mandatory.")

        if not (patient_id.startswith("P") and patient_id[1:].isdigit()):
            raise InvalidPatientDataError("Format Error: Patient ID must start with 'P' followed by digits (e.g., P201).")

        if len(name) < 2:
            raise InvalidPatientDataError("Clinical Error: Patient name must be at least 2 characters long.")

        if ward_unit not in cls.VALID_WARD_UNITS:
            allowed_wards = ", ".join(cls.VALID_WARD_UNITS)
            raise InvalidPatientDataError(f"Ward Assignment Error: Assigned ward must be one of: [{allowed_wards}].")

        # 3. Ensure chart uniqueness to prevent medical record overlaps
        if cls._id_exists(patient_id):
            raise DuplicatePatientError(f"System Conflict: A patient record with ID '{patient_id}' already exists.")

        # 4. Stream entry straight to the disk
        record_line = f"{patient_id},{name},{diagnosis},{ward_unit}\n"
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: Medical chart created for {name} (ID: {patient_id}) in {ward_unit}.")
        except IOError as e:
            print(f"\n[Disk I/O Error]: Failed to write chart to database. Details: {e}")

    @classmethod
    def display_all_patients(cls):
        records = cls._load_records()
        if not records:
            print("\n[Clinical Database Status]: No patient charts are currently registered.")
            return

        print("\n🏥 === LIVE PATIENT SENSUS DIRECTORY ===")
        print(f"{'ID':<8} | {'Patient Name':<20} | {'Primary Diagnosis':<20} | {'Assigned Ward'}")
        print("-" * 70)
        for pid, name, diag, ward in records:
            print(f"{pid:<8} | {name:<20} | {diag:<20} | {ward}")
        print("=" * 70)

    @classmethod
    def search_patient(cls, search_id):
        search_id = str(search_id).strip().upper()
        records = cls._load_records()

        for pid, name, diag, ward in records:
            if pid == search_id:
                print(f"\n🎯 [Clinical Chart Located: {search_id}]")
                print(f" -> Full Name       : {name}")
                print(f" -> Diagnosis       : {diag}")
                print(f" -> Admission Unit  : {ward}")
                return
                
        raise PatientNotFoundError(f"Chart Search Failed: Patient ID '{search_id}' is not in the active registry.")

    # --- Secure Disk Parsers (Internal Helpers) ---
    @classmethod
    def _load_records(cls):
        """Safely loads flat-file patient lines into structured array records."""
        if not os.path.exists(cls.FILE_NAME):
            return []

        parsed_records = []
        try:
            with open(cls.FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    cleaned = line.strip()
                    if cleaned:
                        parts = cleaned.split(",")
                        if len(parts) == 4:
                            parsed_records.append(parts)
        except IOError as e:
            print(f"[Critical System Error]: Cannot parse clinical files. {e}")
            
        return parsed_records

    @classmethod
    def _id_exists(cls, check_id):
        records = cls._load_records()
        return any(pid == check_id for pid, *rest in records)


def main():
    print("=== Secure Clinical Patient Records Gateway ===")
    
    while True:
        print("\n" + "="*35)
        print("          CLINICAL MENU")
        print("="*35)
        print("1. Register New Patient Admission")
        print("2. Display Current Active Census")
        print("3. Search Patient Chart by ID")
        print("4. Close Gateway Portal")
        print("="*35)
        
        choice = input("Select operation (1-4): ").strip()

        try:
            if choice == "1":
                pid = input("Enter Patient ID (e.g. P101): ")
                name = input("Enter Patient Name: ")
                diag = input("Enter Primary Diagnosis: ")
                print(f"Available Wards: {', '.join(HospitalRecordsSystem.VALID_WARD_UNITS)}")
                ward = input("Assign Ward Unit: ")
                HospitalRecordsSystem.add_and_save_patient(pid, name, diag, ward)

            elif choice == "2":
                HospitalRecordsSystem.display_all_patients()

            elif choice == "3":
                search_id = input("Enter Patient Chart ID: ")
                HospitalRecordsSystem.search_patient(search_id)

            elif choice == "4":
                print("\nClinical connection terminated safely. Registry saved.")
                break
            else:
                print("\n[Entry Error]: Select a valid operation between 1 and 4.")

        except InvalidPatientDataError as e:
            print(f"\n🚨 [Admissions Policy Exception]: {e}")
            
        except DuplicatePatientError as e:
            print(f"\n🚨 [Medical Identity Conflict]: {e}")
            
        except PatientNotFoundError as e:
            print(f"\n🚨 [Clinical Query Missing]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [Unexpected System Exception]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()