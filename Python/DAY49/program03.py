import numpy as np


class VectorNormAnalyzer:
    """A comprehensive Vector Norm Analyzer implemented purely using NumPy."""

    def __init__(self, vector):
        self.v = np.array(vector, dtype=float).flatten()
        if self.v.size == 0:
            raise ValueError("Input vector cannot be empty.")
        self.dim = self.v.size

    # --- 1. Standard Lp Norms ---
    def l1_norm(self):
        """L1 Norm (Manhattan / Taxicab): Sum of absolute values."""
        return np.sum(np.abs(self.v))

    def l2_norm(self):
        """L2 Norm (Euclidean): Square root of sum of squared components."""
        return np.sqrt(np.sum(self.v**2))

    def lp_norm(self, p):
        """General Lp Norm for p >= 1."""
        if p < 1:
            raise ValueError("Lp norm mathematically requires p >= 1.")
        return np.sum(np.abs(self.v) ** p) ** (1.0 / p)

    def l_infinity_norm(self):
        """L-infinity Norm (Chebyshev / Max): Maximum absolute element."""
        return np.max(np.abs(self.v))

    def l0_pseudo_norm(self):
        """L0 Pseudo-Norm: Count of non-zero elements (Sparsity count)."""
        return np.count_nonzero(self.v)

    def fractional_lp_norm(self, p):
        """Fractional Lp Norm (0 < p < 1): Non-convex sparsity-promoting metric."""
        if p <= 0:
            raise ValueError("p must be greater than 0.")
        return np.sum(np.abs(self.v) ** p) ** (1.0 / p)

    # --- 2. Custom & Domain-Specific Norms ---
    def weighted_lp_norm(self, weights, p=2):
        """Weighted Lp Norm: ||v||_{w,p} = (sum(w_i * |v_i|^p))^(1/p)"""
        w = np.array(weights, dtype=float).flatten()
        if w.shape != self.v.shape:
            raise ValueError("Weights shape must match vector shape.")
        if np.any(w < 0):
            raise ValueError("Weights must be non-negative.")
        return np.sum(w * (np.abs(self.v) ** p)) ** (1.0 / p)

    def mahalanobis_norm(self, cov_matrix):
        """Mahalanobis Norm: ||v||_M = sqrt(v^T * Inv(Sigma) * v)"""
        cov = np.array(cov_matrix, dtype=float)
        if cov.shape != (self.dim, self.dim):
            raise ValueError(
                f"Covariance matrix must be square of size ({self.dim}, {self.dim})."
            )

        inv_cov = np.linalg.inv(cov)
        return np.sqrt(self.v.T @ inv_cov @ self.v)

    # --- 3. Normalization Utilities ---
    def normalize(self, p=2):
        """Converts vector into a unit vector along the specified Lp norm."""
        if p == np.inf:
            norm_val = self.l_infinity_norm()
        else:
            norm_val = self.lp_norm(p)

        if norm_val == 0:
            return np.zeros_like(self.v)
        return self.v / norm_val

    # --- 4. Full Analysis Report ---
    def analyze(self, custom_p=3, weights=None, cov_matrix=None):
        report = {
            "Dimension (n)": self.dim,
            "L0 (Sparsity Count)": self.l0_pseudo_norm(),
            "L1 Norm (Manhattan)": self.l1_norm(),
            "L2 Norm (Euclidean)": self.l2_norm(),
            f"Lp Norm (p={custom_p})": self.lp_norm(custom_p),
            "L-Infinity Norm (Max)": self.l_infinity_norm(),
            "Unit Vector (L2 normalized)": self.normalize(p=2),
        }

        if weights is not None:
            report["Weighted L2 Norm"] = self.weighted_lp_norm(weights, p=2)

        if cov_matrix is not None:
            report["Mahalanobis Norm"] = self.mahalanobis_norm(cov_matrix)

        return report


# --- Execution Example ---
if __name__ == "__main__":
    x = np.array([3.0, -4.0, 0.0, 12.0])

    w = [1.0, 2.0, 1.0, 0.5]
    sigma = np.eye(4)  # 4x4 Identity matrix

    analyzer = VectorNormAnalyzer(x)
    results = analyzer.analyze(custom_p=3, weights=w, cov_matrix=sigma)

    print("=" * 55)
    print("        PURE NUMPY VECTOR NORM ANALYSIS REPORT")
    print("=" * 55)
    print(f"Input Vector x: {x}\n")

    for metric, val in results.items():
        if isinstance(val, np.ndarray):
            print(f"{metric:<25}: {np.round(val, 4)}")
        elif isinstance(val, float):
            print(f"{metric:<25}: {val:.4f}")
        else:
            print(f"{metric:<25}: {val}")
    print("=" * 55)