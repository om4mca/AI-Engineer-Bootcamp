import numpy as np
import statistics

# Normal Dataset (No Outliers)
data_clean = [50, 52, 55, 58, 60, 62, 65, 68, 70]

# Skewed Dataset (Added 1 Extreme Outlier: CEO Salary / Luxury Mansion)
data_outlier = [50, 52, 55, 58, 60, 62, 65, 68, 1000]

print("--- 1. CLEAN DATASET ---")
print(f"Data   : {data_clean}")
print(f"Mean   : {statistics.mean(data_clean):.2f}")
print(f"Median : {statistics.median(data_clean):.2f}")

print("\n--- 2. DATASET WITH OUTLIER (1000) ---")
print(f"Data   : {data_outlier}")
print(f"Mean   : {statistics.mean(data_outlier):.2f}  <-- Shifted dramatically by +103.5!")
print(f"Median : {statistics.median(data_outlier):.2f}    <-- Remained completely unchanged!")