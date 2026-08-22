import numpy as np

class PatientVector:
    def __init__(self, patient_id: str, age: float, weight_kg: float, 
                 blood_pressure: float, stay_days: float, bill_usd: float):
        self.patient_id = patient_id
        # Feature Vector: [Age, Weight (kg), Blood Pressure (systolic), Stay Days, Total Bill ($)]
        self.vector = np.array([float(age), float(weight_kg), float(blood_pressure), 
                                float(stay_days), float(bill_usd)])
        self.feature_names = ["Age", "Weight", "BP", "Stay_Days", "Bill"]

    def magnitude(self) -> float:
        """Euclidean Norm (L2 Length)."""
        return np.linalg.norm(self.vector)

    def normalize(self) -> np.ndarray:
        """Unit Vector conversion (Magnitude = 1.0)."""
        return self.vector / self.magnitude()

    def euclidean_distance(self, other: 'PatientVector') -> float:
        """Straight-line distance between two patient profiles."""
        return np.linalg.norm(self.vector - other.vector)

    def cosine_similarity(self, other: 'PatientVector') -> float:
        """Directional alignment (angle) between two patient profiles."""
        return np.dot(self.vector, other.vector) / (self.magnitude() * other.magnitude())

# --- DEMONSTRATION ---
# Patient 1: ICU Admission (High stay, high bill)
p1 = PatientVector("PAT-101", age=68, weight_kg=85.0, blood_pressure=145.0, stay_days=14, bill_usd=28000.0)

# Patient 2: Routine Outpatient
p2 = PatientVector("PAT-102", age=32, weight_kg=65.0, blood_pressure=118.0, stay_days=2, bill_usd=1800.0)

print(f"Patient 1 Vector: {p1.vector}")
print(f"Patient 2 Vector: {p2.vector}\n")

print(f"1. Difference Vector (P1 - P2): {p1.vector - p2.vector}")
print(f"2. Raw Euclidean Distance:      {p1.euclidean_distance(p2):,.2f}")
print(f"3. Cosine Similarity (0 to 1):  {p1.cosine_similarity(p2):.4f}")
print(f"4. P1 Normalized Unit Vector:   {np.round(p1.normalize(), 6)}")