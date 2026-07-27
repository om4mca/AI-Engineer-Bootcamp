from employee import Employee
from file_manager import FileManager
from decorators import log_operation
from exceptions import EmployeeNotFoundError

class EmployeeService:
    """Service Layer handling core operational logic."""
    def __init__(self):
        self.employees = {}  # In-memory store (Dictionary)
        self.file_manager = FileManager()

    @log_operation("Add Employee")
    def add_employee(self, emp_id, name, department, salary, email):
        if emp_id in self.employees:
            raise ValueError(f"Employee ID '{emp_id}' already exists!")
        
        emp = Employee(emp_id, name, department, salary, email)
        self.employees[emp.emp_id] = emp
        print(f"✅ Employee '{name}' added successfully!")

    @log_operation("View All Employees")
    def view_all_employees(self):
        if not self.employees:
            print("ℹ️ No employee records found.")
            return

        print("\n" + "="*85)
        print(" EMPLOYEE DIRECTORY ")
        print("="*85)
        for emp in self.employees.values():
            print(emp)
        print("="*85)

    @log_operation("Search Employee")
    def search_employee(self, emp_id):
        emp = self.employees.get(str(emp_id).strip())
        if not emp:
            raise EmployeeNotFoundError(f"Employee ID '{emp_id}' not found.")
        print("\n🔍 Record Found:")
        print(emp)
        return emp

    @log_operation("Update Employee")
    def update_employee(self, emp_id, name=None, department=None, salary=None, email=None):
        emp = self.search_employee(emp_id)

        # Merge new attributes with existing ones
        new_name = name if name else emp.name
        new_dept = department if department else emp.department
        new_salary = salary if salary is not None else emp.salary
        new_email = email if email else emp.email

        # Validate by instantiating new Employee
        updated_emp = Employee(emp_id, new_name, new_dept, new_salary, new_email)
        self.employees[emp_id] = updated_emp
        print(f"✅ Employee ID '{emp_id}' updated successfully!")

    @log_operation("Delete Employee")
    def delete_employee(self, emp_id):
        self.search_employee(emp_id)  # Validate existence
        del self.employees[str(emp_id).strip()]
        print(f"🗑️ Employee ID '{emp_id}' deleted successfully!")

    @log_operation("Save to File")
    def save_to_file(self):
        self.file_manager.save_employees(self.employees)
        print("💾 All employee records saved to file.")

    @log_operation("Load from File")
    def load_from_file(self):
        raw_data = self.file_manager.load_employees()
        self.employees.clear()
        for item in raw_data:
            emp = Employee.from_dict(item)
            self.employees[emp.emp_id] = emp
        print(f"📂 Loaded {len(self.employees)} records from file.")