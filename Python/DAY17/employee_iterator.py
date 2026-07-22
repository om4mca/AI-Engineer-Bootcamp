#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program:Employee Record Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

class EmployeeIterator:
    """Custom iterator to process employee records one by one."""

    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        # Returns the iterator object itself
        return self

    def __next__(self):
        # Fetch next employee record until the end of the list
        if self.index < len(self.employees):
            employee = self.employees[self.index]
            self.index += 1
            return employee

        # Raise StopIteration to cleanly terminate the loop
        raise StopIteration


# --- Test Execution ---
if __name__ == "__main__":
    employees = [
        {"id": 101, "name": "Om"},
        {"id": 102, "name": "Rahul"},
        {"id": 103, "name": "Priya"},
        {"id": 104, "name": "Amit"}
    ]

    employee_iterator = EmployeeIterator(employees)

    for emp in employee_iterator:
        print(f"ID: {emp['id']} | Name: {emp['name']}")