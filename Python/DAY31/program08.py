import pandas as pd

# Load only 'Name', 'Department', and 'Salary'
df = pd.read_csv("E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv", usecols=["Name", "Department", "Salary"])

print(df.head())