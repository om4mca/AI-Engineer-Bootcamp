from collections import Counter
import math
import random

# Set random seed for exact reproducibility
random.seed(42)

# ==============================================================================
# 1. DATASET GENERATION
# ==============================================================================
departments = ["Engineering", "Product", "Sales", "HR", "Marketing"]
performances = ["Exceeds", "Meets", "Needs Improvement"]

N = 250
# Generating synthetic salaries centered around $85,000 with sigma = $15,000
mean_base = 85000
std_base = 15000

dataset = []
for emp_id in range(1001, 1001 + N):
    exp = random.randint(1, 15)
    dept = random.choice(departments)
    perf = random.choices(performances, weights=[0.20, 0.70, 0.10])[0]

    # Generate salary following a normal distribution
    salary = round(random.gauss(mean_base, std_base), 2)

    dataset.append(
        {
            "EmployeeID": emp_id,
            "Department": dept,
            "Experience": exp,
            "Performance": perf,
            "Salary": salary,
        }
    )

salaries = [emp["Salary"] for emp in dataset]

# ==============================================================================
# 2. STATISTICAL ANALYSIS
# ==============================================================================
# Mean Salary
mean_salary = sum(salaries) / N

# Median Salary
sorted_salaries = sorted(salaries)
mid = N // 2
if N % 2 == 0:
    median_salary = (sorted_salaries[mid - 1] + sorted_salaries[mid]) / 2.0
else:
    median_salary = sorted_salaries[mid]

# Standard Deviation
variance = sum((x - mean_salary) ** 2 for x in salaries) / N
std_dev = math.sqrt(variance)

# Compute Z-Scores and tag employees
for emp in dataset:
    z_score = (emp["Salary"] - mean_salary) / std_dev
    emp["Z_Score"] = round(z_score, 2)

# Outliers and Empirical Rule Checks
above_2sig = [emp for emp in dataset if emp["Z_Score"] > 2.0]
below_neg2sig = [emp for emp in dataset if emp["Z_Score"] < -2.0]

within_1sig = [emp for emp in dataset if -1.0 <= emp["Z_Score"] <= 1.0]
within_2sig = [emp for emp in dataset if -2.0 <= emp["Z_Score"] <= 2.0]

pct_1sig = (len(within_1sig) / N) * 100
pct_2sig = (len(within_2sig) / N) * 100

# ==============================================================================
# 3. OUTPUT RESULTS
# ==============================================================================
print("==================================================================")
print("             EMPLOYEE SALARY NORMAL DISTRIBUTION ANALYSIS          ")
print("==================================================================")
print(f"Total Sample Size (N)       : {N} Employees")
print(f"Mean Salary                 : ${mean_salary:,.2f}")
print(f"Median Salary               : ${median_salary:,.2f}")
print(f"Standard Deviation (Sigma)  : ${std_dev:,.2f}")
print(
    f"Salary Distribution Shape   : Mean ≈ Median (Difference: ${abs(mean_salary - median_salary):,.2f}) -> Bell-Shaped / Symmetric\n"
)

print("------------------------------------------------------------------")
print("                     EMPIRICAL RULE & Z-SCORES                    ")
print("------------------------------------------------------------------")
print(
    f"Employees Above +2σ (> ${mean_salary + 2*std_dev:,.2f}) : {len(above_2sig)} ({len(above_2sig)/N:.1%})"
)
print(
    f"Employees Below -2σ (< ${mean_salary - 2*std_dev:,.2f}) : {len(below_neg2sig)} ({len(below_neg2sig)/N:.1%})"
)
print(
    f"Percentage within ±1σ (${mean_salary - std_dev:,.2f} to ${mean_salary + std_dev:,.2f}): {pct_1sig:.2f}% (Expected ~68%)"
)
print(
    f"Percentage within ±2σ (${mean_salary - 2*std_dev:,.2f} to ${mean_salary + 2*std_dev:,.2f}): {pct_2sig:.2f}% (Expected ~95%)\n"
)

# ==============================================================================
# 4. SALARY HISTOGRAM
# ==============================================================================
print("==================================================================")
print("                       SALARY HISTOGRAM                           ")
print("==================================================================")
num_bins = 8
min_s, max_s = min(salaries), max(salaries)
bin_width = (max_s - min_s) / num_bins

print(f"{'Salary Range ($)':<22} | {'Count':<6} | Histogram")
print("-" * 66)

for i in range(num_bins):
    low = min_s + i * bin_width
    high = low + bin_width
    if i == num_bins - 1:
        count = sum(1 for s in salaries if low <= s <= high)
    else:
        count = sum(1 for s in salaries if low <= s < high)

    bar = "█" * count
    print(f"[${low:8,.0f} - ${high:8,.0f}) | {count:<6d} | {bar}")
print("==================================================================\n")