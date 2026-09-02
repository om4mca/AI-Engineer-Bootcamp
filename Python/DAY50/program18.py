import numpy as np


class LinearEquationSolver:
    """Production-Grade Linear System Solver (Ax = b) using Linear Algebra."""

    def __init__(self, A, b):
        self.A = np.asarray(A, dtype=float)
        self.b = np.asarray(b, dtype=float)

        if self.A.ndim != 2:
            raise ValueError("Coefficient matrix A must be 2-dimensional.")
        if self.b.ndim == 1:
            self.b = self.b.reshape(-1, 1)

        self.rows, self.cols = self.A.shape
        if self.b.shape[0] != self.rows:
            raise ValueError("Row count of A must match length of vector b.")

    def check_system_consistency(self) -> dict:
        """Rouché-Capelli Theorem ke aadhar par system ke solutions audit karta hai."""
        augmented_matrix = np.hstack((self.A, self.b))
        rank_A = np.linalg.matrix_rank(self.A)
        rank_aug = np.linalg.matrix_rank(augmented_matrix)

        if rank_A < rank_aug:
            status = "Inconsistent (No Solution)"
        elif rank_A == rank_aug == self.cols:
            status = "Consistent & Unique Solution"
        else: # rank_A == rank_aug < self.cols
            status = "Consistent & Infinite Solutions (Underdetermined)"

        return {
            "Rank(A)": rank_A,
            "Rank([A|b])": rank_aug,
            "Variables (n)": self.cols,
            "System Status": status,
        }

    def solve_direct(self) -> np.ndarray:
        """Solves Ax = b directly using LAPACK solver (LU Decomposition based)."""
        consistency = self.check_system_consistency()
        if consistency["System Status"] == "Inconsistent (No Solution)":
            raise ValueError("System is inconsistent and has no exact solution.")

        if self.rows == self.cols and consistency["Rank(A)"] == self.cols:
            return np.linalg.solve(self.A, self.b).flatten()
        else:
            # Uses Least Squares for non-square or singular matrices
            x_lstsq, _, _, _ = np.linalg.lstsq(self.A, self.b, rcond=None)
            return x_lstsq.flatten()

    def solve_inverse(self) -> np.ndarray:
        """Solves Ax = b using Matrix Inverse (x = A^(-1) * b). Requires square invertible matrix."""
        if self.rows != self.cols:
            raise ValueError("Matrix Inverse method requires a square matrix.")
        if abs(np.linalg.det(self.A)) < 1e-10:
            raise ValueError("Matrix is singular (Determinant ≈ 0). Cannot compute inverse.")

        inv_A = np.linalg.inv(self.A)
        x = inv_A @ self.b
        return x.flatten()

    def verify_solution(self, x: np.ndarray) -> dict:
        """Calculates residual norm ||Ax - b|| to verify accuracy."""
        x_vec = np.asarray(x, dtype=float).reshape(-1, 1)
        residual = (self.A @ x_vec) - self.b
        residual_norm = float(np.linalg.norm(residual))
        return {
            "Residual Vector (Ax - b)": residual.flatten(),
            "Residual L2 Norm": round(residual_norm, 6),
            "Solution Valid?": np.isclose(residual_norm, 0.0, atol=1e-5),
        }


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("      LINEAR EQUATION SOLVER SYSTEM         ")
    print("============================================\n")

    # Example System:
    # 2x + 1y - 1z = 8
    # -3x - 1y + 2z = -11
    # -2x + 1y + 2z = -3

    A_data = [
        [2.0, 1.0, -1.0],
        [-3.0, -1.0, 2.0],
        [-2.0, 1.0, 2.0],
    ]
    b_data = [8.0, -11.0, -3.0]

    solver = LinearEquationSolver(A_data, b_data)

    # 1. System Consistency Inspection
    print("--- [1] System Consistency Check ---")
    consistency = solver.check_system_consistency()
    for k, v in consistency.items():
        print(f"  {k:<20}: {v}")

    # 2. Direct Solve (LU-based)
    print("\n--- [2] Direct LAPACK Solution ---")
    x_sol = solver.solve_direct()
    print(f"  Solution Vector (x) : {np.round(x_sol, 4)}")

    # 3. Inverse Method Solve
    print("\n--- [3] Matrix Inverse Solution (x = A^-1 * b) ---")
    x_inv = solver.solve_inverse()
    print(f"  Solution Vector (x) : {np.round(x_inv, 4)}")

    # 4. Accuracy Verification
    print("\n--- [4] Solution Accuracy Verification ---")
    verification = solver.verify_solution(x_sol)
    for k, v in verification.items():
        print(f"  {k:<24}: {v}")