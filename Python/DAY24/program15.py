import numpy as np

# 1. Create a sample array
data = np.array([12, 45, 7, 23, 89, 34, 3, 50])
print("Original Array:", data)

# 2. Basic Condition: Find values greater than 30
condition = data > 30
print("\nBoolean Mask (data > 30):\n", condition)

# Filter the array using the mask
filtered_data = data[condition]
print("Filtered Array (data > 30):", filtered_data)


# 3. Compound Conditions: Combining multiple logical rules
# Note: Use bitwise operators & (AND), | (OR), ~ (NOT) with parentheses
even_and_gt_20 = data[(data % 2 == 0) & (data > 20)]
print("\nEven numbers AND greater than 20:", even_and_gt_20)


# 4. Modifying Values in Place using Boolean Indexing
# Set all numbers below 20 to -1
data[data < 20] = -1
print("\nArray after replacing values < 20 with -1:\n", data)