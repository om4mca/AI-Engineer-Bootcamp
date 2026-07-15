#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Library Class
# Author: Om Roy
# Date: 15-07-2026
#--------------------------------------------

class Student:
    def __init__(self, student_id: int, name: str, major: str):
        """Initializes an individual student profile."""
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa: float = 0.0

    def __repr__(self) -> str:
        return f"Student(ID={self.student_id}, Name='{self.name}')"


class College:
    def __init__(self, name: str, location: str):
        """Initializes the college management registry."""
        self.name = name
        self.location = location
        self.registry: dict[int, Student] = {}  # O(1) Lookups using unique Student ID

    def enroll_student(self, student: Student):
        """Adds a new student object to the college directory."""
        if student.student_id in self.registry:
            print(f"Registration Error: ID {student.student_id} already exists.")
            return
        self.registry[student.student_id] = student
        print(f"Success: Enrolled {student.name} into {self.name}.")

    def update_gpa(self, student_id: int, new_gpa: float):
        """Locates a student profile and updates their academic GPA."""
        if student_id not in self.registry:
            print("Update Failed: Student record not found.")
            return
        if not (0.0 <= new_gpa <= 4.0):
            raise ValueError("Data Error: GPA score must fall between 0.0 and 4.0.")
        
        self.registry[student_id].gpa = new_gpa

    def calculate_average_gpa(self) -> float:
        """Computes the current aggregate GPA across all enrolled students."""
        if not self.registry:
            return 0.0
        return sum(s.gpa for s in self.registry.values()) / len(self.registry)

    def display_roster(self):
        """Outputs a clean, formatted table of all active student records."""
        print(f"\n--- {self.name} Student Roster ({self.location}) ---")
        print(f"{'ID':<6} | {'Student Name':<18} | {'Major':<15} | {'GPA':<5}")
        print("-" * 55)
        for s in self.registry.values():
            print(f"{s.student_id:<6} | {s.name:<18} | {s.major:<15} | {s.gpa:.2f}")
# 1. Instantiate the central college entity
state_college = College("Apex Institute of Technology", "Boston")

# 2. Create individual student profiles
s1 = Student(1001, "Om Roy", "Computer Science")
s2 = Student(1002, "Sudhir Kumar", "Data Analytics")
s3 = Student(1003, "Raj Kumar", "Bio-Engineering")

# 3. Process enrollments
state_college.enroll_student(s1)
state_college.enroll_student(s2)
state_college.enroll_student(s3)

# 4. Modify student records dynamically
state_college.update_gpa(1001, 3.85)
state_college.update_gpa(1002, 3.40)
state_college.update_gpa(1003, 3.92)

# 5. Display system reports
state_college.display_roster()
print(f"\nOverall Institutional GPA: {state_college.calculate_average_gpa():.2f}")
