import numpy as np

def analyze_linear_dependence(vectors: list):
    """
    Analyzes a set of vectors for linear dependence and identifies redundancies.
    """
    A = np.column_stack(vectors)
    num_vectors = A.shape[1]
    rank = np.linalg.matrix_rank(A)
    
    is_dependent = (rank < num_vectors)
    
    print(f"Vector Count : {num_vectors}")
    print(f"Matrix Rank  : {rank}")
    print(f"Status       : {'DEPENDENT ❌' if is_dependent else 'INDEPENDENT ✅'}")
    
    if is_dependent:
        # Solve A c = 0 using SVD to find linear dependence coefficients
        _, _, Vh = np.linalg.svd(A)
        null_vector = Vh[-1, :]  # Right singular vector corresponding to smallest singular value
        print("Dependence Coefficients (c1*v1 + ... + ck*vk ≈ 0):")
        print(" ", np.round(null_vector, 4))

# Test set with coplanar vectors: v3 = 2*v1 + 3*v2
v1 = np.array([1, 0, 1])
v2 = np.array([0, 1, 1])
v3 = np.array([2, 3, 5])

analyze_linear_dependence([v1, v2, v3])