def validate_patient_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative")

    return True

validate_patient_age(-5)


class InvalidPatientError(Exception):
    pass

def validate_patient(patient):

    if not patient.name:
        raise InvalidPatientError(
            "Patient name cannot be empty"
        )