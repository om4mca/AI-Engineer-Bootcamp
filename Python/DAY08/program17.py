#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Student Result Function
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

def calculate_student_result(name, marks, passing_mark=40, max_mark_per_subject=100):
    """
    Calculates total marks, percentage, final grade, and pass/fail status.
    
    """
    # 1. Validation check for empty input
    if not marks:
        return {"error": "No marks data provided."}
        
    # 2. Process scores and check for individual subject failure
    total_marks = sum(marks.values())
    total_subjects = len(marks)
    max_possible_marks = total_subjects * max_mark_per_subject
    percentage = (total_marks / max_possible_marks) * 100
    
    # Student fails completely if they fail even one subject
    has_failed_subject = any(score < passing_mark for score in marks.values())
    status = "Fail" if has_failed_subject else "Pass"
    
    # 3. Determine the final letter grade
    if status == "Fail":
        grade = "F"
    elif percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "E"
        
    # 4. Return results as a structured dictionary
    return {
        "student_name": name,
        "subject_wise_marks": marks,
        "total_marks": total_marks,
        "max_marks": max_possible_marks,
        "percentage": round(percentage, 2),
        "status": status,
        "grade": grade
    }

# --- Example Implementation ---
student_marks = {"Math": 75, "Science": 92, "English": 68, "History": 85}
result = calculate_student_result("Suraj Kumar", student_marks)

# Pretty print the final breakdown
for key, value in result.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

# end of the program