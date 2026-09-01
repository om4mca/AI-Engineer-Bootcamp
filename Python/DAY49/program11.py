import numpy as np


class LinearSystemSolver:
    """A robust Linear System Solver (Ax = b) implemented in pure NumPy."""

    def __init__(self, A, b, tol=1e-8):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float).flatten()
        if self.A.ndim != 2:
            raise ValueError("Coefficient matrix A must be 2D.")
        self.m, self.n = self.A.shape
        if self.b.shape[0] != self.m:
            raise ValueError(
                f"Dimension mismatch: A is {self.m}x{self.n}, but b has length {self.b.shape[0]}."
            )
        self.tol = tol

    # --- 1. System Classification ---
    def classify_system(self):
        """Classifies the system using Rouché-Capelli Theorem via Matrix Ranks."""
        rank_A = np.linalg.matrix_rank(self.A, tol=self.tol)
        Augmented = np.column_stack([self.A, self.b])
        rank_Aug = np.linalg.matrix_rank(Augmented, tol=self.tol)

        if rank_A < rank_Aug:
            system_type = "Inconsistent (No Exact Solution)"
        elif rank_A == rank_Aug == self.n:
            system_type = "Consistent & Determined (Unique Exact Solution)"
        else:  # rank_A == rank_Aug < n
            system_type = "Consistent & Underdetermined (Infinitely Many Solutions)"

        return {
            "m (Equations)": self.m,
            "n (Variables)": self.n,
            "Rank(A)": rank_A,
            "Rank([A|b])": rank_Aug,
            "Classification": system_type,
        }

    # --- 2. Solver Strategies ---
    def solve_exact_lu(self):
        """Direct solution via LU decomposition / Triangular solve for square non-singular systems."""
        try:
            x = np.linalg.solve(self.A, self.b)
            return x, "Exact LU / Gaussian Elimination"
        except np.linalg.LinAlgError:
            return None, "Matrix A is singular"

    def solve_least_squares_qr(self):
        """QR Decomposition solution minimizing ||Ax - b||_2 for overdetermined systems."""
        Q, R = np.linalg.qr(self.A, mode="reduced")
        # R * x = Q^T * b
        Qty = Q.T @ self.b
        try:
            x = np.linalg.solve(R, Qty)
            return x, "Least Squares via QR Decomposition"
        except np.linalg.LinAlgError:
            # Fall back if R is singular
            x, _, _, _ = np.linalg.lstsq(self.A, self.b, rcond=self.tol)
            return x, "Least Squares Pseudoinverse Fallback"

    def solve_minimum_norm_svd(self):
        """SVD Minimum-Norm solution x = A^+ * b for underdetermined/singular systems."""
        x = np.linalg.pinv(self.A, rcond=self.tol) @ self.b
        return x, "Minimum-Norm Solution via Moore-Penrose Pseudoinverse (SVD)"

    # --- 3. Unified Solve Execution ---
    def solve(self):
        """Automatically selects optimal solver based on system structure."""
        info = self.classify_system()
        rank_A = info["Rank(A)"]
        rank_Aug = info["Rank([A|b])"]

        if self.m == self.n and rank_A == self.n:
            x, method = self.solve_exact_lu()
        elif self.m > self.n and rank_A == self.n:
            x, method = self.solve_least_squares_qr()
        else:
            x, method = self.solve_minimum_norm_svd()

        # Compute Residual Vector r = Ax - b
        residual_vector = self.A @ x - self.b
        residual_norm = np.linalg.norm(residual_vector)

        return {
            "System Information": info,
            "Solution Method": method,
            "Solution Vector x": x,
            "Residual Vector (Ax - b)": residual_vector,
            "Residual Norm ||Ax - b||": residual_norm,
        }


# --- Execution Example ---
if __name__ == "__main__":
    print("=" * 65)
    print("                LINEAR SYSTEM SOLVER REPORT")
    print("=" * 65)

    # Example 1: Square Unique System (3x3)
    A1 = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b1 = [8, -11, -3]

    solver1 = LinearSystemSolver(A1, b1)
    res1 = solver1.solve()

    print("\n--- Case 1: Square System (Unique Solution) ---")
    for k, v in res1.items():
        print(f"[{k}]")
        if isinstance(v, np.ndarray):
            print(f"  {np.round(v, 4)}")
        elif isinstance(v, dict):
            for sub_k, sub_v in v.items():
                print(f"  {sub_k:<28}: {sub_v}")
        else:
            print(f"  {v}")

    # Example 2: Overdetermined System (3 Equations, 2 Variables)
    A2 = [[1, 1], [1, -1], [2, 1]]
    b2 = [2, 0, 3]

    solver2 = LinearSystemSolver(A2, b2)
    res2 = solver2.solve()

    print("\n--- Case 2: Overdetermined System (Least Squares) ---")
    print(f"  Classification: {res2['System Information']['Classification']}")
    print(f"  Method Used   : {res2['Solution Method']}")
    print(f"  Solution x    : {np.round(res2['Solution Vector x'], 4)}")
    print(f"  Residual Norm : {res2['Residual Norm ||Ax - b||']:.4f}")

    print("=" * 65)