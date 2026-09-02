import numpy as np


class MatrixAnalysisSystem:
    """Production-Grade Matrix Analysis and Structural Diagnostic Engine using NumPy."""

    def __init__(self, matrix):
        self.A = np.asarray(matrix, dtype=float)
        if self.A.ndim != 2:
            raise ValueError("Input dataset must be a 2D matrix.")
        self.rows, self.cols = self.A.shape

    @property
    def is_square(self) -> bool:
        """Check karta hai ki matrix square (n x n) hai ya nahi."""
        return self.rows == self.cols

    def analyze_structural_properties(self) -> dict:
        """Matrix ke core algebraic properties audit karta hai."""
        rank = np.linalg.matrix_rank(self.A)
        det = np.linalg.det(self.A) if self.is_square else None
        trace = np.trace(self.A) if self.is_square else None
        cond_num = np.linalg.cond(self.A)

        # Symmetry & Orthogonality Checks
        is_symmetric = (
            np.allclose(self.A, self.A.T) if self.is_square else False
        )
        is_orthogonal = (
            np.allclose(self.A.T @ self.A, np.eye(self.rows))
            if self.is_square
            else False
        )

        return {
            "Shape": (self.rows, self.cols),
            "Matrix Rank": rank,
            "Full Rank?": rank == min(self.rows, self.cols),
            "Determinant": det,
            "Trace": trace,
            "Condition Number": cond_num,
            "Is Symmetric?": is_symmetric,
            "Is Orthogonal?": is_orthogonal,
        }

    def compute_norms(self) -> dict:
        """Matrix Norms calculate karta hai (L1, L2, Frobenius, Infinity)."""
        return {
            "Frobenius Norm": np.linalg.norm(self.A, "fro"),
            "L1 Norm (Max Col Sum)": np.linalg.norm(self.A, 1),
            "Infinity Norm (Max Row Sum)": np.linalg.norm(self.A, np.inf),
            "L2 / Spectral Norm": np.linalg.norm(self.A, 2),
        }

    def matrix_inversion(self) -> np.ndarray:
        """Inverse calculate karta hai (agar singular na ho) ya Pseudo-Inverse return karta hai."""
        if self.is_square and abs(np.linalg.det(self.A)) > 1e-10:
            return np.linalg.inv(self.A)
        return np.linalg.pinv(self.A)

    def perform_svd(self) -> dict:
        """Singular Value Decomposition (A = U * S * Vt) compute karta hai."""
        U, S, Vt = np.linalg.svd(self.A)
        return {"U": U, "Singular Values (S)": S, "Vt": Vt}

    def perform_qr_decomposition(self) -> dict:
        """QR Decomposition (A = Q * R) calculate karta hai."""
        Q, R = np.linalg.qr(self.A)
        return {"Q": Q, "R": R}


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("      MATRIX ANALYSIS SYSTEM (NUMPY)        ")
    print("============================================\n")

    # 1. Matrix Initialization (3x3 Real-Valued Matrix)
    matrix_data = [
        [4.0, 1.0, -2.0],
        [1.0, 5.0, 0.0],
        [-2.0, 0.0, 3.0],
    ]

    analyzer = MatrixAnalysisSystem(matrix_data)

    # 2. Structural Property Inspection
    print("--- [1] Structural & Algebraic Properties ---")
    props = analyzer.analyze_structural_properties()
    for key, val in props.items():
        if isinstance(val, float):
            print(f"  {key:<24}: {val:.4f}")
        else:
            print(f"  {key:<24}: {val}")

    # 3. Norm Calculations
    print("\n--- [2] Matrix Norms ---")
    norms = analyzer.compute_norms()
    for norm_name, val in norms.items():
        print(f"  {norm_name:<26}: {val:.4f}")

    # 4. QR Decomposition Proof (A = Q @ R)
    print("\n--- [3] QR Decomposition ---")
    qr_res = analyzer.perform_qr_decomposition()
    Q, R = qr_res["Q"], qr_res["R"]
    print("Matrix Q (Orthogonal):\n", np.round(Q, 3))
    print("Matrix R (Upper Triangular):\n", np.round(R, 3))
    print("Verification (Q @ R == A)?", np.allclose(Q @ R, analyzer.A))

    # 5. Singular Value Decomposition (SVD)
    print("\n--- [4] Singular Value Decomposition (SVD) ---")
    svd_res = analyzer.perform_svd()
    print("Singular Values:", np.round(svd_res["Singular Values (S)"], 4))