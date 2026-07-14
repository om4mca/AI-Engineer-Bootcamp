#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Student Record
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import os

class DuplicateStudentError(Exception):
    """Raised when attempting to add a Student ID that already exists."""
    pass

class StudentNotFoundError(Exception):
    """Raised when a queried Student ID cannot be located."""
    pass

class InvalidStudentDataError(Exception):
    """Raised when student fields break structural or logical rules."""
    pass


class StudentRegistry:
    FILE_NAME = "students.txt"

    @classmethod
    def add_and_save_student(cls, student_id, name, class_grade, gpa):
        # 1. Clean inputs
        student_id = str(student_id).strip().upper()
        name = str(name).strip().title()
        class_grade = str(class_grade).strip().upper() # e.g., "10TH", "GRADE 11"

        # 2. Field Validations
        if not student_id or not name or not class_grade:
            raise InvalidStudentDataError("All fields (ID, Name, Grade/Class, GPA) must be completed.")

        if not student_id.isalnum():
            raise InvalidStudentDataError("Student ID must be alphanumeric only.")

        try:
            gpa = float(gpa)
            if gpa < 0.0 or gpa > 4.0:
                raise ValueError()
        except ValueError:
            raise InvalidStudentDataError("GPA must be a decimal number between 0.0 and 4.0.")

        # 3. Check for duplicates
        if cls._id_exists(student_id):
            raise DuplicateStudentError(f"A student record with ID '{student_id}' already exists.")

        # 4. Save to text file
        record_line = f"{student_id},{name},{class_grade},{gpa:.2f}\n"
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: Saved student {name} (ID: {student_id}) to records.")
        except IOError as e:
            print(f"\n[Storage Error]: Failed to write data to disk. Details: {e}")

    @classmethod
    def display_all_students(cls):
        records = cls._load_records()
        if not records:
            print("\n[Registry Status]: No student records found.")
            return

        print("\n🎓 === STUDENT DIRECTORY ===")
        print(f"{'ID':<10} | {'Name':<20} | {'Class/Grade':<12} | {'GPA':<5} | {'Academic Status'}")
        print("-" * 70)
        for stud_id, name, grade, gpa_str in records:
            gpa_val = float(gpa_str)
            status = "Academic Honors" if gpa_val >= 3.5 else "Good Standing" if gpa_val >= 2.0 else "Academic Probation"
            print(f"{stud_id:<10} | {name:<20} | {grade:<12} | {gpa_val:<5.2f} | {status}")
        print("=" * 70)

    @classmethod
    def search_student(cls, search_id):
        search_id = str(search_id).strip().upper()
        records = cls._load_records()

        for stud_id, name, grade, gpa in records:
            if stud_id == search_id:
                gpa_val = float(gpa)
                print(f"\n🎯 [Student Record Found: {search_id}]")
                print(f" -> Name        : {name}")
                print(f" -> Class/Grade : {grade}")
                print(f" -> Cumulative GPA: {gpa_val:.2f} / 4.00")
                print(f" -> Standings   : {'Honors List' if gpa_val >= 3.5 else 'Satisfactory' if gpa_val >= 2.0 else 'Warning'}")
                return
                
        raise StudentNotFoundError(f"No match found for Student ID '{search_id}'.")

    # --- Internal Helpers ---
    @classmethod
    def _load_records(cls):
        """Safely loads text file records into memory."""
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
            print(f"[Critical Error]: Cannot read data storage. {e}")
            
        return parsed_records

    @classmethod
    def _id_exists(cls, check_id):
        records = cls._load_records()
        return any(stud_id == check_id for stud_id, *rest in records)


def main():
    print("=== Academy Student Records Gateway ===")
    
    while True:
        print("\n" + "="*35)
        print("          REGISTRY MENU")
        print("="*35)
        print("1. Add & Save New Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Exit System")
        print("="*35)
        
        choice = input("Select an option (1-4): ").strip()

        try:
            if choice == "1":
                stud_id = input("Enter Student ID (e.g. S102): ")
                name = input("Enter Student Full Name: ")
                grade = input("Enter Class/Grade (e.g. 10th): ")
                gpa = input("Enter Cumulative GPA (0.0 - 4.0): ")
                StudentRegistry.add_and_save_student(stud_id, name, grade, gpa)

            elif choice == "2":
                StudentRegistry.display_all_students()

            elif choice == "3":
                search_id = input("Enter Student ID to search: ")
                StudentRegistry.search_student(search_id)

            elif choice == "4":
                print("\nRecords locked and saved. Goodbye!")
                break
            else:
                print("\n[Selection Error]: Input must be between 1 and 4.")

        except InvalidStudentDataError as e:
            print(f"\n🚨 [Data Validation Failed]: {e}")
            
        except DuplicateStudentError as e:
            print(f"\n🚨 [Conflict Error]: {e}")
            
        except StudentNotFoundError as e:
            print(f"\n🚨 [Not Found]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [Unexpected Error]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()
