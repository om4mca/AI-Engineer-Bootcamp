#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Employee Record
# Author: Om Roy
# Date: 14-07-2026
#--------------------------------------------

import os

class DuplicateEmployeeError(Exception):
    """Raised when trying to register an Employee ID that is already taken."""
    pass

class EmployeeNotFoundError(Exception):
    """Raised when a specific Employee ID is not found in the file database."""
    pass

class InvalidEmployeeDataError(Exception):
    """Raised when field formats or inputs break structural constraints."""
    pass


class EmployeeRegistry:
    FILE_NAME = "employees.txt"

    @classmethod
    def add_and_save_employee(cls, emp_id, name, department, role):
        # 1. Sanitize and normalize input strings
        emp_id = str(emp_id).strip().upper()
        name = str(name).strip().title()
        department = str(department).strip().title()
        role = str(role).strip().title()

        # 2. Strict validation rules
        if not emp_id or not name or not department or not role:
            raise InvalidEmployeeDataError("All entry fields (ID, Name, Department, Role) are mandatory.")

        if not (emp_id.startswith("E") and emp_id[1:].isdigit()):
            raise InvalidEmployeeDataError("Format Error: Employee ID must start with an 'E' followed by digits (e.g., E101).")

        if len(name) < 2:
            raise InvalidEmployeeDataError("Validation Error: Name must be at least 2 characters long.")

        # 3. Prevent duplicate Primary Keys
        if cls._id_exists(emp_id):
            raise DuplicateEmployeeError(f"Database Conflict: Employee with ID '{emp_id}' is already registered.")

        # 4. Save to flat file database
        record_line = f"{emp_id},{name},{department},{role}\n"
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: {name} registered as {role} (ID: {emp_id}).")
        except IOError as e:
            print(f"\n[Storage Error]: Failed to write record to flat-file database. Details: {e}")

    @classmethod
    def display_all_employees(cls):
        records = cls._load_records()
        if not records:
            print("\n[Database Status]: The employee registry is currently empty.")
            return

        print("\n💼 === CORPORATE ROSTER DIRECTORY ===")
        print(f"{'ID':<8} | {'Employee Name':<20} | {'Department':<18} | {'Role'}")
        print("-" * 65)
        for emp_id, name, dept, role in records:
            print(f"{emp_id:<8} | {name:<20} | {dept:<18} | {role}")
        print("=" * 65)

    @classmethod
    def search_employee(cls, search_id):
        search_id = str(search_id).strip().upper()
        records = cls._load_records()

        for emp_id, name, dept, role in records:
            if emp_id == search_id:
                print(f"\n🎯 [Employee Profile Found: {search_id}]")
                print(f" -> Name       : {name}")
                print(f" -> Department : {dept}")
                print(f" -> Assigned Role: {role}")
                return
                
        raise EmployeeNotFoundError(f"Lookup Failed: Employee ID '{search_id}' does not exist.")

    # --- Internal Flat-File Parsers ---
    @classmethod
    def _load_records(cls):
        """Safely opens, processes, and serves comma-separated values as lists."""
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
            print(f"[Critical I/O Error]: Unable to load registry from disk. {e}")
            
        return parsed_records

    @classmethod
    def _id_exists(cls, check_id):
        records = cls._load_records()
        return any(emp_id == check_id for emp_id, *rest in records)


def main():
    print("=== Institutional Resource Management Node ===")
    
    while True:
        print("\n" + "="*35)
        print("          DATABASE MENU")
        print("="*35)
        print("1. Register New Employee Record")
        print("2. Display Entire Corporate Roster")
        print("3. Search Profile by Employee ID")
        print("4. Exit Database")
        print("="*35)
        
        choice = input("Choose an option (1-4): ").strip()

        try:
            if choice == "1":
                emp_id = input("Enter Employee ID (e.g. E101): ")
                name = input("Enter Employee Full Name: ")
                dept = input("Enter Department: ")
                role = input("Enter Current Job Title/Role: ")
                EmployeeRegistry.add_and_save_employee(emp_id, name, dept, role)

            elif choice == "2":
                EmployeeRegistry.display_all_employees()

            elif choice == "3":
                search_id = input("Enter Employee ID to search: ")
                EmployeeRegistry.search_employee(search_id)

            elif choice == "4":
                print("\nDatabase session disconnected. Goodbye!")
                break
            else:
                print("\n[Selection Error]: Input value must be an integer between 1 and 4.")

        except InvalidEmployeeDataError as e:
            print(f"\n🚨 [Policy Violation]: {e}")
            
        except DuplicateEmployeeError as e:
            print(f"\n🚨 [Database Conflict]: {e}")
            
        except EmployeeNotFoundError as e:
            print(f"\n🚨 [Lookup Error]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [Unexpected Runtime Exception]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()