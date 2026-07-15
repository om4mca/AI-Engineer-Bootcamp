#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Student Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class Student:
    def __init__(self, student_id: str, name: str, major: str, gpa: float):
        """Initializes a new student record."""
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa = gpa

    def display_student(self):
        """Prints the student's current details in a clean format."""
        print(f"\n--- Student Record: {self.student_id} ---")
        print(f"Name:    {self.name}")
        print(f"Major:   {self.major}")
        print(f"GPA:     {self.gpa:.2f}")

    def update_gpa(self, new_gpa: float):
        """Updates the student's GPA after validating it falls between 0.0 and 4.0."""
        if isinstance(new_gpa, (int, float)) and 0.0 <= new_gpa <= 4.0:
            print(f"[Academic Update] Updating {self.name}'s GPA from {self.gpa:.2f} to {new_gpa:.2f}.")
            self.gpa = new_gpa
        else:
            print("[Error] Invalid GPA. Score must be between 0.0 and 4.0.")

    def change_major(self, new_major: str):
        """Updates the student's field of study."""
        if new_major and isinstance(new_major, str) and new_major.strip():
            print(f"[Major Change] Switching {self.name} from {self.major} to {new_major.strip()}.")
            self.major = new_major.strip()
        else:
            print("[Error] Invalid major provided. Field cannot be empty.")


# --- Demonstration & Object Creation ---
if __name__ == "__main__":
    print("Initializing Student Information System...")

    # Create multiple student objects
    student1 = Student(student_id="S2026-01", name="Om Roy", major="Computer Science", gpa=3.85)
    student2 = Student(student_id="S2026-02", name="Sudhir Kumar", major="Biochemistry", gpa=3.92)
    student3 = Student(student_id="S2026-03", name="Gopal Singh", major="History", gpa=2.70)

    # Display initial student profiles
    student1.display_student()
    student2.display_student()
    student3.display_student()

    print("\n" + "="*40 + "\nProcessing Academic Adjustments...")

    # Modify student data using the methods
    student1.update_gpa(3.95)             # Earned straight A's this semester
    student3.change_major("Political Science") # Found a new passion
    student2.update_gpa(4.5)              # Intentionally testing GPA boundary check error

    # Display updated profiles to verify changes
    print("\n" + "="*40 + "\nFinal Student Roster:")
    student1.display_student()
    student2.display_student()
    student3.display_student()


# end of the program