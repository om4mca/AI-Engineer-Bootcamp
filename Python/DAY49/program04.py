import numpy as np


class MatrixAnalyzer:
    """A comprehensive Matrix Operations Analyzer built purely with NumPy."""

    def __init__(self, matrix):
        self.A = np.array(matrix, dtype=float)
        if self.A.ndim != 2:
            raise ValueError("Input must be a 2D matrix.")
        self.rows, self.cols = self.A.shape
        self.is_square = self.rows == self.cols

    # --- 1. Basic Properties & Scalar Metrics ---
    def trace(self):
        """Sum of diagonal elements (Square matrices only)."""
        if not self.is_square:
            return "Undefined (Matrix must be square)"
        return np.trace(self.A)

    def determinant(self):
        """Determinant of the matrix (Square matrices only)."""
        if not self.is_square:
            return "Undefined (Matrix must be square)"
        return np.linalg.det(self.A)

    def rank(self):
        """Number of linearly independent rows/columns."""
        return np.linalg.matrix_rank(self.A)

    def condition_number(self):
        """Condition number (Sensitivity to small perturbations)."""
        return np.linalg.cond(self.A)

    def inverse(self):
        """Matrix inverse (A^-1) or Moore-Penrose Pseudoinverse (A^+)."""
        if self.is_square and not np.isclose(self.determinant(), 0):
            return np.linalg.inv(self.A), "Exact Inverse (A^-1)"
        return np.linalg.pinv(self.A), "Moore-Penrose Pseudoinverse (A^+)"

    # --- 2. Structural Property Checks ---
    def is_symmetric(self):
        return self.is_square and np.allclose(self.A, self.A.T)

    def is_orthogonal(self):
        if not self.is_square:
            return False
        return np.allclose(self.A @ self.A.T, np.eye(self.rows))

    def is_positive_definite(self):
        """Checks if all eigenvalues are strictly positive."""
        if not self.is_symmetric():
            return False
        eigenvalues = np.linalg.eigvalsh(self.A)
        return np.all(eigenvalues > 0)

    # --- 3. Matrix Norms ---
    def norms(self):
        """Computes standard matrix norms."""
        norms_dict = {
            "Frobenius Norm": np.linalg.norm(self.A, "fro"),
            "Spectral Norm (L2)": np.linalg.norm(self.A, 2),
            "L1 Norm (Max Col Sum)": np.linalg.norm(self.A, 1),
            "L-infinity Norm (Max Row Sum)": np.linalg.norm(self.A, np.inf),
        }
        if self.is_square:
            norms_dict["Nuclear Norm (Trace Norm)"] = np.linalg.norm(
                self.A, "nuc"
            )
        return norms_dict

    # --- 4. Matrix Decompositions ---
    def eigendecomposition(self):
        """Computes eigenvalues and eigenvectors (Square matrices only)."""
        if not self.is_square:
            return "Undefined (Matrix must be square)"
        eigenvalues, eigenvectors = np.linalg.eig(self.A)
        return {"eigenvalues": eigenvalues, "eigenvectors": eigenvectors}

    def svd(self):
        """Singular Value Decomposition: A = U * S * V^T."""
        U, S, Vt = np.linalg.svd(self.A)
        return {"U": U, "Singular Values (S)": S, "V_transpose": Vt}

    def qr_decomposition(self):
        """QR Decomposition: A = Q * R."""
        Q, R = np.linalg.qr(self.A)
        return {"Q": Q, "R": R}

    def cholesky_decomposition(self):
        """Cholesky Decomposition: A = L * L^T (Symmetric Positive-Definite only)."""
        if not self.is_positive_definite():
            return "Undefined (Matrix must be symmetric positive-definite)"
        L = np.linalg.cholesky(self.A)
        return {"L (Lower Triangular)": L}

    # --- 5. Comprehensive Analysis Report ---
    def analyze(self):
        inv_mat, inv_type = self.inverse()

        report = {
            "Dimensions": f"{self.rows} x {self.cols}",
            "Is Square": self.is_square,
            "Is Symmetric": self.is_symmetric(),
            "Is Orthogonal": self.is_orthogonal(),
            "Is Positive Definite": self.is_positive_definite(),
            "Rank": self.rank(),
            "Trace": self.trace(),
            "Determinant": self.determinant(),
            "Condition Number": self.condition_number(),
            f"Inverse ({inv_type})": inv_mat,
            "Matrix Norms": self.norms(),
            "SVD Singular Values": self.svd()["Singular Values (S)"],
        }

        if self.is_square:
            report["Eigenvalues"] = self.eigendecomposition()["eigenvalues"]

        return report


# --- Execution Example ---
if __name__ == "__main__":
    # Test matrix (3x3 Symmetric Positive-Definite Matrix)
    matrix_data = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]

    analyzer = MatrixAnalyzer(matrix_data)
    results = analyzer.analyze()

    print("=" * 60)
    print("           PURE NUMPY MATRIX ANALYSIS REPORT")
    print("=" * 60)

    for metric, val in results.items():
        print(f"\n[{metric}]")
        if isinstance(val, np.ndarray):
            print(np.round(val, 4))
        elif isinstance(val, dict):
            for sub_k, sub_v in val.items():
                if isinstance(sub_v, float):
                    print(f"  {sub_k:<30}: {sub_v:.4f}")
                else:
                    print(f"  {sub_k:<30}: {sub_v}")
        elif isinstance(val, float):
            print(f"{val:.4f}")
        else:
            print(val)

    print("=" * 60)