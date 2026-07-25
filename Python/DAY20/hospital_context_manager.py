import logging
from contextlib import contextmanager

# 1. Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

# Simulated Patient Database
MOCK_PATIENT_DB = {
    "P101": {"name": "Aarav Sharma", "age": 34, "diagnosis": "Hypertension"},
    "P102": {"name": "Priya Patel", "age": 29, "diagnosis": "Type 2 Diabetes"},
    "P103": {"name": "Rohan Verma", "age": 45, "diagnosis": "Asthma"},
}

class HospitalDatabaseConnection:
    """Helper class to simulate active database operations."""
    
    def search_patient(self, name: str):
        logging.info("Searching for patient by name: '%s'...", name)
        results = [
            f"{pid}: {info['name']}"
            for pid, info in MOCK_PATIENT_DB.items()
            if name.lower() in info["name"].lower()
        ]
        return results if results else "No patients found."

    def get_patient_record(self, patient_id: str):
        logging.info("Retrieving record for Patient ID: '%s'...", patient_id)
        if patient_id not in MOCK_PATIENT_DB:
            raise KeyError(f"Patient ID '{patient_id}' not found in database!")
        return MOCK_PATIENT_DB[patient_id]


@contextmanager
def hospital_database():
    """Context Manager to safely manage hospital DB connections."""
    logging.info("Establishing Hospital Database Connection...")
    db_client = HospitalDatabaseConnection()
    
    try:
        # Pass the database interface to the 'with' block
        yield db_client
    except Exception as error:
        # Catch exceptions that happen inside the 'with' block
        logging.error("An error occurred during database operations: %s", error)
        # Re-raise or handle as needed
        raise
    finally:
        # Guaranteed cleanup regardless of success or error
        logging.info("Hospital Database Connection Closed Safely.")


# ==========================================
# Example Usage & Testing
# ==========================================
if __name__ == "__main__":
    print("--- 1. Normal Operations ---")
    with hospital_database() as db:
        # Search patient
        search_results = db.search_patient("Priya")
        print("Search Results:", search_results)
        
        # Retrieve patient record
        patient_record = db.get_patient_record("P101")
        print("Patient Record:", patient_record)

    print("\n--- 2. Handling Exceptions Gracefully ---")
    try:
        with hospital_database() as db:
            # Trying to fetch a non-existent patient ID
            db.get_patient_record("P999")
    except KeyError:
        print("Caught missing patient error outside the block!")