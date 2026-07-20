"""Custom exceptions for the Hospital Management System."""

class HospitalSystemException(Exception):
    """Base exception class for application-specific errors."""
    pass

class PatientNotFoundError(HospitalSystemException):
    """Raised when a patient record cannot be located."""
    def __init__(self, patient_id: str):
        super().__init__(f"Error: Patient with ID '{patient_id}' was not found.")

class DuplicatePatientError(HospitalSystemException):
    """Raised when attempting to register an existing patient ID."""
    def __init__(self, patient_id: str):
        super().__init__(f"Error: Patient with ID '{patient_id}' already exists.")

class InvalidDataError(HospitalSystemException):
    """Raised when validation fails for patient input data."""
    pass