import numpy as np

# 1. Base Vectors (Linearly Independent)
v1 = np.array([3.0, 1.0])
v2 = np.array([1.0, 4.0])

# 2. Generate Random Scalars
np.random.seed(42)
num_points = 1000
c1 = np.random.uniform(-5, 5, num_points)
c2 = np.random.uniform(-5, 5, num_points)

# 3. Compute Linear Combinations (c1*v1 + c2*v2)
span_vectors = np.column_stack([c1 * v1[0] + c2 * v2[0], 
                                c1 * v1[1] + c2 * v2[1]])

# 4. Verify Dimension via Matrix Rank
A = np.column_stack([v1, v2])
rank = np.linalg.matrix_rank(A)

print("=== SPAN ANALYSIS ===")
print(f"Base Vector 1 : {v1}")
print(f"Base Vector 2 : {v2}")
print(f"Matrix Rank   : {rank}")
print(f"Span Status   : {'Spans full 2D plane (ℝ²)' if rank == 2 else 'Spans only a 1D line'}")
print(f"Generated {len(span_vectors)} point combinations across the span.")