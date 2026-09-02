import numpy as np


class VectorOperationsSystem:
    """High-performance n-Dimensional Vector Operations and Spatial Transformation Engine."""

    def __init__(self, vector: np.ndarray):
        """Vector initialization with shape validation."""
        self.v = np.asarray(vector, dtype=float).flatten()

    @property
    def magnitude(self) -> float:
        """Vector ki L2 norm (magnitude/length) calculate karta hai."""
        return np.linalg.norm(self.v)

    def normalize(self) -> np.ndarray:
        """Vector ko unit vector mein convert karta hai (Magnitude = 1.0)."""
        mag = self.magnitude
        if mag == 0:
            raise ValueError("Zero vector ko normalize nahi kiya ja sakta.")
        return self.v / mag

    def dot_product(self, other_vector: np.ndarray) -> float:
        """Algebraic dot product compute karta hai."""
        other = np.asarray(other_vector, dtype=float).flatten()
        return np.dot(self.v, other)

    def cross_product(self, other_vector: np.ndarray) -> np.ndarray:
        """3D Vector Cross product (Vector Product) calculate karta hai."""
        other = np.asarray(other_vector, dtype=float).flatten()
        if self.v.shape[0] != 3 or other.shape[0] != 3:
            raise ValueError(
                "Cross product ke liye dono vectors 3-Dimensional hone chahiye."
            )
        return np.cross(self.v, other)

    def angle_between(
        self, other_vector: np.ndarray, in_degrees: bool = True
    ) -> float:
        """Dono vectors ke beech ka angle compute karta hai using Cosine Rule."""
        other_sys = VectorOperationsSystem(other_vector)
        dot_val = self.dot_product(other_sys.v)
        cos_theta = dot_val / (self.magnitude * other_sys.magnitude)

        # Clipping values to prevent floating point instability outside [-1, 1]
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        angle_rad = np.arccos(cos_theta)

        return np.degrees(angle_rad) if in_degrees else angle_rad

    def projection_onto(self, target_vector: np.ndarray) -> np.ndarray:
        """Current vector ka projection target vector par calculate karta hai (Vector Projection)."""
        target = VectorOperationsSystem(target_vector)
        target_norm = target.normalize()
        scalar_proj = self.dot_product(target_norm)
        return scalar_proj * target_norm

    def euclidean_distance(self, other_vector: np.ndarray) -> float:
        """Dono vectors ke beech ki Euclidean Spatial Distance return karta hai."""
        other = np.asarray(other_vector, dtype=float).flatten()
        return np.linalg.norm(self.v - other)

    def cosine_similarity(self, other_vector: np.ndarray) -> float:
        """Cosine Similarity measure compute karta hai (Range: -1.0 to 1.0)."""
        other_sys = VectorOperationsSystem(other_vector)
        return self.dot_product(other_sys.v) / (
            self.magnitude * other_sys.magnitude
        )


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("       VECTOR OPERATIONS SYSTEM (NUMPY)     ")
    print("============================================\n")

    # Defining two 3D Vectors
    vector_a = [3.0, 4.0, 0.0]
    vector_b = [0.0, 4.0, 3.0]

    vec_a = VectorOperationsSystem(vector_a)
    vec_b = VectorOperationsSystem(vector_b)

    # 1. Magnitudes and Normalization
    print("--- [1] Magnitudes & Normalization ---")
    print(f"Vector A Magnitude: {vec_a.magnitude}")
    print(f"Vector A Unit Vector: {vec_a.normalize()}")

    # 2. Dot and Cross Products
    print("\n--- [2] Dot & Cross Products ---")
    dot_res = vec_a.dot_product(vector_b)
    cross_res = vec_a.cross_product(vector_b)
    print(f"A • B (Dot Product)  : {dot_res}")
    print(f"A × B (Cross Product): {cross_res}")

    # 3. Angle and Similarity Metrics
    print("\n--- [3] Spatial Angles & Similarity ---")
    angle_deg = vec_a.angle_between(vector_b, in_degrees=True)
    cos_sim = vec_a.cosine_similarity(vector_b)
    euc_dist = vec_a.euclidean_distance(vector_b)

    print(f"Angle between A and B: {angle_deg:.2f}°")
    print(f"Cosine Similarity    : {cos_sim:.4f}")
    print(f"Euclidean Distance   : {euc_dist:.4f}")

    # 4. Vector Projection
    print("\n--- [4] Vector Projection ---")
    proj_a_on_b = vec_a.projection_onto(vector_b)
    print(f"Projection of A onto B: {proj_a_on_b}")