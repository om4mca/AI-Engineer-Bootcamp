"""Custom domain exceptions for the Employee Management System."""

class EmployeeSystemError(Exception):
    """Base exception for domain errors."""
    pass

class EmployeeNotFoundError(EmployeeSystemError):
    """Raised when an employee record is not found."""
    def __init__(self, emp_id: str):
        super().__init__(f"Error: Employee with ID '{emp_id}' was not found.")

class DuplicateEmployeeError(EmployeeSystemError):
    """Raised when adding an employee ID that already exists."""
    def __init__(self, emp_id: str):
        super().__init__(f"Error: Employee with ID '{emp_id}' already exists.")

class InvalidInputError(EmployeeSystemError):
    """Raised when input validation fails."""
    pass