import pandas as pd
import numpy as np

# Sample Dataset
data = {
    'Age': [22, 25, 25, 30, 32, 35, 40, 42, 50, 85], # 85 is an outlier
    'Salary': [45000, 48000, 50000, 52000, 60000, 62000, 75000, 82000, 95000, 150000]
}
df = pd.DataFrame(data)

def get_complete_summary_df(dataframe):
    # 1. Base Pandas Description (Count, Mean, Std, Min, 25%, 50%, 75%, Max)
    summary = dataframe.describe().T
    
    # 2. Append additional statistical metrics
    summary['variance'] = dataframe.var()
    summary['IQR'] = summary['75%'] - summary['25%']
    summary['skewness'] = dataframe.skew()
    summary['kurtosis'] = dataframe.kurtosis()
    summary['median'] = dataframe.median()
    summary['mode'] = dataframe.mode().iloc[0] # First modal value
    
    # Rearrange columns logically
    cols = ['count', 'mean', 'median', 'mode', 'std', 'variance', 
            'min', '25%', '75%', 'max', 'IQR', 'skewness', 'kurtosis']
    return summary[cols]

print("--- PANDAS EXTENDED STATISTICAL SUMMARY ---")
print(get_complete_summary_df(df).round(2).to_string())