import numpy as np
import pandas as pd

def detect_outliers_iqr(data):
    # Calculate Q1 (25th percentile) and Q3 (75th percentile)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    
    # Define bounds
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    
    # Identify outliers
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    clean_data = [x for x in data if lower_bound <= x <= upper_bound]
    
    print(f"Lower Bound : {lower_bound:.2f}")
    print(f"Upper Bound : {upper_bound:.2f}")
    print(f"Outliers    : {outliers}")
    
    return clean_data

# Example dataset with extreme values (100 and -50)
data = [12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 100, -50]
clean = detect_outliers_iqr(data)