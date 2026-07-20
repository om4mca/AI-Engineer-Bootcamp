#--------------------------------------------
# AI Engineer Bootcamp
# Day 15
# Program: Search function
# Author: Om Roy
# Date: 20-07-2026
#--------------------------------------------

from typing import List, Dict, Optional

# Sample dataset
patients = [
    {"id": "P101", "name": "Alice Smith", "department": "Cardiology"},
    {"id": "P102", "name": "Bob Jones", "department": "Neurology"},
    {"id": "P103", "name": "Charlie Brown", "department": "Cardiology"},
]

# 1. Exact Match Search (by Unique ID)
def search_by_id(record_id: str) -> Optional[Dict]:
    """Finds a single record by exact ID."""
    target_id = record_id.strip().upper()
    return next((item for item in patients if item["id"] == target_id), None)

# 2. Case-Insensitive Partial Search (by Name or Keyword)
def search_by_keyword(keyword: str) -> List[Dict]:
    """Finds all records matching a partial keyword."""
    term = keyword.strip().lower()
    return [
        item for item in patients 
        if term in item["name"].lower() or term in item["department"].lower()
    ]

# Usage Example:
if __name__ == "__main__":
    # Exact search
    patient = search_by_id("p102")
    print("Found by ID:", patient)

    # Partial/Keyword search
    results = search_by_keyword("cardio")
    print(f"Found {len(results)} matches for 'cardio':", results)