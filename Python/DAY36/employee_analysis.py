import pandas as pd

# Employee data setup
data = {'IT': 200, 'HR': 100, 'Finance': 120, 'Sales': 80}

total_employees = sum(data.values())

# Calculate probabilities and percentages
results = []
for department, count in data.items():
    prob = count / total_employees
    percent = prob * 100
    results.append(
        {
            'Department': department,
            'Count': count,
            'Probability (Decimal)': round(prob, 2),
            'Probability (%)': f'{percent:.1f}%',
        }
    )

# Convert to Pandas DataFrame for clear display
df_results = pd.DataFrame(results)

print(f"Total Employees: {total_employees}\n")
print(df_results.to_string(index=False))