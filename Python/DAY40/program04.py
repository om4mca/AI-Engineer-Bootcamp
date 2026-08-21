import pandas as pd

data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Salary': [45000, 48000, 52000, 50000, 55000, 51000, 49000, 53000, 150000, 12000] # 150k and 12k are outliers
}
df = pd.DataFrame(data)

# 1. Calculate Q1 (25th percentile) and Q3 (75th percentile)
q1 = df['Salary'].quantile(0.25)
q3 = df['Salary'].quantile(0.75)

# 2. Calculate IQR
iqr = q3 - q1

# 3. Define upper and lower bounds (Tukey's Fences)
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# 4. Filter outliers
outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
clean_df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

print(f"Q1: {q1:,} | Q3: {q3:,} | IQR: {iqr:,}")
print(f"Lower Bound: {lower_bound:,} | Upper Bound: {upper_bound:,}\n")
print("--- IDENTIFIED OUTLIERS ---")
print(outliers[['Employee_ID', 'Salary']].to_string(index=False))