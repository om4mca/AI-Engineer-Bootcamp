#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:  Hospital Data Analysis — Python Version
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

import math

# Sample Input Data
patients = [
    {
        "id": 101,
        "name": "Om",
        "age": 42,
        "disease": "Fever"
    },
    {
        "id": 102,
        "name": "Raj",
        "age": 35,
        "disease": "Cold"
    },
    {
        "id": 103,
        "name": "Amit",
        "age": 29,
        "disease": "Fever"
    }
]


# ======================================================
# 10 Functional Modules Implementation
# ======================================================

# 1. Display All Patients
def display_all_patients(data):
    print("📋 All Patients List:")
    print(f"{'ID':<6} | {'Name':<10} | {'Age':<5} | {'Disease':<10}")
    print("-" * 40)
    for p in data:
        print(f"{p['id']:<6} | {p['name']:<10} | {p['age']:<5} | {p['disease']:<10}")

# 2. Find Average Age
def get_average_age(data):
    if not data:
        return 0
    total_age = sum(p["age"] for p in data)
    return total_age / len(data)

# 3. Find Oldest Patient
def get_oldest_patient(data):
    if not data:
        return None
    return max(data, key=lambda x: x["age"])

# 4. Find Youngest Patient
def get_youngest_patient(data):
    if not data:
        return None
    return min(data, key=lambda x: x["age"])

# 5. Search by Disease
def search_by_disease(data, disease_name):
    return [p for p in data if p["disease"].lower() == disease_name.lower()]

# 6. Count Patients by Disease
def count_patients_by_disease(data):
    disease_counts = {}
    for p in data:
        d = p["disease"]
        disease_counts[d] = disease_counts.get(d, 0) + 1
    return disease_counts

# 7. Filter Patients by Age (e.g., age > min_age)
def filter_by_age(data, min_age):
    return [p for p in data if p["age"] > min_age]

# 8. Find Duplicate Records (based on ID or Name & Age)
def find_duplicate_records(data):
    seen = set()
    duplicates = []
    for p in data:
        identifier = (p["id"], p["name"].lower())
        if identifier in seen:
            duplicates.append(p)
        else:
            seen.add(identifier)
    return duplicates

# 9. Validate Patient Data
def validate_patient_data(data):
    invalid_records = []
    for p in data:
        # Checking valid structure, positive age, non-empty fields
        if not isinstance(p.get("id"), int) or p.get("id") <= 0:
            invalid_records.append((p, "Invalid ID"))
        elif not isinstance(p.get("age"), int) or p.get("age") < 0 or p.get("age") > 120:
            invalid_records.append((p, "Invalid Age"))
        elif not p.get("name") or not isinstance(p["name"], str):
            invalid_records.append((p, "Invalid Name"))
        elif not p.get("disease") or not isinstance(p["disease"], str):
            invalid_records.append((p, "Invalid Disease"))
    return invalid_records

# 10. Generate Summary Report
def generate_summary_report(data):
    total_patients = len(data)
    avg_age = get_average_age(data)
    oldest = get_oldest_patient(data)
    youngest = get_youngest_patient(data)
    disease_summary = count_patients_by_disease(data)

    print("====== HOSPITAL DATA ANALYSIS ======")
    print()
    print(f"Total Patients: {total_patients}")
    print()
    print(f"Average Age: {avg_age:.2f}")
    print()
    print(f"Oldest Patient: {oldest['name'] if oldest else 'N/A'}")
    print()
    print(f"Youngest Patient: {youngest['name'] if youngest else 'N/A'}")
    print()
    print("Disease Summary:")
    print()
    for disease, count in disease_summary.items():
        print(f"{disease}: {count}")


# ======================================================
# Execution
# ======================================================
if __name__ == "__main__":
    
    # Validation Check
    invalid_records = validate_patient_data(patients)
    if invalid_records:
        print("⚠️ Found Invalid Records:", invalid_records)
    
    # Generate Output Report
    generate_summary_report(patients)