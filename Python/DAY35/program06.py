import numpy as np
import pandas as pd

data = [10, 15, 20, 25, 30, 30, 45]

# --- NumPy ---
np_pop_var = np.var(data)          # Default: ddof=0 (Population)
np_sample_var = np.var(data, ddof=1) # Set ddof=1 for Sample

print(f"NumPy Sample Variance (ddof=1) : {np_sample_var:.2f}")
print(f"NumPy Pop Variance (ddof=0)    : {np_pop_var:.2f}")

# --- Pandas ---
df = pd.DataFrame({'Values': data})
pd_sample_var = df['Values'].var()        # Default: ddof=1 (Sample)
pd_pop_var = df['Values'].var(ddof=0)     # Set ddof=0 for Population

print(f"Pandas Sample Variance (ddof=1): {pd_sample_var:.2f}")
print(f"Pandas Pop Variance (ddof=0)   : {pd_pop_var:.2f}")