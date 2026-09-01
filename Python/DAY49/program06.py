import numpy as np


class DeterminantAnalyzer:
    """A comprehensive Determinant Analyzer implemented using pure NumPy."""

    def __init__(self, matrix):
        self.A = np.array(matrix, dtype=float)
        if self.A.ndim != 2:
            raise ValueError("Input must be a 2D matrix.")
        if self.A.shape[0] != self.A.shape[1]:
            raise ValueError(
                f"Determinant is only defined for square matrices. Got shape {self.A.shape}."
            )
        self.n = self.A.shape[0]

    # --- 1. Determinant Calculation Algorithms ---
    def det_numpy(self):
        """Standard NumPy determinant (LU decomposition based)."""
        return np.linalg.det(self.A)

    def det_eigenvalues(self):
        """Determinant via product of eigenvalues: det(A) = prod(lambda_i)."""
        eigenvalues = np.linalg.eigvals(self.A)
        return np.prod(eigenvalues)

    def det_laplace(self, M=None):
        """Laplace Expansion (Cofactor Expansion) - Recursive O(n!).

        Best suited for small matrices (n <= 4).
        """
        if M is None:
            M = self.A.copy()

        n = M.shape[0]
        if n == 1:
            return M[0, 0]
        if n == 2:
            return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]

        det = 0.0
        for c in range(n):
            minor = np.delete(np.delete(M, 0, axis=0), c, axis=1)
            cofactor = ((-1) ** c) * M[0, c] * self.det_laplace(minor)
            det += cofactor
        return det

    def det_gaussian_elimination(self):
        """Determinant via Triangularization (Gaussian Elimination) - O(n^3)."""
        M = self.A.copy()
        det = 1.0
        swaps = 0

        for i in range(self.n):
            # Partial pivoting
            pivot = np.argmax(np.abs(M[i:, i])) + i
            if np.isclose(M[pivot, i], 0.0):
                return 0.0

            if pivot != i:
                M[[i, pivot]] = M[[pivot, i]]
                swaps += 1

            det *= M[i, i]

            # Eliminate below
            for j in range(i + 1, self.n):
                factor = M[j, i] / M[i, i]
                M[j, i:] -= factor * M[i, i:]

        return det * ((-1) ** swaps)

    # --- 2. Geometric & Algebraic Insights ---
    def geometric_interpretation(self):
        """Interprets the scale factor of volume transformation."""
        det_val = self.det_numpy()
        mag = abs(det_val)

        if self.n == 2:
            unit = "area"
        elif self.n == 3:
            unit = "volume"
        else:
            unit = f"{self.n}-dimensional hypervolume"

        orientation = (
            "Preserves orientation"
            if det_val > 0
            else "Reverses orientation (Reflected)"
            if det_val < 0
            else "Collapses dimension"
        )

        return {
            "Scaling Factor": mag,
            "Orientation": orientation,
            "Description": f"Scales {unit} by a factor of {mag:.4f}.",
        }

    # --- 3. Matrix Stability & Singularity Checks ---
    def singularity_analysis(self, tol=1e-12):
        """Analyzes invertibility and ill-conditioning."""
        det_val = self.det_numpy()
        is_singular = np.isclose(det_val, 0.0, atol=tol)

        cond_num = (
            np.linalg.cond(self.A) if not is_singular else np.inf
        )

        return {
            "Is Singular": is_singular,
            "Is Invertible": not is_singular,
            "Condition Number": cond_num,
            "Ill-Conditioned": cond_num > 1e10 if not is_singular else True,
        }

    # --- 4. Full Analysis Report ---
    def analyze(self):
        det_val = self.det_numpy()

        report = {
            "Matrix Size": f"{self.n}x{self.n}",
            "Determinant (LU)": det_val,
            "Determinant (Eigenvalues)": self.det_eigenvalues(),
            "Determinant (Gaussian)": self.det_gaussian_elimination(),
            "Singularity Analysis": self.singularity_analysis(),
            "Geometric Property": self.geometric_interpretation(),
        }

        # Run Laplace expansion only for small matrices due to O(n!) complexity
        if self.n <= 4:
            report["Determinant (Laplace)"] = self.det_laplace()
        else:
            report["Determinant (Laplace)"] = (
                "Skipped (n > 4 is computationally expensive)"
            )

        return report


# --- Execution Example ---
if __name__ == "__main__":
    # Test matrix: 3x3 Non-singular matrix
    matrix_data = [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]

    analyzer = DeterminantAnalyzer(matrix_data)
    results = analyzer.analyze()

    print("=" * 60)
    print("              DETERMINANT ANALYSIS REPORT")
    print("=" * 60)

    for metric, val in results.items():
        print(f"\n[{metric}]")
        if isinstance(val, dict):
            for sub_k, sub_v in val.items():
                if isinstance(sub_v, float):
                    print(f"  {sub_k:<25}: {sub_v:.6f}")
                else:
                    print(f"  {sub_k:<25}: {sub_v}")
        elif isinstance(val, float):
            print(f"  {val:.6f}")
        else:
            print(f"  {val}")

    print("=" * 60)