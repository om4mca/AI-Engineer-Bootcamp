"""Manager layer coordinating model state, storage, and business rules."""

# Change from:
# from .models import Patient
# from .storage import StorageHandler
# from .exceptions import PatientNotFoundError, DuplicatePatientError

# To this:
# In manager.py
from typing import List, Dict  # <--- Make sure List is added here
from models import Patient
from storage import StorageHandler
from exceptions import PatientNotFoundError, DuplicatePatientError

class HospitalManager:
    """Controls overall patient lifecycle and validation."""
    def __init__(self, storage_file: str = "patients_db.json"):
        self.storage = StorageHandler(storage_file)
        self._patients: Dict[str, Patient] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Loads persistent records into internal memory map."""
        records = self.storage.load_all()
        for record in records:
            patient = Patient.from_dict(record)
            self._patients[patient.patient_id] = patient

    def _sync(self) -> None:
        """Synchronizes current state back to the storage file."""
        records = [p.to_dict() for p in self._patients.values()]
        self.storage.save_all(records)

    def register_patient(self, patient: Patient) -> None:
        """Registers a new patient record."""
        if patient.patient_id in self._patients:
            raise DuplicatePatientError(patient.patient_id)
        
        self._patients[patient.patient_id] = patient
        self._sync()

    def search_patient(self, patient_id: str) -> Patient:
        """Finds a patient by ID."""
        patient_id = patient_id.upper().strip()
        if patient_id not in self._patients:
            raise PatientNotFoundError(patient_id)
        return self._patients[patient_id]

    def get_all_patients(self) -> List[Patient]:
        """Returns a list of all registered patients."""
        return list(self._patients.values())

    def update_patient(self, patient_id: str, **kwargs) -> Patient:
        """Updates specific fields for an existing patient."""
        patient = self.search_patient(patient_id)

        if "ailment" in kwargs and kwargs["ailment"]:
            patient.ailment = kwargs["ailment"].strip().title()
        if "doctor" in kwargs and kwargs["doctor"]:
            patient.doctor = kwargs["doctor"].strip().title()
        if "contact" in kwargs and kwargs["contact"]:
            patient._contact = kwargs["contact"].strip()

        self._sync()
        return patient