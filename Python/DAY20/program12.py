import sqlite3
import logging
from contextlib import contextmanager

# Set up logging to track database access
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

class HospitalDatabase:
    """Helper class providing database operations inside the context."""
    def __init__(self, connection: sqlite3.Connection):
        self.conn = connection
        self.cursor = connection.cursor()

    def search_patient(self, name: str):
        logging.info("Searching records for patient: '%s'...", name)
        query = "SELECT patient_id, name, age, diagnosis FROM patients WHERE name LIKE ?"
        self.cursor.execute(query, (f"%{name}%",))
        return self.cursor.fetchall()

    def add_patient(self, patient_id: str, name: str, age: int, diagnosis: str):
        logging.info("Adding new patient: %s (%s)...", name, patient_id)
        query = "INSERT INTO patients (patient_id, name, age, diagnosis) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (patient_id, name, age, diagnosis))


@contextmanager
def hospital_db_session(db_path: str = ":memory:"):
    """
    Context Manager to manage hospital DB connections.
    Guarantees automatic commit on success and rollback on errors.
    """
    logging.info("Connecting to Hospital Database (%s)...", db_path)
    conn = sqlite3.connect(db_path)
    
    # Initialize sample table if using in-memory database
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            diagnosis TEXT
        )
    """)
    conn.commit()

    db = HospitalDatabase(conn)

    try:
        # Pass the database operational handle to the 'with' block
        yield db
        
        # Commit transaction automatically if no errors occurred inside block
        conn.commit()
        logging.info("Transaction committed successfully.")

    except Exception as error:
        # Roll back changes if an exception was raised inside 'with'
        conn.rollback()
        logging.error("Transaction failed! Changes rolled back. Reason: %s", error)
        raise  # Re-raise to allow caller handling

    finally:
        # Guaranteed cleanup regardless of pass or fail
        conn.close()
        logging.info("Hospital Database Connection Closed Safely.")


# ==========================================
# Practical Usage
# ==========================================
if __name__ == "__main__":
    
    print("--- 1. Performing Database Writes & Searches ---")
    with hospital_db_session() as db:
        db.add_patient("P101", "Aarav Sharma", 34, "Hypertension")
        db.add_patient("P102", "Priya Patel", 29, "Type 2 Diabetes")
        
        # Search patient record
        results = db.search_patient("Priya")
        print("Search Results:", results)

    print("\n--- 2. Testing Automatic Rollback on Failure ---")
    try:
        with hospital_db_session() as db:
            db.add_patient("P103", "Rohan Verma", 45, "Asthma")
            
            # Simulating a primary key conflict error (Duplicate ID P101)
            db.add_patient("P101", "Duplicate Entry", 50, "Error Test")
            
    except sqlite3.IntegrityError:
        print(">> Integrity Error caught! The rollback prevented corrupted data insertion.")