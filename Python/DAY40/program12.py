import numpy as np
from scipy import stats

# Sample dataset
data = np.array([10, 12, 15, 18, 20, 22, 25, 100]) # 100 is an extreme value

# Compute Z-scores across array
z_scores = stats.zscore(data)

print("--- SCIPY Z-SCORE CALCULATIONS ---")
for x, z in zip(data, z_scores):
    print(f"Value: {x:3d}  |  Z-score: {z:+.2f}")