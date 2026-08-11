# 🚀 AI Engineer Bootcamp - Day 34

## 📅 Date
11-08-2026

## 📚 Topics Covered


- # Day 34 — Exploratory Data Analysis

## Introduction

## What is EDA?

## EDA Workflow

## Dataset Inspection

## Data Types

## Missing Values

## Duplicate Records

## Statistical Analysis

## Categorical Analysis

## Numerical Analysis

## Data Visualization

## Relationship Analysis

## Employee EDA Project

## Hospital EDA Project

## Key Insights

## Practice Programs

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day34 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is EDA?

Exploratory Data Analysis (EDA) is the critical initial process of analyzing, summarizing, and visualizing a dataset to understand its underlying structure, spot anomalies, identify missing values, detect patterns, and test hypotheses before applying statistical modeling or machine learning.

2. Why is EDA important?

Ensures Data Quality: Uncovers missing values, duplicates, and invalid data types.Guides Feature Selection: Highlights which variables have strong relationships with the target variable.Prevents Garbage-In, Garbage-Out: Ensures algorithms aren't trained on flawed or noisy data.Informs Algorithm Choice: Reveals whether data is linear, skewed, or contains extreme outliers, guiding the choice of machine learning models.

3. What is the first step in EDA?

Understanding the data structure and metadata (shape, columns, and data types). This usually involves running df.shape, df.head(), and df.info() to get a high-level overview of the dataset.🐍 Pandas Inspection Commands

4. What does df.shape return?

It returns a tuple representing the dimensions of the DataFrame as (number_of_rows, number_of_columns). Note that it is an attribute, not a method, so it does not use parentheses.

5. Difference between head() and tail()?

df.head(n): Returns the first $n$ rows of the DataFrame (default $n = 5$). Useful for inspecting top records and checking column alignment.df.tail(n): Returns the last $n$ rows of the DataFrame (default $n = 5$). Useful for verifying total row loading and bottom records.

6. What does info() provide?

df.info() outputs a concise technical summary of the DataFrame:Total number of rows and columns.Index range.Column names.Non-null value count per column (helps identify missing data).Data type (dtype) of each column.Total memory usage.

7. What does describe() provide?

df.describe() returns summary statistics for numerical columns:count: Number of non-missing values.mean & std: Average and standard deviation.min & max: Minimum and maximum values.25%, 50% (median), 75%: Quartiles indicating data spread.(Note: df.describe(include='object') can be used to get counts, unique values, and top categories for text/categorical columns).🧹 Data Cleaning & Quality

8. How do you check missing values?

df.isnull() or df.isna(): Returns a Boolean DataFrame (True for missing values).df.isnull().sum(): Sums True values per column to give the count of missing values.(df.isnull().sum() / len(df)) * 100: Gives the percentage of missing values per column.

9. How do you check duplicates?

df.duplicated(): Returns a Boolean Series (True for duplicate rows).df.duplicated().sum(): Gives the total count of duplicate rows.

10. Difference between unique() and nunique()?

df['col'].unique(): Returns an array of distinct values present in the column.df['col'].nunique(): Returns an integer count of distinct values in the column (by default, excludes NaN values).

11. What does value_counts() do?

df['col'].value_counts() returns a Series containing counts of unique values in descending order. It is the primary tool for frequency distribution of categorical features. Setting normalize=True returns relative frequencies (percentages).📊 Feature Analysis & Visualization

12. How do you analyze categorical data?

Summary Functions: value_counts(), unique(), nunique().Visualizations: Bar charts (plt.bar / sns.countplot), pie charts.Cross-Analysis: Contingency tables / Cross-tabulations (pd.crosstab()).

13. How do you analyze numerical data?

Summary Statistics: describe(), mean, median, standard deviation, skewness, kurtosis.Visualizations: Histograms (for distribution shape), Box plots (for quartiles and outliers), KDE plots (for probability density).

14. How can Matplotlib help during EDA?

Matplotlib provides the fundamental canvas to render static, customizable visual representations of data patterns:Univariate Plots: Histograms, Bar plots, Box plots to inspect single variables.Bivariate Plots: Scatter plots, Line charts to examine relationships between two variables.Multivariate Plots: Multi-panel subplots (plt.subplots()) to display integrated performance dashboards.

15. What is a distribution?

A distribution shows how values of a variable are spread or scattered across its range. It reveals the central tendency (mean/median), spread (variance), and shape (e.g., normal/bell-curve, uniform, or skewed right/left).

16. What is an outlier?

An outlier is a data point that differs significantly from other observations in the dataset. Outliers can arise from measurement errors, data entry mistakes, or genuine rare events. They are commonly identified visually using Boxplots or mathematically using the Interquartile Range (IQR) method or Z-scores.💡 Advanced & Strategic Interview Questions

17. Why should EDA be performed before Machine Learning?

Prevents Data Leakage: Ensures train-test split boundaries are maintained cleanly.Informs Preprocessing: Identifies whether imputation, scaling, log transformations (for skewed distributions), or encoding strategies (One-Hot vs Target Encoding) are needed.Identifies Multicollinearity: Uncovers redundant, highly correlated predictor variables.

18. What is the difference between Data Cleaning and EDA?

Data Cleaning is an operational process focused on fixing dirty data (handling missing values, dropping duplicates, correcting wrong data types, standardizing formats).EDA is an investigative process focused on gaining insights, discovering patterns, testing assumptions, and formulating hypotheses. Data cleaning is often informed and driven by EDA findings.

19. How do you find relationships between variables?

Numerical vs Numerical: Scatter plots, Correlation matrices (df.corr()), Heatmaps.Categorical vs Numerical: GroupBy aggregations (df.groupby('Category')['Numerical'].mean()), Boxplots, Violin plots.Categorical vs Categorical: Cross-tabulations (pd.crosstab()), Stacked Bar charts.

20. What is a data insight?

A data insight is a meaningful, actionable finding derived from analyzing data that provides context and leads to strategic decision-making. It goes beyond describing what the data says to explaining why it matters and what action should be taken.Example:Raw Data: "Cardiology patients stay an average of 8 days."Data Insight: "Cardiology stay duration strongly correlates with high total bills ($50k+). Implementing an early-discharge protocol for non-critical cardiology patients could reduce bed occupancy by 15% and cut patient out-of-pocket costs."