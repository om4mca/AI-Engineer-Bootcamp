import pandas as pd

# Create a sample DataFrame
data = {
    'EmployeeID': ['E101', 'E102', 'E103', 'E104'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, None, 28],                # Contains a missing value (None)
    'Salary': [70000.50, 80000.00, 95000.75, 62000.00]
}

df = pd.DataFrame(data)

# Call the info() method
df.info()