import pandas as pd

# Skip the top 2 rows (rows 0 and 1)
df = pd.read_csv("E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv", skiprows=2)

print(df.head())