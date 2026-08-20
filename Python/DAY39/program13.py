import pandas as pd
from scipy import stats

data = {
    'Item_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Value': [50, 52, 51, 53, 52, 51, 54, 52, 50, 2]  # 2 is far below -2σ
}
df = pd.DataFrame(data)

# Calculate Z-score using population std (ddof=0)
df['Z_Score'] = stats.zscore(df['Value'])

# Filter for values strictly less than -2σ
below_minus_2sigma = df[df['Z_Score'] < -2.0]

print("--- Values Below -2σ ---")
print(below_minus_2sigma)