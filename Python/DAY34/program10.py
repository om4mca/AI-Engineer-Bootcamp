import pandas as pd
import numpy as np

# Sample Hospital Department Data
data = {
    'Department': ['Cardiology', 'Neurology', 'Cardiology', 'Orthopedics', 
                   'Cardiology', 'ICU', 'Neurology', np.nan, 'Cardiology']
}
df = pd.DataFrame(data)

# Basic Value Counts
print(df['Department'].value_counts())