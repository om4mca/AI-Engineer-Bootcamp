import math

class PatientVector:
    def __init__(self, patient_id: str, age: float, weight: float, 
                 blood_pressure: float, stay_days: float, bill: float):
        self.patient_id = patient_id
        # Feature Vector: [Age, Weight, Blood Pressure, Stay Days, Bill]
        self.vector = [float(age), float(weight), float(blood_pressure), 
                       float(stay_days), float(bill)]
        self.feature_names = ["Age", "Weight", "Blood Pressure", "Stay Days", "Bill"]

    @property
    def dimension(self) -> int:
        return len(self.vector)

    def add(self, other: 'PatientVector') -> list:
        """Element-wise addition."""
        self._check_dimension(other)
        return [a + b for a, b in zip(self.vector, other.vector)]

    def subtract(self, other: 'PatientVector') -> list:
        """Element-wise subtraction (Difference Vector)."""
        self._check_dimension(other)
        return [a - b for a, b in zip(self.vector, other.vector)]

    def scale(self, scalar: float) -> list:
        """Scalar multiplication."""
        return [scalar * x for x in self.vector]

    def dot_product(self, other: 'PatientVector') -> float:
        """Sum of element-wise products."""
        self._check_dimension(other)
        return sum(a * b for a, b in zip(self.vector, other.vector))

    def magnitude(self) -> float:
        """Euclidean Norm (L2 Norm)."""
        return math.sqrt(sum(x ** 2 for x in self.vector))

    def normalize(self) -> list:
        """Unit Vector conversion (Magnitude = 1.0)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return [x / mag for x in self.vector]

    def _check_dimension(self, other: 'PatientVector'):
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have identical dimensions.")


# --- DEMONSTRATION ---
p1 = PatientVector("PAT-101", age=65, weight=85.0, blood_pressure=140.0, stay_days=12, bill=15000.0)
p2 = PatientVector("PAT-102", age=30, weight=68.0, blood_pressure=120.0, stay_days=3, bill=2500.0)

print(f"Patient 1 Vector: {p1.vector}")
print(f"Patient 2 Vector: {p2.vector}\n")

print(f"1. Addition (P1 + P2):          {p1.add(p2)}")
print(f"2. Subtraction (P1 - P2):       {p1.subtract(p2)}")
print(f"3. Scalar Scaling (P1 * 1.10):  {[round(x, 2) for x in p1.scale(1.10)]}")
print(f"4. Dot Product (P1 · P2):       {p1.dot_product(p2):,.2f}")
print(f"5. Magnitude ||P1||:            {p1.magnitude():,.2f}")
print(f"6. Normalized Unit Vector P1:   {[round(x, 6) for x in p1.normalize()]}")