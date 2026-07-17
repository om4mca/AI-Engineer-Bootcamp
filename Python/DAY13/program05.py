#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Person → Student
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hi, my name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str, major: str):
        # Call the parent class (Person) constructor
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    # Override the introduce method to add student details
    def introduce(self) -> str:
        base_introduction = super().introduce()
        return f"{base_introduction} I am majoring in {self.major} (ID: {self.student_id})."


# Example usage:
if __name__ == "__main__":
    # Create a Person instance
    generic_person = Person("Om", 30)
    print(generic_person.introduce())
    
    # Create a Student instance
    college_student = Student("Sudhir", 20, "S12345", "Computer Science")
    print(college_student.introduce())
