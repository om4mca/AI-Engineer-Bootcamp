import numpy as np

# 1. Generate 5 evenly spaced numbers from 0 to 1 (inclusive)
arr1 = np.linspace(0, 1, num=5)

# 2. Generate 10 evenly spaced numbers between 10 and 50
arr2 = np.linspace(10, 50, num=10)

# 3. Exclude the endpoint using endpoint=False
arr3 = np.linspace(0, 10, num=5, endpoint=False)

# 4. Return step size along with array using retstep=True
arr4, step = np.linspace(0, 100, num=5, retstep=True)

print("1. 5 values from 0 to 1  :", arr1)
print("2. 10 values from 10 to 50:", arr2)
print("3. Without endpoint      :", arr3)
print(f"4. With step size returned: {arr4} (Step Size = {step})")