from models.patient import Patient
from utils.validators import validate_patient_age
from utils.decorators import log_operation


class PatientService:

    def __init__(self):
        self.patients = []

    @log_operation
    def add_patient(
        self,
        patient_id,
        name,
        age,
        disease
    ):

        validate_patient_age(age)

        patient = Patient(
            patient_id,
            name,
            age,
            disease
        )

        self.patients.append(patient)

        return patient

    def get_all_patients(self):

        for patient in self.patients:
            yield patient

     