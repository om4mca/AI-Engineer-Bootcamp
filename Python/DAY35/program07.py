import numpy as np
import pandas as pd

data = [10, 15, 20, 25, 30, 30, 45]

# --- NumPy ---
np_sample_std = np.std(data, ddof=1)  # Set ddof=1 for Sample
np_pop_std = np.std(data, ddof=0)     # Default: ddof=0 (Population)

print(f"NumPy Sample Std Dev (ddof=1) : {np_sample_std:.4f}")
print(f"NumPy Pop Std Dev (ddof=0)    : {np_pop_std:.4f}")

# --- Pandas ---
df = pd.DataFrame({'Values': data})
pd_sample_std = df['Values'].std()          # Default: ddof=1 (Sample)
pd_pop_std = df['Values'].std(ddof=0)       # Set ddof=0 for Population

print(f"Pandas Sample Std Dev (ddof=1): {pd_sample_std:.4f}")
print(f"Pandas Pop Std Dev (ddof=0)   : {pd_pop_std:.4f}")