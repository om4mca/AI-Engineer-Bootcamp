import numpy as np

class EmployeeMatrixAnalyzer:
    """
    Analyzes employee feature matrices for numerical stability, 
    collinearity, determinism, and invertibility.
    """
    def __init__(self, tolerance: float = 1e-8):
        self.tolerance = tolerance

    def analyze(self, name: str, matrix: list | np.ndarray) -> dict:
        A = np.asarray(matrix, dtype=float)
        results = {
            "name": name,
            "matrix": A,
            "shape": A.shape,
            "is_square": False,
            "det": None,
            "status": "Invalid",
            "inverse": None,
            "verified": False
        }

        # 1. Dimension Check
        if A.ndim != 2 or A.shape[0] != A.shape[1]:
            results["status"] = "Non-Square Matrix (Cannot compute determinant)"
            return results
        
        results["is_square"] = True

        # 2. Compute Determinant
        det = np.linalg.det(A)
        results["det"] = round(det, 6)

        # 3. Invertibility & Exception Handling
        if np.isclose(det, 0.0, atol=self.tolerance):
            results["status"] = "Singular Matrix (Redundant/Collinear Features — Det = 0)"
        else:
            try:
                inv = np.linalg.inv(A)
                results["inverse"] = np.round(inv, 4)
                
                # 4. Verify Identity (A @ Inverse ≈ I)
                identity_check = A @ inv
                results["verified"] = np.allclose(identity_check, np.eye(A.shape[0]), atol=self.tolerance)
                results["status"] = "Non-Singular (Fully Invertible)"
            except np.linalg.LinAlgError:
                results["status"] = "Singular (LinAlgError during inversion)"

        return results

    def print_report(self, results: dict):
        print("=" * 60)
        print(f"  ANALYSIS REPORT: {results['name'].upper()}")
        print("=" * 60)
        print(f"Matrix Input:\n{results['matrix']}")
        print(f"Shape: {results['shape']}")
        
        if not results["is_square"]:
            print(f"Status: {results['status']}\n")
            return

        print(f"Determinant: {results['det']}")
        print(f"Status: {results['status']}")

        if results["inverse"] is not None:
            print(f"\nInverse Matrix:\n{results['inverse']}")
            print(f"Verification Check (A @ Inverse ≈ Identity): {'PASSED ✅' if results['verified'] else 'FAILED ❌'}")
        else:
            print("Inverse: N/A (Cannot invert singular matrix)")
        print()


# ----------------------------------------------------
# Example Employee Datasets
# ----------------------------------------------------

datasets = {
    "Engineering Team (Distinct Features)": [
        [4, 85],   # [Years Experience, Tech Score]
        [2, 60]
    ],
    
    "Sales Team (Collinear/Duplicate Scale)": [
        [5, 50],   # Feature 2 is exactly 10x Feature 1
        [8, 80]
    ],
    
    "Management Cohort (3x3 Matrix)": [
        [10, 90, 5],  # [Tenure, Performance, Direct Reports]
        [3,  75, 1],
        [7,  80, 3]
    ]
}

# Run Analyzer
analyzer = EmployeeMatrixAnalyzer()

for title, data in datasets.items():
    res = analyzer.analyze(title, data)
    analyzer.print_report(res)