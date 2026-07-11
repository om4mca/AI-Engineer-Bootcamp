# Import the custom Student class blueprint explicitly from our module
from student_mod import Student


def main():
    print("=== Academic Registry Portal System ===")
    
    # 1. Instantiate student profiles
    student_one = Student(name="Om ROy", major="Computer Science")
    student_two = Student(name="Rakesh Ranjan", major="Mechanical Engineering")
    
    # 2. Populate academic logs for Student One
    student_one.add_course_grade("Data Structures", 94.5)
    student_one.add_course_grade("Linear Algebra", 88.0)
    student_one.add_course_grade("Software Engineering", 91.0)
    
    # 3. Populate academic logs for Student Two (Hitting Probationary Thresholds)
    student_two.add_course_grade("Thermodynamics", 62.0)
    student_two.add_course_grade("Fluid Mechanics", 58.5)
    student_two.add_course_grade("Calculus III", 71.0)
    
    # 4. Process and print individual summaries via report functions
    for student in [student_one, student_two]:
        report = student.generate_transcript()
        
        print(f"\n[TRANSCRIPT FOR: {report['Name']} | {report['ID']}]")
        print(f"  Field of Study: {report['Major']}")
        print(f"  Enrolled Courses & Marks:")
        for course, grade in report['Grades'].items():
            print(f"    - {course}: {grade}")
        print(f"  Cumulative GPA:    {report['GPA']}")
        print(f"  Status Evaluation: {report['Academic Standing']}")
        
    print("\n=======================================")

if __name__ == "__main__":
    main()