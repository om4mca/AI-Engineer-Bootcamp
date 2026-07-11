#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Hospital Module
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------


import uuid
import math
from datetime import datetime

class Patient:
    def __init__(self, name: str, age: int, triage_symptom: str, base_fee: float):
        """
        Initializes a core patient record.
        triage_symptom maps to standard emergency severity indices.
        """
        self.patient_id = f"PAT-{str(uuid.uuid4())[:8].upper()}"
        self.name = name
        self.age = age
        self.triage_symptom = triage_symptom.lower()
        self.admission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.base_fee = base_fee

    def determine_triage_priority(self) -> str:
        """Categorizes urgency level based on symptom severity mapping."""
        critical_symptoms = ["chest pain", "shortness of breath", "severe trauma"]
        urgent_symptoms = ["high fever", "deep laceration", "abdominal pain"]
        
        if any(s in self.triage_symptom for s in critical_symptoms):
            return "LEVEL 1 - IMMEDIATE (Resuscitation/Emergent)"
        elif any(s in self.triage_symptom for s in urgent_symptoms):
            return "LEVEL 2 - URGENT (Fast-Track Assessment)"
        else:
            return "LEVEL 3 - NON-URGENT (Routine Medical Evaluation)"

    def calculate_final_invoice(self, insurance_discount_pct: float = 0.0) -> float:
        """
        Calculates hospital bill including standard 5% healthcare service tax,
        minus any active corporate insurance tier coverage.
        """
        if not (0.0 <= insurance_discount_pct <= 1.0):
            raise ValueError("Insurance discount percentage must stand between 0.0 and 1.0")
            
        tax_amount = self.base_fee * 0.05
        gross_total = self.base_fee + tax_amount
        
        discount_reduction = gross_total * insurance_discount_pct
        final_bill = gross_total - discount_reduction
        
        # Round up using ceiling for clean financial rounding thresholds
        return float(math.ceil(final_bill))

    def export_medical_profile(self, discount_pct: float = 0.0) -> dict:
        """Generates a secure administrative snapshot of active patient tracking metrics."""
        return {
            "Patient ID": self.patient_id,
            "Full Name": self.name,
            "Age": f"{self.age} yrs",
            "Admitted": self.admission_time,
            "Triage Status": self.determine_triage_priority(),
            "Total Balance Due": self.calculate_final_invoice(discount_pct)
        }