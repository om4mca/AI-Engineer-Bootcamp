# 🚀 AI Engineer Bootcamp - Day 42

## 📅 Date
24-08-2026

## 📚 Topics Covered


- # Day 42 — Matrices & Matrix Fundamentals

## Introduction

## What is a Matrix?

## Matrix Dimensions

## Rows and Columns

## Matrix Elements

## Matrix Indexing

## Matrix Slicing

## Matrix Addition

## Matrix Subtraction

## Scalar Multiplication

## Matrix Transpose

## Identity Matrix

## Zero Matrix

## Element-wise Multiplication

## Matrix Multiplication

## NumPy Matrix Operations

## Feature Matrix

## Employee Feature Matrix Analyzer

## Hospital Patient Feature Matrix Analyzer

## Practice Programs

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day41 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is a matrix?

A matrix is a two-dimensional rectangular array of numbers organized in rows and columns.

2. What do rows and columns represent?

In data analysis, rows represent individual data points or samples (e.g., individual patients or employees), while columns represent attributes or features of those samples (e.g., age, salary, blood pressure).

3. What does a $3 \times 4$ matrix mean?

It means the matrix consists of 3 rows and 4 columns, containing a total of 12 elements.

4. How do you find matrix dimensions in NumPy?

Use the .shape attribute on a NumPy array (e.g., matrix.shape).

5. How does NumPy indexing work for matrices?

NumPy uses zero-based indexing via [row_index, col_index]. For example, matrix[0, 2] accesses the element in the 1st row and 3rd column.

6. How do you select a complete row?

Use a single row index with a colon : for columns: matrix[row_index, :].

7. How do you select a complete column?

Use a colon : for all rows with a single column index: matrix[:, col_index].

8. What is matrix slicing?

Matrix slicing is extracting a sub-region of a matrix using index ranges formatted as [start_row:stop_row, start_col:stop_col].

9. How do you add two matrices?

You add their corresponding elements together. Both matrices must have the exact same dimensions ($m \times n$).

10. What is scalar multiplication?

Multiplying every individual element of a matrix by a single constant number (a scalar).

11. What is a matrix transpose?

Flipping a matrix over its main diagonal, turning its rows into columns and its columns into rows (changing an $m \times n$ matrix into an $n \times m$ matrix).

12. What is an identity matrix?

A square matrix with ones along its main diagonal (top-left to bottom-right) and zeros everywhere else. Multiplying any matrix by an identity matrix leaves it unchanged.

13. What is a zero matrix?

A matrix in which all elements are zero.

14. Difference between A * B and A @ B in NumPy?

A * B: Performs element-wise multiplication (Hadamard product), requiring both matrices to have identical shapes.A @ B: Performs standard matrix multiplication (dot product), requiring the number of columns in A to match the number of rows in B.

15. Why are matrices important in Machine Learning?

Matrices allow algorithms to process large datasets simultaneously through vectorized operations, vastly speeding up computations compared to looping over individual data points.