import pandas as pd

# Data values and custom index labels
data = [85, 92, 78, 90]
custom_index = ['Math', 'Science', 'English', 'History']

# Create Series with custom labels
scores = pd.Series(data, index=custom_index)

print(scores)