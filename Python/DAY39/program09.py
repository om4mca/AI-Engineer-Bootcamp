import pandas as pd

df = pd.DataFrame({
    'Feature_A': [10, 20, 30, 40, 50],
    'Feature_B': [100, 200, 150, 300, 250]
})

# Standardize a single column
# Formula: (X - mean) / std
df['Feature_A_standardized'] = (df['Feature_A'] - df['Feature_A'].mean()) / df['Feature_A'].std(ddof=0)

# Standardize multiple columns at once
cols_to_scale = ['Feature_A', 'Feature_B']
df_standardized = (df[cols_to_scale] - df[cols_to_scale].mean()) / df[cols_to_scale].std(ddof=0)

print(df)