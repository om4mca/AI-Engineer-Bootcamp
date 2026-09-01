import numpy as np


class LinearIndependenceChecker:
    """Demonstrates and verifies linear independence of a set of vectors."""

    def __init__(self, vectors, tol=1e-8):
        # Stack vectors as columns of matrix V: shape (dim, num_vectors)
        self.V = np.column_stack(vectors).astype(float)
        self.dim, self.k = self.V.shape
        self.tol = tol

    # --- 1. Rank Criterion ---
    def check_via_rank(self):
        """Vectors are independent iff Rank(V) == k (number of vectors)."""
        rank = np.linalg.matrix_rank(self.V, tol=self.tol)
        is_independent = rank == self.k
        return rank, is_independent

    # --- 2. Determinant Criterion (Square Case Only) ---
    def check_via_determinant(self):
        """For k vectors in R^k, independent iff det(V) != 0."""
        if self.dim != self.k:
            return None, "N/A (Non-square matrix)"

        det_val = np.linalg.det(self.V)
        is_independent = not np.isclose(det_val, 0.0, atol=self.tol)
        return det_val, is_independent

    # --- 3. Gram Matrix Criterion G = V^T * V ---
    def check_via_gram_matrix(self):
        """Vectors are independent iff Gram Matrix G = V^T * V is positive definite (det(G) > 0)."""
        G = self.V.T @ self.V
        det_G = np.linalg.det(G)
        min_eig = np.min(np.linalg.eigvalsh(G))
        is_independent = min_eig > self.tol
        return det_G, min_eig, is_independent

    # --- 4. Linear Dependency Relation Finder ---
    def find_dependency_coefficients(self):
        """If dependent, finds non-trivial coefficients c such that V * c = 0."""
        rank, is_ind = self.check_via_rank()
        if is_ind:
            return None, "Vectors are linearly independent (No non-trivial relation)."

        # SVD: Right singular vectors V_svd corresponding to zero singular value give nullspace
        _, S, Vt = np.linalg.svd(self.V)
        # Smallest singular value corresponds to last row of Vt
        c = Vt[-1, :]
        residual = np.linalg.norm(self.V @ c)

        return c, f"Residual ||V * c|| = {residual:.2e}"

    # --- 5. Full Report ---
    def analyze(self):
        rank, ind_rank = self.check_via_rank()
        det_val, ind_det = self.check_via_determinant()
        det_G, min_eig, ind_gram = self.check_via_gram_matrix()
        c_dep, dep_msg = self.find_dependency_coefficients()

        return {
            "Dimension (R^n)": self.dim,
            "Number of Vectors (k)": self.k,
            "Matrix Rank": f"{rank} / {self.k}",
            "Is Independent (Rank Test)": ind_rank,
            "Determinant det(V)": det_val,
            "Is Independent (Det Test)": ind_det,
            "Gram Det det(V^T V)": det_G,
            "Min Eigenvalue of Gram Matrix": min_eig,
            "Dependency Coefficients c": c_dep,
            "Dependency Verification": dep_msg,
        }


# --- Execution Example ---
if __name__ == "__main__":
    print("=" * 65)
    print("        LINEAR INDEPENDENCE DEMONSTRATION & VERIFICATION")
    print("=" * 65)

    # Example 1: Linearly Independent Set in R^3
    v1 = [1, 0, 2]
    v2 = [0, 1, 3]
    v3 = [4, 1, 0]

    checker_ind = LinearIndependenceChecker([v1, v2, v3])
    print("\n--- Test 1: Independent Set ---")
    for k, v in checker_ind.analyze().items():
        print(f"  {k:<32}: {v}")

    # Example 2: Linearly Dependent Set in R^3 (v3 = 2*v1 + 3*v2)
    u1 = np.array([1.0, 2.0, 0.0])
    u2 = np.array([0.0, 1.0, 4.0])
    u3 = 2 * u1 + 3 * u2  # Dependent: [2, 7, 12]

    checker_dep = LinearIndependenceChecker([u1, u2, u3])
    print("\n--- Test 2: Dependent Set ---")
    for k, v in checker_dep.analyze().items():
        print(f"  {k:<32}: {v}")

    print("=" * 65)