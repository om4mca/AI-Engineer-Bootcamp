import numpy as np

salaries = np.array([
    25000, 30000, 35000, 40000, 45000,
    50000, 60000, 75000, 90000, 120000
])

print("====== EMPLOYEE SALARY ANALYSIS ======\n")
print(f"Total Salary: ₹{np.sum(salaries):,}")
print(f"Average Salary: ₹{np.mean(salaries):,.2f}")
print(f"Median Salary: ₹{np.median(salaries):,.2f}")
print(f"Minimum Salary: ₹{np.min(salaries):,}")
print(f"Maximum Salary: ₹{np.max(salaries):,}\n")

print(f"Standard Deviation: {np.std(salaries):,.2f}")
print(f"Variance: {np.var(salaries):,.2f}\n")

print(f"Lowest Salary Index: {np.argmin(salaries)}")
print(f"Highest Salary Index: {np.argmax(salaries)}\n")

print(f"25th Percentile: ₹{np.percentile(salaries, 25):,.2f}")
print(f"75th Percentile: ₹{np.percentile(salaries, 75):,.2f}\n")

print("Cumulative Salary:")
print(np.cumsum(salaries).tolist())