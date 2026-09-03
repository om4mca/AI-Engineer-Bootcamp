import pandas as pd

# 1. Create Sample Dataset
data = {
    'Age': [25, 45, 35, 50],                    # Numerical (Integer)
    'BloodPressure': [120.5, 140.2, 115.0, 135.8],# Numerical (Float)
    'Education': ['Bachelor', 'PhD', 'Master', 'Master'], # Categorical (String/Text)
    'IsSmoker': [True, False, False, True],     # Categorical (Boolean)
    'RiskLevel': ['Low', 'High', 'Low', 'Medium'] # Categorical Target
}

df = pd.DataFrame(data)

# Separate Features (X) from Target
X = df.drop(columns=['RiskLevel'])

# -------------------------------------------------------------------
# METHOD 1: Using select_dtypes() (Pandas Recommended)
# -------------------------------------------------------------------
num_cols = X.select_dtypes(include=['int64', 'float64', 'number']).columns.tolist()
cat_cols = X.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

print("--- METHOD 1: Pandas select_dtypes() ---")
print("Numerical Features   :", num_cols)
print("Categorical Features :", cat_cols)


# -------------------------------------------------------------------
# METHOD 2: Programmatic Data Inspection Loop
# -------------------------------------------------------------------
print("\n--- METHOD 2: Data Type Inspection ---")
for col in X.columns:
    col_type = X[col].dtype
    if col_type in ['int64', 'float64']:
        print(f"Column '{col}': Numerical ({col_type})")
    else:
        print(f"Column '{col}': Categorical ({col_type})")


# -------------------------------------------------------------------
# METHOD 3: Pure Python (Dictionaries / Lists)
# -------------------------------------------------------------------
sample_row = {
    'Age': 25, 
    'BloodPressure': 120.5, 
    'Education': 'Bachelor', 
    'IsSmoker': True
}

py_num = [k for k, v in sample_row.items() if isinstance(v, (int, float)) and not isinstance(v, bool)]
py_cat = [k for k, v in sample_row.items() if isinstance(v, (str, bool))]

print("\n--- METHOD 3: Pure Python ---")
print("Numerical   :", py_num)
print("Categorical :", py_cat)