#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Person → Employee
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: str, salary: float):
        # Call the parent class (Person) constructor
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self) -> str:
        # Extend the parent class method
        base_info = super().display_info()
        return f"{base_info}, ID: {self.employee_id}, Salary: {self.salary:,.2f}"


# Example Usage
if __name__ == "__main__":
    # Create an instance of Employee
    emp = Employee(name="Om Roy", age=30, employee_id="E1042", salary=95000.0)
    
    # Display the employee's details
    print(emp.display_info())
