class PatientSystemError(Exception):
    """Base exception for Hospital System."""
    pass

class PatientNotFoundError(PatientSystemError):
    """Raised when a patient ID is not found."""
    pass

class ValidationError(PatientSystemError):
    """Raised when patient validation fails."""
    pass

class DataStorageError(PatientSystemError):
    """Raised when file I/O operations fail."""
    pass