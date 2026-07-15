#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Employee Management
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class Employee:
    def __init__(self, employee_id: str, name: str, department: str, salary: float):
        """Initializes a new employee record."""
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_employee(self):
        """Prints the employee's current details in a clean format."""
        print(f"\n--- Employee Record: {self.employee_id} ---")
        print(f"Name:       {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary:     {self.salary:,.2f}")

    def increase_salary(self, percentage: float):
        """Increases the employee's salary by a given percentage."""
        if percentage > 0:
            raise_amount = self.salary * (percentage / 100)
            old_salary = self.salary
            self.salary += raise_amount
            print(f"[Raise] {self.name} received a {percentage}% raise. "
                  f"Salary bumped from {old_salary:,.2f} to {self.salary:,.2f}.")
        else:
            print("[Error] Invalid percentage. The increase must be greater than 0.")

    def update_department(self, new_department: str):
        """Updates the employee's department."""
        if new_department and isinstance(new_department, str) and new_department.strip():
            print(f"[Transfer] Moving {self.name} from {self.department} to {new_department.strip()}.")
            self.department = new_department.strip()
        else:
            print("[Error] Invalid department provided. Department cannot be empty.")


# --- Demonstration & Object Creation ---
if __name__ == "__main__":
    print("Initializing Employee Management System...")

    # Create multiple employee objects
    emp1 = Employee(employee_id="E001", name="Om Roy", department="Engineering", salary=95000.00)
    emp2 = Employee(employee_id="E002", name="Sudhir Kumar", department="Marketing", salary=72000.00)
    emp3 = Employee(employee_id="E003", name="Sushat Behera", department="Human Resources", salary=68000.00)

    # Display initial employee records
    emp1.display_employee()
    emp2.display_employee()
    emp3.display_employee()

    print("\n" + "="*40 + "\nProcessing Corporate Changes...")

    # Apply adjustments using the methods
    emp1.increase_salary(8.5)            # 8.5% merit increase
    emp2.update_department("Operations") # Department transfer
    emp3.increase_salary(-2.0)           # Intentionally testing input validation

    # Display updated records to verify changes
    print("\n" + "="*40 + "\nFinal Employee Directory:")
    emp1.display_employee()
    emp2.display_employee()
    emp3.display_employee()