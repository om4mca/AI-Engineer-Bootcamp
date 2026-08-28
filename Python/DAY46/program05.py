import numpy as np

def check_linear_independence(vectors: list) -> bool:
    """
    Checks if a list of vectors is linearly independent.
    
    Parameters:
        vectors: List of 1D array-like vectors.
    """
    # Stack vectors as columns to form matrix A
    A = np.column_stack(vectors)
    num_vectors = A.shape[1]
    
    # Calculate matrix rank
    rank = np.linalg.matrix_rank(A)
    
    is_independent = (rank == num_vectors)
    return is_independent, rank, num_vectors

# Test Independent Vectors
v1 = np.array([2, 1])
v2 = np.array([1, 3])
indep, rank, count = check_linear_independence([v1, v2])
print(f"Set 1: Rank={rank}/{count} -> {'INDEPENDENT ✅' if indep else 'DEPENDENT ❌'}")

# Test Dependent Vectors
u1 = np.array([1, 2])
u2 = np.array([-3, -6])
indep, rank, count = check_linear_independence([u1, u2])
print(f"Set 2: Rank={rank}/{count} -> {'INDEPENDENT ✅' if indep else 'DEPENDENT ❌'}")