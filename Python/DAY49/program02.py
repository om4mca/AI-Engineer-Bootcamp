import numpy as np


class VectorAnalyzer:
    """A comprehensive vector operations analyzer for 2D, 3D, or n-dimensional vectors."""

    def __init__(self, vec_a, vec_b, scalar_k=1.0):
        self.a = np.array(vec_a, dtype=float)
        self.b = np.array(vec_b, dtype=float)
        self.k = float(scalar_k)

        if self.a.shape != self.b.shape:
            raise ValueError(
                "Vectors A and B must have the same number of dimensions."
            )

        self.dim = self.a.shape[0]

    # --- Basic Vector Arithmetic ---
    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def scale_a(self):
        return self.k * self.a

    def scale_b(self):
        return self.k * self.b

    # --- Products & Projections ---
    def dot_product(self):
        return np.dot(self.a, self.b)

    def cross_product(self):
        if self.dim not in (2, 3):
            return "Cross product is only defined for 2D and 3D vectors."
        return np.cross(self.a, self.b)

    def projection_a_onto_b(self):
        """Vector projection of A onto B: proj_B(A) = ((A . B) / ||B||^2) * B"""
        b_norm_sq = np.dot(self.b, self.b)
        if b_norm_sq == 0:
            return "Undefined (cannot project onto zero vector B)."
        return (self.dot_product() / b_norm_sq) * self.b

    # --- Norms & Distance Metrics ---
    def norms(self, vec):
        return {
            "L1 (Manhattan)": np.linalg.norm(vec, ord=1),
            "L2 (Euclidean)": np.linalg.norm(vec, ord=2),
            "L_infinity (Max)": np.linalg.norm(vec, ord=np.inf),
        }

    # --- Spatial Angles & Cosine Similarity ---
    def cosine_similarity(self):
        norm_a = np.linalg.norm(self.a, ord=2)
        norm_b = np.linalg.norm(self.b, ord=2)
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return self.dot_product() / (norm_a * norm_b)

    def angle_degrees(self):
        cos_sim = np.clip(self.cosine_similarity(), -1.0, 1.0)
        return np.degrees(np.arccos(cos_sim))

    # --- Summary Report Generator ---
    def generate_report(self):
        print("=" * 55)
        print(f"       VECTOR OPERATIONS ANALYZER ({self.dim}D Space)")
        print("=" * 55)
        print(f"Vector A          : {self.a}")
        print(f"Vector B          : {self.b}")
        print(f"Scalar k          : {self.k}\n")

        print("--- 1. BASIC ARITHMETIC ---")
        print(f"A + B             : {self.add()}")
        print(f"A - B             : {self.subtract()}")
        print(f"k * A             : {self.scale_a()}")
        print(f"k * B             : {self.scale_b()}\n")

        print("--- 2. PRODUCTS & PROJECTIONS ---")
        print(f"Dot Product (A . B): {self.dot_product():.4f}")
        print(f"Cross Product (A x B): {self.cross_product()}")
        print(f"Proj of A onto B  : {self.projection_a_onto_b()}\n")

        print("--- 3. NORMS & ANGLES ---")
        print(f"Norms of A        : {self.norms(self.a)}")
        print(f"Norms of B        : {self.norms(self.b)}")
        print(f"Cosine Similarity : {self.cosine_similarity():.4f}")
        print(f"Angle Theta (deg) : {self.angle_degrees():.2f}°")
        print("=" * 55)


# --- Example Execution ---
if __name__ == "__main__":
    # Test with 3D vectors
    vector_a = [3, 4, 0]
    vector_b = [1, 2, 0]
    scalar = 2.5

    analyzer = VectorAnalyzer(vector_a, vector_b, scalar_k=scalar)
    analyzer.generate_report()