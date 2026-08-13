import numpy as np
import pandas as pd

# 1. Create Synthetic Employee Dataset (N = 1000)
np.random.seed(42)  # For reproducible results

n_employees = 1000

departments = ["IT", "HR", "Finance", "Sales"]
dept_probs = [0.40, 0.20, 0.24, 0.16]  # Matching previous distributions

data = {
    "EmployeeID": range(101, 101 + n_employees),
    "Name": [f"Employee_{i}" for i in range(1, n_employees + 1)],
    "Department": np.random.choice(departments, size=n_employees, p=dept_probs),
    "Age": np.random.randint(22, 60, size=n_employees),
    "Salary": np.random.normal(loc=65000, scale=18000, size=n_employees).round(
        -2
    ),
    "Experience": np.random.randint(0, 35, size=n_employees),
}

df = pd.DataFrame(data)

# 2. Probability Calculation Function
total_n = len(df)


def calc_prob(condition):
    count = condition.sum()
    probability = count / total_n
    percentage = probability * 100
    return count, probability, percentage


# 3. Compute Requested Probabilities
prob_it_cnt, prob_it, prob_it_pct = calc_prob(df["Department"] == "IT")
prob_hr_cnt, prob_hr, prob_hr_pct = calc_prob(df["Department"] == "HR")
prob_sal_cnt, prob_sal, prob_sal_pct = calc_prob(df["Salary"] > 50000)
prob_age_cnt, prob_age, prob_age_pct = calc_prob(df["Age"] > 30)
prob_exp_cnt, prob_exp, prob_exp_pct = calc_prob(df["Experience"] > 5)

# 4. Display Probability Results
print("=" * 60)
print("             📊 EMPLOYEE PROBABILITY ANALYSIS             ")
print("=" * 60)
print(f"Total Dataset Size (N): {total_n}\n")

print(f"P(IT Employee)          : {prob_it:.4f}  | {prob_it_pct:.1f}%")
print(f"P(HR Employee)          : {prob_hr:.4f}  | {prob_hr_pct:.1f}%")
print(f"P(Salary > $50,000)     : {prob_sal:.4f}  | {prob_sal_pct:.1f}%")
print(f"P(Age > 30)             : {prob_age:.4f}  | {prob_age_pct:.1f}%")
print(f"P(Experience > 5 years) : {prob_exp:.4f}  | {prob_exp_pct:.1f}%")
print("=" * 60)



# 1. Create Employee Dataset (N = 1000)
np.random.seed(42)

n = 1000
data = {
    'EmployeeID': range(101, 101 + n),
    'Name': [f'Employee_{i}' for i in range(1, n + 1)],
    'Department': np.random.choice(['IT', 'HR', 'Finance', 'Sales'], size=n, p=[0.40, 0.20, 0.24, 0.16]),
    'Age': np.random.randint(22, 60, size=n),
    'Salary': np.random.normal(loc=65000, scale=18000, size=n).round(-2),
    'Experience': np.random.randint(0, 35, size=n)
}

df = pd.DataFrame(data)

# 2. Calculate Probabilities
p_it = (df['Department'] == 'IT').mean() * 100
p_hr = (df['Department'] == 'HR').mean() * 100
p_salary_50k = (df['Salary'] > 50000).mean() * 100
p_age_30 = (df['Age'] > 30).mean() * 100
p_exp_5 = (df['Experience'] > 5).mean() * 100

# Additional probabilities for deeper insights
p_it_high_salary = ((df['Department'] == 'IT') & (df['Salary'] > 50000)).mean() * 100
p_senior = (df['Age'] > 45).mean() * 100

# 3. Print 5 Key Insights using Python
print("=" * 65)
print("             💡 5 KEY PROBABILITY INSIGHTS")
print("=" * 65)

print(f"1. Probability of selecting an IT employee = {p_it:.1f}%")
print(f"   -> IT is the largest department in the workforce.")

print(f"\n2. Probability of selecting an employee with Salary > $50,000 = {p_salary_50k:.1f}%")
print(f"   -> Nearly 8 out of 10 employees earn above the $50k threshold.")

print(f"\n3. Probability of selecting an employee with Experience > 5 years = {p_exp_5:.1f}%")
print(f"   -> Over 80% of the workforce consists of experienced professionals.")

print(f"\n4. Probability of selecting an employee aged over 30 = {p_age_30:.1f}%")
print(f"   -> The majority of the team represents a mature demographic.")

print(f"\n5. Probability of selecting an HR employee = {p_hr:.1f}%")
print(f"   -> For every 1 HR staff member, there are approximately {p_it/p_hr:.1f} IT employees.")

print("=" * 65)