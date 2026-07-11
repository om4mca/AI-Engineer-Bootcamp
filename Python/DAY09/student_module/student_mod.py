#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Student Module
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import uuid
import math

class Student:
    def __init__(self, name: str, major: str):
        """Initializes a student profile with a unique academic enrollment ID."""
        self.student_id = f"STU-{str(uuid.uuid4())[:6].upper()}"
        self.name = name
        self.major = major
        self.courses = {}  # Format: {"Course Name": numeric_score}

    def add_course_grade(self, course_name: str, score: float):
        """Adds or updates a course score in the student record."""
        if not (0.0 <= score <= 100.0):
            raise ValueError("Course scores must fall within the range of 0 to 100.")
        self.courses[course_name] = score

    def _convert_to_letter_grade(self, score: float) -> str:
        """Internal helper to parse numeric metrics into standard letters."""
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "F"

    def calculate_gpa(self) -> float:
        """
        Calculates average grade percentage. Returns 0.0 if no courses 
        are currently registered to the student transcript profile.
        """
        if not self.courses:
            return 0.0
        
        total_score = sum(self.courses.values())
        average = total_score / len(self.courses)
        return round(average, 2)

    def check_academic_standing(self) -> str:
        """Evaluates whether the student qualifies for honors list or probationary monitoring."""
        current_gpa = self.calculate_gpa()
        
        if current_gpa >= 90.0:
            return "Dean's Honor Roll List"
        elif current_gpa < 65.0:
            return "Academic Probationary Review"
        else:
            return "Good Academic Standing"

    def generate_transcript(self) -> dict:
        """Compiles clean data overview maps for systemic parsing pipelines."""
        transcript_grades = {course: f"{score} ({self._convert_to_letter_grade(score)})" 
                             for course, score in self.courses.items()}
        
        return {
            "ID": self.student_id,
            "Name": self.name,
            "Major": self.major,
            "Grades": transcript_grades,
            "GPA": f"{self.calculate_gpa()}%",
            "Academic Standing": self.check_academic_standing()
        }