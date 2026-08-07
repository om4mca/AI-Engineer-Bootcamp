import pandas as pd

# Load your CSV file
df = pd.read_csv("E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv")

# Show statistics for numerical columns
print(df.describe())