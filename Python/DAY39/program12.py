import pandas as pd
from scipy import stats

data = {
    'Item_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Value': [10, 12, 11, 13, 12, 11, 14, 12, 10, 45]  # 45 is far above +2σ
}
df = pd.DataFrame(data)

# Calculate Z-score using population std (ddof=0)
df['Z_Score'] = stats.zscore(df['Value'])

# Filter for values strictly greater than +2σ
above_2sigma = df[df['Z_Score'] > 2.0]

print("--- Values Above +2σ ---")
print(above_2sigma)