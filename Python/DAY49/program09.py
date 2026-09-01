import numpy as np


class MatrixRankAnalyzer:
    """A comprehensive Matrix Rank Analyzer implemented using pure NumPy."""

    def __init__(self, matrix, tol=None):
        self.A = np.array(matrix, dtype=float)
        if self.A.ndim != 2:
            raise ValueError("Input must be a 2D matrix.")
        self.m, self.n = self.A.shape

        # Default numerical tolerance based on machine epsilon
        if tol is None:
            self.tol = max(self.m, self.n) * np.finfo(self.A.dtype).eps * np.linalg.norm(self.A, ord=2)
        else:
            self.tol = float(tol)

    # --- 1. Rank Calculation Engines ---
    def rank_svd(self):
        """Rank via Singular Value Decomposition: Count singular values > tolerance."""
        singular_values = np.linalg.svd(self.A, compute_uv=False)
        return np.sum(singular_values > self.tol), singular_values

    def rank_qr(self):
        """Rank via QR Decomposition with Pivoting: Count non-zero diagonal entries of R."""
        Q, R, P = np.linalg.qr(self.A, mode="full", pivoting=True)
        diag_R = np.abs(np.diag(R))
        return np.sum(diag_R > self.tol)

    def rank_rref(self):
        """Rank via Reduced Row Echelon Form (Gaussian Elimination with Partial Pivoting)."""
        M = self.A.copy()
        pivot_count = 0
        r, c = 0, 0

        while r < self.m and c < self.n:
            # Find pivot in current column
            max_row = np.argmax(np.abs(M[r:, c])) + r
            if np.abs(M[max_row, c]) <= self.tol:
                M[r:, c] = 0.0
                c += 1
                continue

            # Swap pivot row
            M[[r, max_row]] = M[[max_row, r]]

            # Eliminate lower entries
            for i in range(r + 1, self.m):
                factor = M[i, c] / M[r, c]
                M[i, c:] -= factor * M[r, c:]

            pivot_count += 1
            r += 1
            c += 1

        return pivot_count, M

    # --- 2. Fundamental Subspace Dimensions ---
    def fundamental_subspaces(self):
        """Calculates dimensions of the 4 Fundamental Subspaces of Linear Algebra."""
        r, _ = self.rank_svd()
        return {
            "Column Space Col(A) / Image": r,
            "Null Space Null(A) / Kernel": self.n - r,
            "Row Space Row(A)": r,
            "Left Null Space Null(A^T)": self.m - r,
        }

    # --- 3. Rank-Nullity Verification ---
    def verify_rank_nullity_theorem(self):
        """Verifies Rank(A) + Nullity(A) = n (Number of Columns)."""
        r, _ = self.rank_svd()
        nullity = self.n - r
        is_valid = (r + nullity) == self.n
        return {
            "Rank r": r,
            "Nullity (n - r)": nullity,
            "Columns n": self.n,
            "Theorem Holds (r + nullity == n)": is_valid,
        }

    # --- 4. Rank Classification & Data Diagnostics ---
    def classify_rank(self):
        """Categorizes rank completeness and numerical health."""
        r, s_vals = self.rank_svd()
        max_possible_rank = min(self.m, self.n)
        is_full_rank = r == max_possible_rank

        # Effective rank check (condition ratio of singular values)
        cond_ratio = s_vals[0] / s_vals[-1] if s_vals[-1] > 0 else np.inf

        return {
            "Max Possible Rank min(m, n)": max_possible_rank,
            "Actual Rank": r,
            "Is Full Rank": is_full_rank,
            "Is Rank Deficient": not is_full_rank,
            "Singular Value Ratio (s_max / s_min)": cond_ratio,
            "Multicollinearity / Low-Rank Alert": cond_ratio > 1e8,
        }

    # --- 5. Full Analysis Report ---
    def analyze(self):
        rank_svd_val, s_vals = self.rank_svd()
        rank_rref_val, rref_mat = self.rank_rref()

        return {
            "Matrix Dimensions": f"{self.m} x {self.n}",
            "Numerical Tolerance": self.tol,
            "Rank (SVD Method)": rank_svd_val,
            "Rank (QR Pivoting Method)": self.rank_qr(),
            "Rank (RREF Method)": rank_rref_val,
            "Singular Values": s_vals,
            "Classification": self.classify_rank(),
            "Subspace Dimensions": self.fundamental_subspaces(),
            "Rank-Nullity Verification": self.verify_rank_nullity_theorem(),
        }


# --- Execution Example ---
if __name__ == "__main__":
    # Test matrix: 4x3 Rank-Deficient Matrix (Col 3 = Col 1 + 2*Col 2)
    col1 = np.array([1, 2, 3, 4])
    col2 = np.array([5, 6, 7, 8])
    col3 = col1 + 2 * col2  # Linearly dependent column

    matrix_data = np.column_stack([col1, col2, col3])

    analyzer = MatrixRankAnalyzer(matrix_data)
    results = analyzer.analyze()

    print("=" * 65)
    print("              MATRIX RANK ANALYSIS REPORT")
    print("=" * 65)

    for k, v in results.items():
        print(f"\n[{k}]")
        if isinstance(v, np.ndarray):
            print(np.round(v, 4))
        elif isinstance(v, dict):
            for sub_k, sub_v in v.items():
                if isinstance(sub_v, float):
                    print(f"  {sub_k:<38}: {sub_v:.4e}")
                else:
                    print(f"  {sub_k:<38}: {sub_v}")
        elif isinstance(v, float):
            print(f"  {v:.4e}")
        else:
            print(f"  {v}")

    print("=" * 65)