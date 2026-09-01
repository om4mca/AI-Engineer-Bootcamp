import numpy as np


class EigenAnalyzer:
    """A comprehensive Eigenvalue & Eigenvector Analyzer built using pure NumPy."""

    def __init__(self, matrix, tol=1e-7):
        self.A = np.array(matrix, dtype=float)
        if self.A.ndim != 2 or self.A.shape[0] != self.A.shape[1]:
            raise ValueError(
                f"Eigen spectral analysis requires a square 2D matrix. Got shape {self.A.shape}."
            )
        self.n = self.A.shape[0]
        self.tol = tol

    # --- 1. Eigenvalue & Eigenvector Computation ---
    def compute_spectrum(self):
        """Computes eigenvalues and right eigenvectors satisfying A * v = lambda * v."""
        eigenvalues, eigenvectors = np.linalg.eig(self.A)
        return eigenvalues, eigenvectors

    # --- 2. Spectral Verification ---
    def verify_eigen_equation(self, eigenvalues, eigenvectors):
        """Verifies ||A * v_i - lambda_i * v_i||_2 for each eigenpair."""
        residuals = []
        for i in range(self.n):
            lam = eigenvalues[i]
            v = eigenvectors[:, i]
            res = np.linalg.norm(self.A @ v - lam * v)
            residuals.append(res)
        return np.array(residuals)

    # --- 3. Multiplicities & Diagonalizability ---
    def check_multiplicities_and_diagonalizability(
        self, eigenvalues, eigenvectors
    ):
        """Calculates Algebraic vs.

        Geometric Multiplicity and checks diagonalizability.
        """
        # Round eigenvalues to group duplicates within tolerance
        rounded_eigs = np.round(eigenvalues, decimals=6)
        unique_eigs, algebraic_mults = np.unique(
            rounded_eigs, return_counts=True
        )

        spectral_info = {}
        total_geometric_mult = 0

        for idx, lam in enumerate(unique_eigs):
            alg_mult = algebraic_mults[idx]

            # Geometric multiplicity = nullity of (A - lambda * I)
            shift_matrix = self.A - lam * np.eye(self.n)
            nullity = self.n - np.linalg.matrix_rank(
                shift_matrix, tol=self.tol
            )
            geo_mult = nullity

            spectral_info[lam] = {
                "Algebraic Multiplicity": int(alg_mult),
                "Geometric Multiplicity": int(geo_mult),
                "Defective": geo_mult < alg_mult,
            }
            total_geometric_mult += geo_mult

        is_diagonalizable = total_geometric_mult == self.n

        return spectral_info, is_diagonalizable

    # --- 4. Conservation Laws & Spectral Metrics ---
    def verify_conservation_laws(self, eigenvalues):
        """Verifies Trace = Sum(Eigenvalues) and Det = Product(Eigenvalues)."""
        trace_exact = np.trace(self.A)
        det_exact = np.linalg.det(self.A)

        sum_eigs = np.sum(eigenvalues)
        prod_eigs = np.prod(eigenvalues)

        return {
            "Exact Trace": trace_exact,
            "Sum of Eigenvalues": sum_eigs,
            "Trace Conservation Match": np.isclose(trace_exact, sum_eigs),
            "Exact Determinant": det_exact,
            "Product of Eigenvalues": prod_eigs,
            "Determinant Conservation Match": np.isclose(det_exact, prod_eigs),
        }

    def spectral_radius(self, eigenvalues):
        """Spectral Radius rho(A) = max(|lambda_i|)."""
        return np.max(np.abs(eigenvalues))

    # --- 5. Reconstruction / Spectral Decomposition ---
    def reconstruct_matrix(self, eigenvalues, eigenvectors):
        """Reconstructs A = V * Lambda * V^-1 if matrix is diagonalizable."""
        V = eigenvectors
        Lambda = np.diag(eigenvalues)

        try:
            V_inv = np.linalg.inv(V)
            A_reconstructed = V @ Lambda @ V_inv
            reconstruction_error = np.linalg.norm(
                self.A - A_reconstructed, ord="fro"
            )
            return A_reconstructed, reconstruction_error
        except np.linalg.LinAlgError:
            return None, "Matrix V is singular (non-diagonalizable)"

    # --- 6. Comprehensive Analysis Report ---
    def analyze(self):
        eigs, vecs = self.compute_spectrum()
        residuals = self.verify_eigen_equation(eigs, vecs)
        spectral_info, is_diag = (
            self.check_multiplicities_and_diagonalizability(eigs, vecs)
        )
        conservation = self.verify_conservation_laws(eigs)
        A_rec, rec_err = self.reconstruct_matrix(eigs, vecs)

        return {
            "Matrix Shape": f"{self.n}x{self.n}",
            "Eigenvalues": eigs,
            "Eigenvectors (Columns)": vecs,
            "Max Verification Residual ||Av - lambda*v||": np.max(residuals),
            "Spectral Radius rho(A)": self.spectral_radius(eigs),
            "Is Diagonalizable": is_diag,
            "Multiplicity Analysis": spectral_info,
            "Conservation Laws": conservation,
            "Spectral Reconstruction Error ||A - V*Lambda*V^-1||_F": rec_err,
        }


# --- Execution Example ---
if __name__ == "__main__":
    # Test matrix: 3x3 Real Symmetric Matrix (Guaranteed Real Eigenvalues and Diagonalizable)
    matrix_data = [[4.0, 2.0, 0.0], [2.0, 5.0, 3.0], [0.0, 3.0, 6.0]]

    analyzer = EigenAnalyzer(matrix_data)
    results = analyzer.analyze()

    print("=" * 65)
    print("           EIGENVALUE & EIGENVECTOR ANALYSIS REPORT")
    print("=" * 65)

    for k, v in results.items():
        print(f"\n[{k}]")
        if isinstance(v, np.ndarray):
            print(np.round(v, 4))
        elif isinstance(v, dict):
            for sub_k, sub_v in v.items():
                if isinstance(sub_v, (float, np.float64, complex)):
                    print(f"  {sub_k:<35}: {sub_v:.4f}")
                else:
                    print(f"  {sub_k:<35}: {sub_v}")
        elif isinstance(v, (float, np.float64, complex)):
            print(f"  {v:.6f}")
        else:
            print(f"  {v}")

    print("=" * 65)