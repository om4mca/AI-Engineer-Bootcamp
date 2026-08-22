import math

class EmployeeVector:
    def __init__(self, employee_id: str, age: float, experience: float, 
                 projects: float, performance: float, salary: float):
        self.employee_id = employee_id
        # Numerical feature vector: [Age, Experience, Projects, Performance, Salary]
        self.vector = [float(age), float(experience), float(projects), 
                       float(performance), float(salary)]
        self.feature_names = ["Age", "Experience", "Projects", "Performance", "Salary"]

    @property
    def dimension(self) -> int:
        """Calculate vector dimension (number of elements)."""
        return len(self.vector)

    def add(self, other: 'EmployeeVector') -> list:
        """Element-wise addition of two vectors."""
        self._check_dimension(other)
        return [a + b for a, b in zip(self.vector, other.vector)]

    def subtract(self, other: 'EmployeeVector') -> list:
        """Element-wise subtraction of two vectors (Difference Vector)."""
        self._check_dimension(other)
        return [a - b for a, b in zip(self.vector, other.vector)]

    def scale(self, scalar: float) -> list:
        """Scalar multiplication: multiplies every element by a constant."""
        return [scalar * x for x in self.vector]

    def dot_product(self, other: 'EmployeeVector') -> float:
        """Calculates dot product (sum of element-wise products)."""
        self._check_dimension(other)
        return sum(a * b for a, b in zip(self.vector, other.vector))

    def magnitude(self) -> float:
        """Calculates Euclidean Norm (L2 Norm / vector length)."""
        return math.sqrt(sum(x ** 2 for x in self.vector))

    def normalize(self) -> list:
        """Converts vector to a unit vector (Magnitude = 1.0)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return [x / mag for x in self.vector]

    def _check_dimension(self, other: 'EmployeeVector'):
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have identical dimensions.")

    def __repr__(self):
        return f"Employee({self.employee_id}) -> {self.vector}"


# ==============================================================================
# DEMONSTRATION & VECTOR MATHEMATICS
# ==============================================================================

# Define two employees as feature vectors
emp_A = EmployeeVector(employee_id="EMP-101", age=28, experience=4, projects=8, performance=4.2, salary=75000)
emp_B = EmployeeVector(employee_id="EMP-102", age=45, experience=20, projects=25, performance=4.8, salary=140000)

print(f"Vector A ({emp_A.employee_id}): {emp_A.vector}")
print(f"Vector B ({emp_B.employee_id}): {emp_B.vector}\n")

# 1. Dimension
print(f"1. Vector Dimension: {emp_A.dimension}D space")

# 2. Vector Addition
vec_add = emp_A.add(emp_B)
print(f"2. Vector Addition (A + B): {vec_add}")

# 3. Vector Subtraction
vec_sub = emp_A.subtract(emp_B)
print(f"3. Vector Subtraction (A - B): {vec_sub}")

# 4. Scalar Scaling (e.g., projecting a 10% increase across all metrics)
vec_scaled = emp_A.scale(1.10)
print(f"4. Scaled Vector (A * 1.10): {[round(x, 2) for x in vec_scaled]}")

# 5. Dot Product
dot_prod = emp_A.dot_product(emp_B)
print(f"5. Dot Product (A · B): {dot_prod:,.2f}")

# 6. Magnitude (L2 Norm)
mag_A = emp_A.magnitude()
print(f"6. Magnitude of A (||A||): {mag_A:,.2f}")

# 7. Normalization (Unit Vector)
unit_A = emp_A.normalize()
print(f"7. Normalized Unit Vector A: {[round(x, 6) for x in unit_A]}")