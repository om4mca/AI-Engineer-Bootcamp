import numpy as np


class LinearSystemVerifier:
    """Verifies candidate solutions x for a linear system Ax = b."""

    def __init__(self, A, b, x, tol=1e-7):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float).flatten()
        self.x = np.array(x, dtype=float).flatten()
        self.m, self.n = self.A.shape
        self.tol = tol

    # --- 1. Residual & Relative Error ---
    def compute_residuals(self):
        """Calculates residual vector r = Ax - b and relative error."""
        Ax = self.A @ self.x
        residual_vector = Ax - self.b
        residual_norm = np.linalg.norm(residual_vector)

        b_norm = np.linalg.norm(self.b)
        relative_error = (
            residual_norm / b_norm if b_norm > self.tol else residual_norm
        )

        return residual_vector, residual_norm, relative_error

    # --- 2. Orthogonality Condition (Least Squares Verification) ---
    def verify_least_squares_orthogonality(self, residual_vector):
        """Verifies if residual r is orthogonal to Column Space Col(A): A^T * r = 0."""
        normal_residual = self.A.T @ residual_vector
        normal_residual_norm = np.linalg.norm(normal_residual)
        is_least_squares = normal_residual_norm < self.tol
        return normal_residual, normal_residual_norm, is_least_squares

    # --- 3. Solution Status Classification ---
    def verify(self):
        res_vec, res_norm, rel_err = self.compute_residuals()
        norm_res_vec, norm_res_norm, is_lsq = (
            self.verify_least_squares_orthogonality(res_vec)
        )

        if res_norm < self.tol:
            status = "Exact Solution"
        elif is_lsq:
            status = "Valid Least-Squares Solution (Minimizes ||Ax - b||)"
        else:
            status = "Invalid Solution (Neither Exact nor Least-Squares)"

        return {
            "System Shape (m x n)": f"{self.m} x {self.n}",
            "Candidate x": self.x,
            "Residual Vector (Ax - b)": res_vec,
            "Absolute Residual Norm ||r||": res_norm,
            "Relative Error ||r|| / ||b||": rel_err,
            "Normal Residual ||A^T r||": norm_res_norm,
            "Satisfies Normal Equations (A^T A x = A^T b)": is_lsq,
            "Verification Status": status,
        }


# --- Execution Example ---
if __name__ == "__main__":
    print("=" * 65)
    print("           LINEAR SYSTEM SOLUTION VERIFICATION")
    print("=" * 65)

    A = np.array([[2.0, 1.0], [1.0, -1.0], [2.0, 1.0]])
    b = np.array([2.0, 0.0, 3.0])

    # Candidate 1: Exact solution attempt (will be invalid since system is inconsistent)
    x_exact_attempt = np.array([1.0, 0.0])
    # Candidate 2: Optimal Least-Squares solution x = (A^T A)^(-1) A^T b
    x_lsq = np.linalg.lstsq(A, b, rcond=None)[0]

    v1 = LinearSystemVerifier(A, b, x_exact_attempt).verify()
    v2 = LinearSystemVerifier(A, b, x_lsq).verify()

    print("\n--- Candidate 1 (Arbitrary/Invalid Candidate) ---")
    print(f"  Residual Norm ||r||      : {v1['Absolute Residual Norm ||r||']:.4f}")
    print(f"  Normal Residual ||A^T r||: {v1['Normal Residual ||A^T r||']:.4f}")
    print(f"  Status                   : {v1['Verification Status']}")

    print("\n--- Candidate 2 (Least-Squares Solution) ---")
    print(f"  Residual Norm ||r||      : {v2['Absolute Residual Norm ||r||']:.4f}")
    print(f"  Normal Residual ||A^T r||: {v2['Normal Residual ||A^T r||']:.4f}")
    print(f"  Status                   : {v2['Verification Status']}")

    print("=" * 65)