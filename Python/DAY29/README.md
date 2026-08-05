# 🚀 AI Engineer Bootcamp - Day 29

## 📅 Date
05-08-2026

## 📚 Topics Covered


- # Day 29 — Pandas Data Cleaning & Missing Data

## Introduction

## Missing Data

## Detecting Missing Values

## Handling Missing Values

## dropna()

## fillna()

## Forward Fill

## Backward Fill

## Duplicate Data

## Removing Duplicates

## Renaming Columns

## Changing Data Types

## unique()

## value_counts()

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run

## 📂 GitHub

Day29 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is missing data?

Missing data refers to data values that are absent, unrecorded, or undefined within a dataset. It occurs due to human error, system glitches, optional survey fields, or failed sensor measurements.

2. Difference between None and NaN?

FeatureNoneNaN (Not a Number)OriginNative Python NoneType objectNumPy float value (np.nan)TypePython NoneTypeFloating-point (float)PerformanceSlower; forces object dtype in arraysFaster; vectorizable across numeric columnsBehavior in PandasAutomatically converted to NaN in numeric/object columnsPreserved as standard missing value indicator

3. What does isnull() do?

isnull() evaluates each element in a Pandas DataFrame or Series and returns a boolean mask (True if the value is missing, False if valid).

4. Difference between isnull() and isna()?

There is no functional difference. isna() was added to match R’s naming convention (is.na()). isnull() and isna() are exact aliases in Pandas.

5. How do you count missing values?

Use .isna().sum() to sum up True instances column-by-column:Python# Missing counts per column
df.isna().sum()

# Total missing values across entire DataFrame
df.isna().sum().sum()
Part 2: Handling Missing Data

6. What does dropna() do?

dropna() drops rows or columns containing missing (NaN or None) values from a DataFrame.

7. Difference between dropna(axis=0) and dropna(axis=1)?

dropna(axis=0) (Default): Removes rows that contain missing values.dropna(axis=1): Removes columns that contain missing values.

8. What does fillna() do?

fillna() replaces missing (NaN) values with a specified default value, statistical metric (mean, median), or propagation strategy.

9. Why use mean for missing numeric values?

Filling missing values with the mean preserves the overall mean of the dataset without changing the total sum. It works best when data is normally distributed without severe outliers.

10. Why use median instead of mean in some cases?

The median (middle value) is robust against extreme outliers and skewed distributions (e.g., salary, house prices). Unlike the mean, extreme values do not distort the median.

11. What is forward fill (ffill)?

Forward fill propagates the last observed valid value forward to replace subsequent missing values. Common in time-series data (e.g., filling weekend stock prices with Friday's close).

12. What is backward fill (bfill)?

Backward fill uses the next available valid value to fill preceding missing entries.Part 3: Structuring & Cleaning Data

13. What are duplicate rows?

Duplicate rows are identical entries in a dataset where every column value (or specified key subset) matches another row, often created by multiple data joins or entry errors.

14. How do you remove duplicates?

Use drop_duplicates():Python# Remove identical rows across all columns
df = df.drop_duplicates()

# Remove duplicates based on a specific key column
df = df.drop_duplicates(subset=['Patient_ID'], keep='first')

15. What does rename() do?

rename() modifies column headers or index labels:Pythondf = df.rename(columns={'Old_Name': 'New_Name'})

16. What is astype()?

astype() casts a Pandas Series or column from one data type to another (e.g., converting a float 34.0 to integer 34 or a string to datetime).

17. Difference between unique() and nunique()?

unique(): Returns an array of unique values (including NaN).nunique(): Returns the integer count of unique values (excludes NaN by default).

18. What does value_counts() return?

value_counts() returns a Series containing the counts of unique values in descending order, showing category frequencies.Part 4: Importance of Data Cleaning

19. Why is data cleaning important?

Accuracy: Prevents distorted metrics, false reports, and wrong business decisions.Consistency: Standardizes column names, formats, and data types across source systems.Integrity: Eliminates noise, incomplete records, and corrupt entries.

20. Why is data cleaning critical before Machine Learning?

Model Failure: Most Scikit-Learn models crash when fed NaN or unencoded string values.Garbage In, Garbage Out: Models trained on duplicates, unhandled outliers, or improper data types learn wrong patterns and generalize poorly.Data Leakage Prevention: Deduplication ensures identical samples do not split into both training and test sets, which inflates model accuracy artificially.