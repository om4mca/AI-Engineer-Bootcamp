#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Employee Class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Employee:
    # Class variable shared across all employee instances
    company_name = "Tech Corp"
    total_employees = 0

    def __init__(self, emp_id: int, name: str, position: str, salary: float):
        # Instance variables unique to each worker
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        
        # Track the total workforce count automatically
        Employee.total_employees += 1

    def update_salary(self, new_salary: float):
        """Updates the employee salary with a given input."""
        if new_salary > 0:
            self.salary = new_salary
        else:
            print("Error: Salary must be a positive number.")

    def __str__(self) -> str:
        """Returns a user-friendly string overview of the worker."""
        return f"{self.name} | ID: {self.emp_id} | Position: {self.position} | Salary: ${self.salary:,}"
