import pandas as pd
import numpy as np
from scipy import stats

# Sample data
data = {
    'Feature_A': [10, 12, 23, 23, 16, 23, 21, 16],
    'Feature_B': [100, 110, 105, 120, 115, 130, 125, 118],
    'Feature_C': [1.2, 2.4, 1.8, 3.1, 2.7, 1.9, 2.2, 3.0]
}
df = pd.DataFrame(data)

# Method A: Pure Pandas (Vectorized across all columns)
# Formula: Z = (X - μ) / σ
# ddof=0 calculates population standard deviation; ddof=1 calculates sample standard deviation
df_zscore_pandas = (df - df.mean()) / df.std(ddof=0)

# Method B: Using SciPy's zscore function
df_zscore_scipy = df.apply(stats.zscore)

print("--- Pandas Z-Scores ---")
print(df_zscore_pandas)