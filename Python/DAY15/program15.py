#--------------------------------------------
# AI Engineer Bootcamp
# Day 15
# Program: Update function
# Author: Om Roy
# Date: 20-07-2026
#--------------------------------------------

from typing import Dict, Any, Optional

# Sample in-memory database
patients_db: Dict[str, Dict[str, Any]] = {
    "P101": {"name": "Alice Smith", "age": 30, "doctor": "Dr. Adams", "status": "Admitted"},
    "P102": {"name": "Bob Jones", "age": 45, "doctor": "Dr. Baker", "status": "Discharged"}
}

def update_patient_record(patient_id: str, **updates) -> Optional[Dict[str, Any]]:
    """
    Updates an existing patient record dynamically.
    
    Example:
        update_patient_record("P101", doctor="Dr. House", status="Discharged")
    """
    pid = patient_id.strip().upper()
    
    if pid not in patients_db:
        raise KeyError(f"Error: Record for ID '{pid}' not found.")

    # Filter out None or empty values to avoid overwriting existing data with blank input
    cleaned_updates = {k: v for k, v in updates.items() if v is not None and str(v).strip() != ""}

    # Update the existing record in-place
    patients_db[pid].update(cleaned_updates)
    return patients_db[pid]


# Example Usage:
if __name__ == "__main__":
    print("Before Update:", patients_db["P101"])
    
    # Update doctor and status only
    updated_record = update_patient_record("P101", doctor="Dr. House", status="In Treatment")
    
    print("After Update :", updated_record)