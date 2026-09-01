import numpy as np


class MatrixInverseVerifier:
    """A comprehensive verification engine to test if Matrix B is the inverse of Matrix A."""

    def __init__(self, A, B, rtol=1e-5, atol=1e-8):
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)
        self.rtol = rtol
        self.atol = atol

        if self.A.ndim != 2 or self.B.ndim != 2:
            raise ValueError("Both inputs must be 2D matrices.")

        self.rows_A, self.cols_A = self.A.shape
        self.rows_B, self.cols_B = self.B.shape
        self.is_square = (self.rows_A == self.cols_A) and (
            self.rows_B == self.cols_B
        )

    # --- 1. Right and Left Residual Calculations ---
    def compute_residuals(self):
        """Computes ||A * B - I|| and ||B * A - I|| using the Frobenius norm."""
        if not self.is_square or (self.cols_A != self.rows_B):
            return None, None

        I_n = np.eye(self.rows_A)

        # Compute product matrices
        AB = self.A @ self.B
        BA = self.B @ self.A

        # Calculate residual errors against identity matrix
        right_residual = np.linalg.norm(AB - I_n, ord="fro")
        left_residual = np.linalg.norm(BA - I_n, ord="fro")

        return right_residual, left_residual

    # --- 2. Numerical Identity Equality Check ---
    def is_exact_inverse(self):
        """Checks if A * B and B * A equal Identity within tolerance limits."""
        if not self.is_square or (self.shape_match() is False):
            return False

        I_n = np.eye(self.rows_A)
        right_valid = np.allclose(
            self.A @ self.B, I_n, rtol=self.rtol, atol=self.atol
        )
        left_valid = np.allclose(
            self.B @ self.A, I_n, rtol=self.rtol, atol=self.atol
        )

        return right_valid and left_valid

    # --- 3. Matrix Conditioning & Singularity Check ---
    def check_conditioning(self):
        """Evaluates determinant and condition number to check numerical stability."""
        if not self.is_square:
            return {"Status": "Non-Square Matrix"}

        det_A = np.linalg.det(self.A)
        cond_A = np.linalg.cond(self.A)

        return {
            "Determinant det(A)": det_A,
            "Condition Number cond(A)": cond_A,
            "Is Singular": np.isclose(det_A, 0.0),
            "Ill-Conditioned": cond_A > (1.0 / self.rtol),
        }

    # --- 4. Pseudoinverse Verification (For Rectangular/Singular) ---
    def verify_pseudoinverse(self):
        """Verifies 4 Penrose Conditions for Moore-Penrose Pseudoinverse:

        1. A * B * A = A
        2. B * A * B = B
        3. (A * B)^T = A * B
        4. (B * A)^T = B * A
        """
        c1 = np.allclose(
            self.A @ self.B @ self.A, self.A, rtol=self.rtol, atol=self.atol
        )
        c2 = np.allclose(
            self.B @ self.A @ self.B, self.B, rtol=self.rtol, atol=self.atol
        )
        c3 = np.allclose(
            (self.A @ self.B).T, self.A @ self.B, rtol=self.rtol, atol=self.atol
        )
        c4 = np.allclose(
            (self.B @ self.A).T, self.B @ self.A, rtol=self.rtol, atol=self.atol
        )

        return {
            "ABA == A": c1,
            "BAB == B": c2,
            "(AB)^T == AB": c3,
            "(BA)^T == BA": c4,
            "Is Valid Pseudoinverse": c1 and c2 and c3 and c4,
        }

    def shape_match(self):
        return (
            self.rows_A == self.cols_A
            and self.rows_B == self.cols_B
            and self.rows_A == self.rows_B
        )

    # --- 5. Full Verification Report ---
    def verify(self):
        right_res, left_res = self.compute_residuals()
        is_inv = self.is_exact_inverse()
        cond_info = self.check_conditioning()
        pseudo_info = self.verify_pseudoinverse()

        return {
            "Matrix A Shape": f"{self.rows_A}x{self.cols_A}",
            "Matrix B Shape": f"{self.rows_B}x{self.cols_B}",
            "Is True Inverse": is_inv,
            "Right Residual ||A*B - I||_F": (
                f"{right_res:.2e}" if right_res is not None else "N/A"
            ),
            "Left Residual ||B*A - I||_F": (
                f"{left_res:.2e}" if left_res is not None else "N/A"
            ),
            "Conditioning": cond_info,
            "Moore-Penrose Conditions": pseudo_info,
        }


# --- Execution Example ---
if __name__ == "__main__":
    # Define Matrix A
    A = np.array([[2.0, 1.0], [5.0, 3.0]])

    # Generate exact inverse B
    B_exact = np.linalg.inv(A)

    # Generate slightly noisy inverse candidate B
    B_noisy = B_exact + np.array([[0.001, -0.002], [0.0005, 0.001]])

    print("=" * 60)
    print("      MATRIX INVERSE VERIFICATION SYSTEM REPORT")
    print("=" * 60)

    # Verify Exact Inverse
    verifier_exact = MatrixInverseVerifier(A, B_exact)
    print("\n--- Test 1: Exact Inverse Verification ---")
    for k, v in verifier_exact.verify().items():
        print(f"{k:<32}: {v}")

    # Verify Noisy Inverse
    verifier_noisy = MatrixInverseVerifier(A, B_noisy)
    print("\n--- Test 2: Noisy Candidate Verification ---")
    for k, v in verifier_noisy.verify().items():
        print(f"{k:<32}: {v}")

    print("=" * 60)