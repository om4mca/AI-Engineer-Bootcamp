import numpy as np
import pandas as pd

data = [10, 15, 20, 25, 30, 30, 45]

# --- NumPy ---
# Option A: np.ptp() (Peak-to-Peak)
numpy_range_ptp = np.ptp(data)

# Option B: np.max() - np.min()
numpy_range_diff = np.max(data) - np.min(data)

print(f"NumPy Peak-to-Peak Range : {numpy_range_ptp}")

# --- Pandas ---
df = pd.DataFrame({'Values': data})
pandas_range = df['Values'].max() - df['Values'].min()

print(f"Pandas Series Range      : {pandas_range}")