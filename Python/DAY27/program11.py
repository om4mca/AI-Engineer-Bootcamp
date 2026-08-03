import pandas as pd

# Create a sample DataFrame with 8 rows
data = {
    'PatientID': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008'],
    'Name': ['Amit', 'Rahul', 'Priya', 'Neha', 'Rohan', 'Sna', 'Karan', 'Meera'],
    'Age': [25, 40, 32, 65, 50, 29, 45, 38],
    'Temperature': [36.5, 38.2, 37.0, 39.1, 37.5, 36.8, 38.0, 37.2]
}

df = pd.DataFrame(data)

# 1. Inspect first 5 rows (default)
print("=== Head (Default 5 Rows) ===")
print(df.head())

# 2. Inspect first 3 rows
print("\n=== Head (First 3 Rows) ===")
print(df.head(3))

# 3. Inspect last 2 rows
print("\n=== Tail (Last 2 Rows) ===")
print(df.tail(2))