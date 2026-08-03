import pandas as pd

# Create a DataFrame with mixed data types
data = {
    'EmployeeID': ['E101', 'E102', 'E103'],   # Text/String (object)
    'Age': [25, 30, 35],                       # Integer (int64)
    'Salary': [70000.50, 80000.00, 95000.75],  # Float (float64)
    'IsActive': [True, False, True]            # Boolean (bool)
}

df = pd.DataFrame(data)

# Display column data types
print(df.dtypes)