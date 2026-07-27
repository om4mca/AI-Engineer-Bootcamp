from patient import Patient
from file_manager import FileManager
from decorators import log_operation
from exceptions import PatientNotFoundError

class PatientService:
    """Service Layer handling business operations."""
    def __init__(self):
        self.patients = {}  # In-memory database (Dictionary)
        self.file_manager = FileManager()

    @log_operation("Add Patient")
    def add_patient(self, patient_id, name, age, disease, contact):
        if patient_id in self.patients:
            raise ValueError(f"Patient with ID '{patient_id}' already exists!")
        
        patient = Patient(patient_id, name, age, disease, contact)
        self.patients[patient.patient_id] = patient
        print(f"✅ Patient '{name}' added successfully!")

    @log_operation("View All Patients")
    def view_all_patients(self):
        if not self.patients:
            print("ℹ️ No patient records found.")
            return
        
        print("\n" + "="*70)
        print(" HOSPITAL PATIENT RECORDS ")
        print("="*70)
        for patient in self.patients.values():
            print(patient)
        print("="*70)

    @log_operation("Search Patient")
    def search_patient(self, patient_id):
        patient = self.patients.get(str(patient_id).strip())
        if not patient:
            raise PatientNotFoundError(f"Patient ID '{patient_id}' not found.")
        print("\n🔍 Record Found:")
        print(patient)
        return patient

    @log_operation("Update Patient")
    def update_patient(self, patient_id, name=None, age=None, disease=None, contact=None):
        patient = self.search_patient(patient_id)
        
        # Build updated attributes
        new_name = name if name else patient.name
        new_age = age if age else patient.age
        new_disease = disease if disease else patient.disease
        new_contact = contact if contact else patient.contact

        # Re-validate with new instance before committing
        updated = Patient(patient_id, new_name, new_age, new_disease, new_contact)
        self.patients[patient_id] = updated
        print(f"✅ Patient ID '{patient_id}' updated successfully!")

    @log_operation("Delete Patient")
    def delete_patient(self, patient_id):
        self.search_patient(patient_id) # Verify existence
        del self.patients[str(patient_id).strip()]
        print(f"🗑️ Patient ID '{patient_id}' deleted successfully!")

    @log_operation("Save Patients to File")
    def save_to_file(self):
        self.file_manager.save_patients(self.patients)
        print("💾 All patient records saved to JSON file.")

    @log_operation("Load Patients from File")
    def load_from_file(self):
        raw_data = self.file_manager.load_patients()
        self.patients.clear()
        for item in raw_data:
            p = Patient.from_dict(item)
            self.patients[p.patient_id] = p
        print(f"📂 Loaded {len(self.patients)} patient records from file.")