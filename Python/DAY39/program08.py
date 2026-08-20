import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Compute mean and standard deviation
mean = np.mean(arr)
std = np.std(arr)

# Standardize
standardized_arr = (arr - mean) / std

print("Standardized 1D Array:")
print(standardized_arr)
print("Mean:", np.mean(standardized_arr))  # Output ~ 0.0
print("Std Dev:", np.std(standardized_arr)) # Output ~ 1.0