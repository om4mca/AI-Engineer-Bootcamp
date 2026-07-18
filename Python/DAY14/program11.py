#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Student Class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------


class Student:
    # Class variable shared across all student instances
    school_name = "Global Academy"

    def __init__(self, name, roll_number):
        """Constructor to initialize individual student data."""
        self.name = name              # Instance variable
        self.roll_number = roll_number  # Instance variable
        self.grades = []              # Starts with an empty list for grades

    def add_grade(self, score):
        """Appends a new score to the student's grades."""
        if 0 <= score <= 100:
            self.grades.append(score)
        else:
            print("Invalid score! Please enter a value between 0 and 100.")

    def calculate_average(self):
        """Calculates and returns the average grade."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def display_status(self):
        """Returns a string indicating pass/fail status based on average."""
        average = self.calculate_average()
        return "Passing" if average >= 60 else "Failing"

    def __str__(self):
        """Provides a user-friendly string view of the object."""
        return f"Student: {self.name} (Roll No: {self.roll_number})"


# --- How to use the Student class ---

# 1. Create instances (objects) of the Student class
student1 = Student("Alice Smith", 101)
student2 = Student("Bob Jones", 102)

# 2. Add grades to the students
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2.add_grade(55)
student2.add_grade(48)

# 3. Print object and metrics
print(student1)  # Triggers the __str__ method
print(f"Average Grade: {student1.calculate_average():.2f}")
print(f"Academic Status: {student1.display_status()}")
print(f"School: {student1.school_name}")  # Accessing class variable

print("-" * 30)

print(student2)
print(f"Average Grade: {student2.calculate_average():.2f}")
print(f"Academic Status: {student2.display_status()}")
