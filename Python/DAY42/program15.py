import pandas as pd
import numpy as np

# Sample raw DataFrame
df = pd.DataFrame({
    'SqFt': [1500, 2000, 1200],
    'Bedrooms': [3, 4, 2],
    'Location': ['Suburban', 'Urban', 'Suburban'],
    'Price': [300, 450, 250]
})

# 1. Separate target variable y
y = df['Price'].to_numpy()

# 2. Encode categorical variables and drop raw text columns
df_features = pd.get_dummies(df.drop(columns=['Price']), columns=['Location'])

# 3. Extract Feature Matrix X as a 2D NumPy Array
X = df_features.to_numpy(dtype=float)

print("Feature Matrix X:\n", X)
print("Shape of X:", X.shape) # Output: (3 samples, 3 features)