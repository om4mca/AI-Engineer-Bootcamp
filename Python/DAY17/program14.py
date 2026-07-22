#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Employee Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

class EmployeeIterator:
    """Production-grade iterator to process employee records with department and active status filtering."""

    def __init__(self, employees, department=None, active_only=True):
        self.employees = employees
        self.department = department
        self.active_only = active_only
        self.index = 0

    def __iter__(self):
        # Iterator protocol: return self
        return self

    def __next__(self):
        # Scan through employee records statefully
        while self.index < len(self.employees):
            employee = self.employees[self.index]
            self.index += 1

            # 1. Skip inactive employees if active_only is set
            if self.active_only and not employee.get("is_active", True):
                continue

            # 2. Skip employees outside the specified department
            if self.department and employee.get("department") != self.department:
                continue

            return employee

        # Raised when all employee records have been evaluated
        raise StopIteration


# --- Test Execution ---
if __name__ == "__main__":
    employee_db = [
        {"id": 101, "name": "Om Sharma", "department": "Engineering", "role": "Backend Dev", "is_active": True},
        {"id": 102, "name": "Rahul Verma", "department": "HR", "role": "HR Manager", "is_active": False},
        {"id": 103, "name": "Priya Patel", "department": "Engineering", "role": "Frontend Dev", "is_active": True},
        {"id": 104, "name": "Amit Kumar", "department": "Finance", "role": "Accountant", "is_active": True},
        {"id": 105, "name": "Neha Gupta", "department": "Engineering", "role": "DevOps Engineer", "is_active": False},
    ]

    print("--- 1. All Active Employees ---")
    active_iter = EmployeeIterator(employee_db, active_only=True)
    for emp in active_iter:
        print(f"[{emp['department']}] ID {emp['id']}: {emp['name']} - {emp['role']}")

    print("\n--- 2. Active Engineering Team Only ---")
    eng_iter = EmployeeIterator(employee_db, department="Engineering", active_only=True)
    for emp in eng_iter:
        print(f"💻 {emp['name']} ({emp['role']})")