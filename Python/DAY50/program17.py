import numpy as np


class EigenvalueAnalyzer:
    """Spectral Analysis & Eigendecomposition Engine using NumPy."""

    def __init__(self, matrix):
        self.A = np.asarray(matrix, dtype=float)
        if self.A.ndim != 2 or self.A.shape[0] != self.A.shape[1]:
            raise ValueError(
                "Eigendecomposition requires a square matrix (n x n)."
            )
        self.n = self.A.shape[0]
        self._eigenvalues = None
        self._eigenvectors = None

    def compute_eigendecomposition(self) -> dict:
        """Computes Eigenvalues (λ) and Right Eigenvectors (v)."""
        self._eigenvalues, self._eigenvectors = np.linalg.eig(self.A)
        return {"eigenvalues": self._eigenvalues, "eigenvectors": self._eigenvectors}

    def analyze_spectral_properties(self) -> dict:
        """Performs structural spectral checks (Trace, Det relation, Spectral Radius)."""
        if self._eigenvalues is None:
            self.compute_eigendecomposition()

        evals = self._eigenvalues
        spectral_radius = float(np.max(np.abs(evals)))
        sum_evals = float(np.sum(evals))
        prod_evals = float(np.prod(evals))

        matrix_trace = float(np.trace(self.A))
        matrix_det = float(np.linalg.det(self.A))

        # Check if matrix is symmetric (guarantees real eigenvalues & orthogonal eigenvectors)
        is_symmetric = np.allclose(self.A, self.A.T)

        # Check Diagonalizability: Matrix is diagonalizable if it has n linearly independent eigenvectors
        rank_eigenvectors = np.linalg.matrix_rank(self._eigenvectors)
        is_diagonalizable = rank_eigenvectors == self.n

        return {
            "Matrix Dimension": f"{self.n}x{self.n}",
            "Is Symmetric?": is_symmetric,
            "Spectral Radius": round(spectral_radius, 4),
            "Sum of Eigenvalues": round(sum_evals, 4),
            "Matrix Trace": round(matrix_trace, 4),
            "Trace Matching Proof": np.isclose(sum_evals, matrix_trace),
            "Product of Eigenvalues": round(prod_evals, 4),
            "Matrix Determinant": round(matrix_det, 4),
            "Determinant Matching Proof": np.isclose(prod_evals, matrix_det),
            "Is Diagonalizable?": is_diagonalizable,
        }

    def get_characteristic_polynomial(self) -> np.ndarray:
        """Returns coefficients of characteristic polynomial p(λ) = det(A - λI)."""
        return np.poly(self.A)

    def verify_eigen_equation(self, index: int = 0) -> dict:
        """Verifies fundamental equation A*v = λ*v for a specific eigenvalue-eigenvector pair."""
        if self._eigenvalues is None:
            self.compute_eigendecomposition()

        lam = self._eigenvalues[index]
        v = self._eigenvectors[:, index]

        lhs = self.A @ v
        rhs = lam * v
        is_equal = np.allclose(lhs, rhs)

        return {
            "Eigenvalue (λ)": lam,
            "Eigenvector (v)": v,
            "A @ v": lhs,
            "λ * v": rhs,
            "A*v == λ*v Proof": is_equal,
        }


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("         EIGENVALUE ANALYZER SYSTEM         ")
    print("============================================\n")

    # Sample 3x3 Real Symmetric Matrix
    matrix_data = [
        [4.0, 2.0, 0.0],
        [2.0, 5.0, 3.0],
        [0.0, 3.0, 6.0],
    ]

    analyzer = EigenvalueAnalyzer(matrix_data)

    # 1. Compute Eigenvalues & Eigenvectors
    eig_data = analyzer.compute_eigendecomposition()
    print("--- [1] Eigenvalues & Eigenvectors ---")
    for idx, (lam, vec) in enumerate(
        zip(eig_data["eigenvalues"], eig_data["eigenvectors"].T)
    ):
        print(f"  λ_{idx+1} = {lam:.4f} | Eigenvector: {np.round(vec, 4)}")

    # 2. Spectral Properties Audit
    print("\n--- [2] Spectral Properties Audit ---")
    props = analyzer.analyze_spectral_properties()
    for key, val in props.items():
        print(f"  {key:<28}: {val}")

    # 3. Characteristic Polynomial
    print("\n--- [3] Characteristic Polynomial ---")
    poly_coeffs = analyzer.get_characteristic_polynomial()
    print("  Coefficients [λ^n, ..., λ^0]:", np.round(poly_coeffs, 4))

    # 4. Verify Equation (A * v == λ * v)
    print("\n--- [4] Verification of (A * v = λ * v) ---")
    verification = analyzer.verify_eigen_equation(index=0)
    print(f"  Selected λ         : {verification['Eigenvalue (λ)']:.4f}")
    print(f"  Proof Validated?   : {verification['A*v == λ*v Proof']}")