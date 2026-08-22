import numpy as np
from scipy.spatial.distance import cosine, euclidean, cityblock

u = np.array([2.0, 4.0, 5.0])
v = np.array([3.0, -1.0, 2.0])

# 1. Directional Alignment: Cosine Similarity & Distance
# Cosine Similarity = (u · v) / (||u|| * ||v||)
cos_sim = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
cos_dist = 1.0 - cos_sim  # Equivalent to scipy.spatial.distance.cosine(u, v)

# 2. Geometric Distance: L2 (Euclidean) Distance
euclidean_dist = np.linalg.norm(u - v)

# 3. Grid Distance: L1 (Manhattan) Distance
manhattan_dist = np.linalg.norm(u - v, ord=1)

# 4. Component Equality & Element-wise Difference
diff_vector = u - v
is_close = np.isclose(u, v, atol=1e-5)  # Element-wise close comparison

print("--- VECTOR COMPARISON RESULTS ---")
print(f"Cosine Similarity (-1 to 1):  {cos_sim:.4f}  (Measures angle/orientation)")
print(f"Cosine Distance (0 to 2):    {cos_dist:.4f}  (Measures directional difference)")
print(f"Euclidean Distance (L2):     {euclidean_dist:.4f}  (Measures straight-line distance)")
print(f"Manhattan Distance (L1):     {manhattan_dist:.4f}  (Measures grid path distance)")
print(f"Difference Vector (u - v):   {diff_vector}")