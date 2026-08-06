# 🚀 AI Engineer Bootcamp - Day 30

## 📅 Date
06-08-2026

## 📚 Topics Covered


- # Day 30 — Pandas GroupBy & Data Aggregation

## Introduction

## GroupBy

## count()

## size()

## sum()

## mean()

## median()

## min()

## max()

## agg()

## Named Aggregation

## Multiple Columns

## Multiple GroupBy

## value_counts()

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run

## 📂 GitHub

Day30 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is GroupBy?

GroupBy is an operation that allows you to split data into distinct categories based on one or more keys, apply a calculation (such as averaging or counting) to each category, and combine the results into a single dataset.

It implements the classic Split-Apply-Combine strategy:

Split: Divides the DataFrame into subsets based on matching column values.

Apply: Computes an aggregation function independently on each subset.

Combine: Merges the results back into a structured tabular output.

2. Why do we use GroupBy?

Without GroupBy, analyzing segment-specific patterns in large datasets requires writing slow manual loops. GroupBy allows you to:

Aggregate high-volume data into concise executive summaries.

Compare metrics across categories (e.g., performance across branches or regions).

Identify segment-level outliers, trends, and anomalies fast.

Execute vectorized calculations optimized in C under the hood.

3. Difference between count() and size()?

Feature	count()	size()
Missing Values (NaNs)	Excludes missing values (NaN/None).	Includes all rows, counting NaN entries.
Output Type	Evaluates specific column(s).	Counts total rows in each group frame.
Use Case	Counting valid responses/records.	Counting total allocated records.
Python
# Example
df.groupby('Department')['Salary'].count() # Ignores missing salaries
df.groupby('Department').size()            # Total rows assigned to department

4. Difference between sum() and mean()?

sum(): Adds up all numerical values within a group. It calculates total magnitude (e.g., total departmental payroll budget).

mean(): Divides the sum() by the total number of non-null entries count(). It calculates the central tendency or average per record (e.g., average employee salary).

5. What does agg() do?

The .agg() (aggregation) function allows you to execute multiple statistical calculations at once or apply different calculations to different columns within a single GroupBy step.

Python
# Multiple metrics on a single column
df.groupby('Department')['Salary'].agg(['mean', 'median', 'max'])

# Custom metrics per column
df.groupby('Department').agg({
    'Salary': ['sum', 'mean'],
    'Age': 'mean',
    'Experience': 'max'
})

6. What is Named Aggregation?

Named Aggregation lets you specify clear, custom output column names directly inside .agg(), preventing Pandas from returning complex, multi-level indexed column headers.

Python
# Returns clean columns: Department | Total_Staff | Avg_Pay
df.groupby('Department').agg(
    Total_Staff=('EmployeeID', 'count'),
    Avg_Pay=('Salary', 'mean')
).reset_index()

7. How do you GroupBy multiple columns?

Pass a list of column names inside the .groupby() call. This creates multi-level hierarchy (sub-groups).

Python
# Breaks down metrics by Department, then further by City
df.groupby(['Department', 'City'])['Salary'].mean()

8. What is as_index=False?

By default, Pandas sets the grouping column(s) as the DataFrame index. Passing as_index=False preserves them as standard DataFrame columns, returning a flat output without needing to call .reset_index().

Python
# Returns 'Department' as a regular column instead of an index
df.groupby('Department', as_index=False)['Salary'].mean()

9. Why use value_counts()?

value_counts() quickly calculates the frequency distribution (row count and optional percentages) of unique categorical values in a Series or DataFrame without having to explicitly write a .groupby().size() statement.

Python
# Direct frequency count of employees per department
df['Department'].value_counts()

# Percentage breakdown
df['Department'].value_counts(normalize=True) * 100

10. Difference between GroupBy and value_counts()?

Metric	GroupBy	value_counts()
Primary Focus	Complex aggregations across numerical and categorical data.	Quick count/frequency calculation of unique categories.
Output Versatility	High (can calculate sum, mean, custom functions).	Single-purpose (counts or proportions).
Scope	Works across multi-column operations simultaneously.	Applied primarily on a single column or Series.

11. When is median better than mean?

Median is preferred over mean when data contains extreme outliers or is heavily skewed.

Mean includes all values equally, making it sensitive to extreme values (e.g., 5 executives earning $2,000,000 skewing the average salary of 100 staff members upwards).

Median represents the exact 50th percentile (middle value), providing a realistic representation of typical behavior in skewed distributions like income, property prices, or hospital stay durations.

12. How do you calculate department-wise salary?

Python
# Comprehensive salary metrics per department
department_salary = df.groupby('Department').agg(
    Total_Payroll=('Salary', 'sum'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

13. How do you calculate average age?
Python
# Average age overall
avg_age_overall = df['Age'].mean()

# Average age grouped by department
avg_age_dept = df.groupby('Department')['Age'].mean().reset_index()

14. How do you create a business summary report?

You aggregate key metrics using Named Aggregation and formatting methods:

Python
summary_report = df.groupby('Department').agg(
    Total_Employees=('EmployeeID', 'count'),
    Total_Spend=('Salary', 'sum'),
    Average_Salary=('Salary', 'mean'),
    Average_Experience=('Experience', 'mean')
).reset_index()

# Display formatted report
print("====== BUSINESS SUMMARY REPORT ======")
print(summary_report.to_string(index=False))

15. Where is GroupBy used in industry?

Finance & Banking: Summing daily transactional volumes, detecting fraud rates per merchant category, and calculating portfolio risks by asset class.

E-Commerce & Retail: Analyzing customer lifetime value (CLV) by acquisition channel, tracking inventory turn rates per category, and computing average order value (AOV).

Healthcare Analytics: Calculating average length of stay (ALOS) per clinical specialty, tracking patient readmission rates by hospital wing, and monitoring departmental treatment costs.

Human Resources (HR Analytics): Monitoring attrition rates by department, analyzing salary equity ratios across experience levels, and tracking training completion rates.