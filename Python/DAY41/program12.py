import numpy as np

class EmployeeVector:
    def __init__(self, emp_id: str, age: float, experience_years: float, 
                 salary_k: float, projects_completed: float, performance_score: float):
        self.emp_id = emp_id
        # Vector: [Age, Experience (yrs), Salary ($k), Projects Completed, Performance Rating (1-5)]
        self.vector = np.array([float(age), float(experience_years), 
                                float(salary_k), float(projects_completed), 
                                float(performance_score)])
        self.feature_names = ["Age", "Experience", "Salary_k", "Projects", "Rating"]

    def magnitude(self) -> float:
        """Euclidean Norm (L2 Length)."""
        return np.linalg.norm(self.vector)

    def normalize(self) -> np.ndarray:
        """Unit Vector conversion (Magnitude = 1.0)."""
        return self.vector / self.magnitude()

    def euclidean_distance(self, other: 'EmployeeVector') -> float:
        """Straight-line distance between two employee profiles."""
        return np.linalg.norm(self.vector - other.vector)

    def cosine_similarity(self, other: 'EmployeeVector') -> float:
        """Directional alignment between two employee profiles."""
        return np.dot(self.vector, other.vector) / (self.magnitude() * other.magnitude())

# --- DEMONSTRATION ---
emp1 = EmployeeVector("EMP-101", age=28, experience_years=4, salary_k=85.0, projects_completed=12, performance_score=4.2)
emp2 = EmployeeVector("EMP-102", age=45, experience_years=18, salary_k=160.0, projects_completed=45, performance_score=4.8)

print(f"Employee 1 Vector: {emp1.vector}")
print(f"Employee 2 Vector: {emp2.vector}\n")

print(f"1. Difference Vector (EMP2 - EMP1): {emp2.vector - emp1.vector}")
print(f"2. Raw Euclidean Distance:          {emp1.euclidean_distance(emp2):.2f}")
print(f"3. Cosine Similarity (0 to 1):      {emp1.cosine_similarity(emp2):.4f}")
print(f"4. EMP1 Normalized Unit Vector:     {np.round(emp1.normalize(), 4)}")