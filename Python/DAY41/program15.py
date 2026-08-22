import numpy as np

# 1. Define 1D Vectors
u = np.array([2.0, 4.0, 5.0])
v = np.array([3.0, -1.0, 2.0])

# 2. Key Vector Operations
vec_add   = u + v                                        # [ 5.  3.  7.]
vec_scale = 2.5 * u                                      # [ 5. 10. 12.5]
hadamard  = u * v                                        # [ 6. -4. 10.]
dot_prod  = u @ v                                        # 12.0
l2_norm   = np.linalg.norm(u)                            # 6.7082
u_unit    = u / l2_norm                                  # [0.2981, 0.5963, 0.7454]
cos_sim   = (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v)) # 0.4811
euc_dist  = np.linalg.norm(u - v)                        # 5.9161

# 3. Reshaping for Matrix Operations
col_vec   = u.reshape(-1, 1)  # Shape: (3, 1) - Column Vector
row_vec   = u.reshape(1, -1)  # Shape: (1, 3) - Row Vector

print(f"Dot Product (u @ v):      {dot_prod}")
print(f"Cosine Similarity:         {cos_sim:.4f}")
print(f"Euclidean Distance:        {euc_dist:.4f}")
print(f"Normalized Unit Vector u:  {np.round(u_unit, 4)}")