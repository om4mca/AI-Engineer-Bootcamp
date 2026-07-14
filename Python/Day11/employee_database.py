#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Employee Database
# Author: Om Roy
# Date: 14-07-2026
#--------------------------------------------


import os

class DuplicateEmployeeError(Exception):
    """Raised when trying to add an employee ID that already exists."""
    pass

class EmployeeNotFoundError(Exception):
    """Raised when a searched Employee ID cannot be found."""
    pass

class InvalidEmployeeDataError(Exception):
    """Raised when validation constraints (e.g., negative salary, empty name) are broken."""
    pass


class EmployeeDatabase:
    FILE_NAME = "employees.txt"

    @classmethod
    def add_and_save_employee(cls, emp_id, name, department, salary):
        # 1. Clean and normalize input data fields
        emp_id = str(emp_id).strip().upper()
        name = str(name).strip().title()
        department = str(department).strip().title()

        # 2. Strict validation constraints
        if not emp_id or not name or not department:
            raise InvalidEmployeeDataError("All fields (ID, Name, Department, Salary) are mandatory.")

        if not emp_id.isalnum():
            raise InvalidEmployeeDataError("Employee ID must be alphanumeric (letters and numbers only).")

        try:
            salary = float(salary)
            if salary < 0:
                raise ValueError()
        except ValueError:
            raise InvalidEmployeeDataError("Salary must be a valid positive number.")

        # 3. Check for duplicates in the existing records
        if cls._id_exists(emp_id):
            raise DuplicateEmployeeError(f"An employee with ID '{emp_id}' already exists in the database.")

        # 4. Save/Append the entry straight to the file
        record_line = f"{emp_id},{name},{department},{salary:.2f}\n"
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: Saved {name} (ID: {emp_id}) to database.")
        except IOError as e:
            print(f"\n[File Error]: Failed to write data to disk. Details: {e}")

    @classmethod
    def display_all_employees(cls):
        records = cls._load_records()
        if not records:
            print("\n[Database Status]: No employee records found.")
            return

        print("\n📋 === EMPLOYEE DIRECTORY ===")
        print(f"{'ID':<10} | {'Name':<20} | {'Department':<15} | {'Salary':<10}")
        print("-" * 65)
        for emp_id, name, dept, salary in records:
            print(f"{emp_id:<10} | {name:<20} | {dept:<15} | {float(salary):>9,.2f}")
        print("=" * 65)

    @classmethod
    def search_employee(cls, search_id):
        search_id = str(search_id).strip().upper()
        records = cls._load_records()

        for emp_id, name, dept, salary in records:
            if emp_id == search_id:
                print(f"\n🎯 [Employee Found: {search_id}]")
                print(f" -> Name       : {name}")
                print(f" -> Department : {dept}")
                print(f" -> Salary     : {float(salary):,.2f}")
                return
                
        raise EmployeeNotFoundError(f"No database entry matches Employee ID '{search_id}'.")

    # --- Internal Utility Helper Methods ---
    @classmethod
    def _load_records(cls):
        """Safely opens, reads, and parses the flat file database into lists."""
        if not os.path.exists(cls.FILE_NAME):
            return []

        parsed_records = []
        try:
            with open(cls.FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    cleaned_line = line.strip()
                    if cleaned_line:  # Ignore empty blank lines
                        parts = cleaned_line.split(",")
                        if len(parts) == 4:
                            parsed_records.append(parts)
        except IOError as e:
            print(f"[Critical Read Error]: Cannot read database file. {e}")
            
        return parsed_records

    @classmethod
    def _id_exists(cls, check_id):
        """Checks if an Employee ID already exists to prevent duplicate entries."""
        records = cls._load_records()
        return any(emp_id == check_id for emp_id, *rest in records)


def main():
    print("=== Corporate Employee Database ===")
    
    while True:
        print("\n" + "="*35)
        print("          DATABASE MENU")
        print("="*35)
        print("1. Add & Save New Employee")
        print("2. Display All Employees")
        print("3. Search Employee by ID")
        print("4. Exit Database")
        print("="*35)
        
        choice = input("Select an option (1-4): ").strip()

        try:
            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Employee Full Name: ")
                dept = input("Enter Department Name: ")
                salary = input("Enter Annual Salary: ")
                EmployeeDatabase.add_and_save_employee(emp_id, name, dept, salary)

            elif choice == "2":
                EmployeeDatabase.display_all_employees()

            elif choice == "3":
                search_id = input("Enter Employee ID to search: ")
                EmployeeDatabase.search_employee(search_id)

            elif choice == "4":
                print("\nDatabase connection closed. Goodbye!")
                break
            else:
                print("\n[Selection Error]: Please enter a choice between 1 and 4.")

        except InvalidEmployeeDataError as e:
            print(f"\n🚨 [Validation Error]: {e}")
            
        except DuplicateEmployeeError as e:
            print(f"\n🚨 [Database Conflict]: {e}")
            
        except EmployeeNotFoundError as e:
            print(f"\n🚨 [Search Failure]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [Unexpected System Error]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()


 # end of the program