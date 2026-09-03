import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Age': [25, 45, 35, 50],
    'BMI': [22.4, 28.1, 24.5, 30.2],
    'Income': [50000, 85000, 62000, 95000],
    'Purchased': [0, 1, 0, 1]  # Target column
}
df = pd.DataFrame(data)

# --- METHOD 1: Using .drop() (Recommended & Most Common) ---
# Drop the target column to form X, select target column for y
X = df.drop(columns=['Purchased'])
y = df['Purchased']

print("X (Features):\n", X)
print("\ny (Target):\n", y)


# --- METHOD 2: Direct Column Selection ---
feature_cols = ['Age', 'BMI', 'Income']
target_col = 'Purchased'

X = df[feature_cols]
y = df[target_col]


# --- METHOD 3: Converting directly to NumPy Arrays ---
# Use .values or .to_numpy() for scikit-learn models
X_array = df.drop(columns=['Purchased']).to_numpy()
y_array = df['Purchased'].to_numpy()

print("\nX Shape (NumPy):", X_array.shape)  # (4, 3)
print("y Shape (NumPy):", y_array.shape)    # (4,)