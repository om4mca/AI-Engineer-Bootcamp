# 🚀 AI Engineer Bootcamp - Day 28

## 📅 Date
04-08-2026

## 📚 Topics Covered


- # Day 28 — Pandas Data Selection, Filtering & Sorting

## Introduction

## Column Selection

## Row Selection

## iloc

## loc

## Conditional Filtering

## Multiple Conditions

## AND (&)

## OR (|)

## NOT (~)

## isin()

## String Filtering

## Sorting

## Multiple Column Sorting

## sort_index()

## reset_index()

## query()

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run

## 📂 GitHub

Day28 Completed Successfully ✅

## 🧠 Interview Preparation


1. 1. Selecting Columns
Single Column: Use single brackets (returns a Pandas Series) or double brackets (returns a 1-column DataFrame).

Python
df['age']         # Returns a Series
df[['age']]       # Returns a DataFrame
Multiple Columns: Pass a list of column names inside double brackets.

Python
df[['name', 'age', 'salary']]
2. Row Selection (iloc vs loc)
iloc (Integer-Location): Selects by numeric index position (0-indexed).

Python
df.iloc[0]          # First row
df.iloc[0:5]        # First 5 rows (position 0 up to 4)
df.iloc[0, 2]       # Row 0, Column 2
loc (Label-Location): Selects by label name or boolean conditions.

Python
df.loc['row_label'] # Row with a specific label
df.loc[0:5]         # Rows labeled 0 through 5 INCLUSIVE
df.loc[0, 'age']    # Row label 0, column named 'age'
3. Conditional Filtering Essentials
Conditional Filtering: Extracting a subset of rows where a specific logical condition evaluates to True.

Values Greater Than a Specific Number: Pass a boolean mask into .loc[] or bracket notation.

Python
df[df['age'] > 30]
4. Combining Multiple Conditions
Applying Multiple Conditions: Use bitwise operators (& for AND, | for OR, ~ for NOT).

Python
df[(df['age'] > 30) & (df['salary'] > 50000)]
Difference Between & and |:

& (AND): Both conditions must be True.

| (OR): At least one condition must be True.

What ~ Does: Negates a boolean condition (NOT). It flips True to False and vice versa.

Python
df[~(df['age'] > 30)]  # Selects rows where age is NOT > 30
Why Parentheses Are Crucial: Python’s operator precedence gives bitwise operators (&, |, ~) higher priority than comparison operators (>, <, ==). Without parentheses around each condition, Python throws a ValueError.

5. Specialized Filtering (isin & Strings)
isin() Method: Filters rows where a column's value matches any item in a provided list.

Python
df[df['department'].isin(['Sales', 'Marketing', 'HR'])]
Filtering String Values: Access string methods via the .str accessor.

Python
df[df['name'].str.startswith('A')]
.str.contains(): Checks whether a specific substring or regular expression pattern exists within text cells.

Python
# Finds rows where email contains '@gmail.com'
df[df['email'].str.contains('@gmail.com', na=False)] 
6. Sorting DataFrames
sort_values(): Sorts the DataFrame by the values of one or more specified columns.

Python
df.sort_values(by='age', ascending=False)
sort_index(): Sorts the DataFrame by its row or column labels (indexes) rather than cell values.

Python
df.sort_index(ascending=True)
Sorting by Multiple Columns: Pass a list of column names and corresponding sorting directions to ascending.

Python
df.sort_values(by=['department', 'salary'], ascending=[True, False])
What reset_index(drop=True) Does: Re-indexes the rows sequentially starting from 0 after filtering or sorting. drop=True prevents the old index from being saved as a new column.

Python
df_filtered = df[df['age'] > 30].reset_index(drop=True)
7. Advanced Syntax & Real-World Application
Purpose of query(): Allows filtering using clean, SQL-like string syntax, which makes code easier to read and often faster on large datasets.

Python
df.query("age > 30 and department == 'Sales'")
Usefulness in Real-World Data Analysis:

Data Cleaning: Removing outliers, invalid inputs, or missing entries.

Targeted Insights: Isolating specific cohorts (e.g., high-value customers, churned users).

Preprocessing: Preparing clean data subsets for machine learning models or visualization dashboards.