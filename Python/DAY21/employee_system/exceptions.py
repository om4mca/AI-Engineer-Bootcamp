class EmployeeSystemError(Exception):
    """Base exception class for Employee Management System."""
    pass

class EmployeeNotFoundError(EmployeeSystemError):
    """Raised when an employee ID is not found."""
    pass

class ValidationError(EmployeeSystemError):
    """Raised when employee data validation fails."""
    pass

class DataStorageError(EmployeeSystemError):
    """Raised when file reading/writing fails."""
    pass