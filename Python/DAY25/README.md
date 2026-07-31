# 🚀 AI Engineer Bootcamp - Day 25

## 📅 Date
31-07-2026

## 📚 Topics Covered


- # Day 25 — NumPy Mathematics, Statistics & Aggregation

## Introduction

## Mathematical Functions

- sum()
- mean()
- median()
- min()
- max()

## Statistical Functions

- std()
- var()
- percentile()

## Index Functions

- argmin()
- argmax()

## Cumulative Operations

- cumsum()
- cumprod()

## Unique Values

## Sorting

## Axis

## keepdims

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run



## 📂 GitHub

Day25 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is NumPy aggregation?

NumPy aggregation refers to functions that take an array of values and compute a single summary value (or a reduced set of values) across specified axes, such as finding the sum, average, minimum, or maximum.

2. What does np.sum() do?

It calculates the sum of all elements in an array or along a specified axis.

3. Difference between mean and median?

Mean (np.mean): The arithmetic average (sum of values divided by the count). It is sensitive to extreme values (outliers).Median (np.median): The middle value when the data is sorted. It is robust against outliers.

4. What is standard deviation?

Standard deviation ($\sigma$ or $s$) measures the average amount of variability or spread of data points relative to their mean. A low value means points are clustered near the mean; a high value means they are widely spread out.

5. What is variance?

Variance ($\sigma^2$ or $s^2$) measures how far a set of numbers are spread out from their mean, calculated as the average of the squared deviations from the mean.

6. What is the relationship between variance and standard deviation?

Standard deviation is the square root of variance:$$\text{Standard Deviation} = \sqrt{\text{Variance}}$$(Conversely, Variance is the square of Standard Deviation: $\text{Variance} = \text{Standard Deviation}^2$).

7. What does np.argmin() return?

It returns the index (position) of the minimum element in an array along a specified axis.

8. What does np.argmax() return?

It returns the index (position) of the maximum element in an array along a specified axis.Advanced Operations

9. What is cumulative sum?

np.cumsum() returns the running total of array elements. For example, [1, 2, 3] becomes [1, 1+2, 1+2+3] $\rightarrow$ [1, 3, 6].

10. What is cumulative product?

np.cumprod() returns the running product of array elements. For example, [1, 2, 3, 4] becomes [1, 1*2, 1*2*3, 1*2*3*4] $\rightarrow$ [1, 2, 6, 24].

11. What is a percentile?

A percentile is a measure indicating the value below which a given percentage of observations fall. For example, the 25th percentile is the value below which 25% of the data lies.

12. What is the 50th percentile?

The 50th percentile is the Median—exactly half the dataset falls below this value and half above it.

13. What does np.unique() do?

It finds and returns the sorted unique (distinct) elements of an array, removing duplicate entries.

14. How do you count unique values?

By setting the parameter return_counts=True inside np.unique(). For example:Pythonvalues, counts = np.unique(arr, return_counts=True)

15. What does np.sort() do?

It returns a sorted copy of an array without modifying the original array (unlike Python's list .sort() which mutates in place).Axes & Dimensions

16. What is an axis in NumPy?

An axis refers to a specific direction or dimension along an array. In a 2D array:Axis 0 refers to rows.Axis 1 refers to columns.

17. Difference between axis=0 and axis=1?

axis=0: Operates vertically down columns (collapsing rows).axis=1: Operates horizontally across rows (collapsing columns).

18. What is keepdims=True?

When applying aggregation functions (like np.mean or np.sum), keepdims=True keeps the reduced axes in the output as dimensions with size 1 (e.g., maintaining shape (N, 1) instead of reducing to a 1D array of shape (N,)). This prevents shape mismatch errors during element-wise operations.Practical Applications

19. Why are aggregation functions important in Data Analysis?

Data Summarization: Quickly summarize large, complex datasets into understandable metrics.Missing Value Handling & Outlier Detection: Spot extreme values or skewed data using percentiles and ranges.Feature Understanding: Identify general patterns, distributions, and variance across data attributes.

20. How is NumPy aggregation useful in Machine Learning?

Data Normalization / Scaling: Subtracting column means and dividing by standard deviations ($Z$-score normalization).Loss Functions: Calculating mean squared error (MSE) or mean absolute error (MAE) during model training using np.mean().Classification Decisions: Converting output probabilities into predicted class labels using np.argmax().