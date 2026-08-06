import pandas as pd

df = pd.DataFrame({
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'Engineering']
})

# Frequency count per department
print(df['Department'].value_counts())