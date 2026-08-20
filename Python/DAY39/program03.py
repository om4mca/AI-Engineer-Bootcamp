import math
import statistics
import numpy as np

data = [10, 12, 23, 23, 16, 23, 21, 16]

# 1. Pure Python (Manual Sample Standard Deviation)
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
sample_std_manual = math.sqrt(variance)

# 2. Standard Library (statistics module)
sample_std_stat = statistics.stdev(data)
pop_std_stat = statistics.pstdev(data)

# 3. NumPy (ddof=1 for Sample, ddof=0 for Population)
sample_std_np = np.std(data, ddof=1)
pop_std_np = np.std(data, ddof=0)

print(f"Sample Std Dev (s)     : {sample_std_stat:.2f}")
print(f"Population Std Dev (σ) : {pop_std_stat:.2f}")