import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
    'Age': [25.0, np.nan, 30.0, 35.0, np.nan],
    'Salary': [50000, 60000, np.nan, 80000, 90000]
})

print("--- Original DataFrame ---")
print(df)

# Calculate mean age ( (25 + 30 + 35) / 3 = 30.0 )
mean_age = df['Age'].mean()

# Fill missing values in 'Age' column
df['Age'] = df['Age'].fillna(mean_age)

print(df)