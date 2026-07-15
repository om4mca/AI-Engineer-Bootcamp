#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Create Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class Student:
    pass

student1 = Student()

print(student1)

print()
print("------Constructor--------")
class Student:

    def __init__(self):
        print("Constructor Called")

student = Student()


print()
print("----Attributes-----")
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Om", 42)

print(student.name)
print(student.age)


print()
print("-------Methods----------")
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student:", self.name)

student = Student("Om")

student.display()



print()
print("----Multiple Objects------")

student1 = Student("Om")
student2 = Student("Rahul")
student3 = Student("Priya")

student1.display()
student2.display()
student3.display()
# end of the program