# 🚀 AI Engineer Bootcamp - Day 23

## 📅 Date
29-07-2026

## 📚 Topics Covered


- # Day 23 — NumPy Fundamentals

## Introduction

## What is NumPy?

## Why NumPy?

## Installation

## Importing NumPy

## NumPy Arrays

## 1D Arrays

## 2D Arrays

## Array Properties

- ndim
- shape
- size
- dtype
- itemsize

## Indexing

## Slicing

## Array Operations

## Mathematical Functions

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Runs






## 📂 GitHub

Day23 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is NumPy?

NumPy is the fundamental open-source Python library used for scientific computing, data analysis, and numerical operations. It introduces a powerful multi-dimensional array object (ndarray) along with an extensive collection of high-level mathematical functions.

2. What does NumPy stand for?

NumPy stands for Numerical Python.

3. Why is NumPy used in Data Science?

High Performance: Executes numerical computations significantly faster than native Python data structures.Vectorized Computations: Allows batch mathematical operations without slow for loops.Ecosystem Foundation: Serving as the core engine, major data science and AI libraries like Pandas, Scikit-Learn, PyTorch, and SciPy are built directly on top of NumPy.4. What is a NumPy array?A NumPy array (ndarray) is a grid of values—all of the exact same data type—indexed by a tuple of non-negative integers. It stores data in contiguous (continuous) memory blocks for optimized processing.

5. Difference between Python List and NumPy Array?

FeaturePython ListNumPy Array (ndarray)Data TypesHeterogeneous (can mix numbers, strings, objects).Homogeneous (all elements must be the exact same type).Memory AllocationMemory pointers scattered across different locations.Elements stored in contiguous, continuous memory blocks.Execution SpeedSlower due to dynamic type-checking overhead.Extremely fast due to optimized C-backend implementation.Math OperationsConcatenates or duplicates ([1, 2] * 2 = [1, 2, 1, 2]).Performs element-wise arithmetic (np.array([1, 2]) * 2 = [2, 4]).

6. What is a 1D array?

A 1D (One-Dimensional) array is a flat array or a single vector of numbers containing a single axis (Axis 0).Example: np.array([10, 20, 30])

7. What is a 2D array?

A 2D (Two-Dimensional) array is a grid of numbers arranged in rows and columns (a matrix). It contains two axes: Axis 0 (Rows) and Axis 1 (Columns).Example: np.array([[1, 2, 3], [4, 5, 6]])

8. What is ndim?

ndim is an array attribute that returns the number of dimensions (axes) of the array.Example: For a 2D matrix, arr.ndim returns 2.

9. What is shape?

shape is a tuple of integers indicating the size of the array along each dimension.Example: A matrix with 3 rows and 4 columns has a shape of (3, 4).

10. What is size?

size returns the total number of elements present across all dimensions in the array.Example: An array of shape (3, 4) has a size of $3 \times 4 = 12$.

11. What is dtype?

dtype (Data Type) specifies the type of data stored in the array elements (e.g., int32, int64, float64, bool).

12. What is itemsize?

itemsize returns the memory size of a single array element in bytes.Example: For int32, itemsize is 4 bytes; for float64, it is 8 bytes.

13. What is array indexing?

Array indexing is the method of accessing specific individual elements within an array using zero-based indices (e.g., arr[0] for 1D, or arr[row_index, col_index] for 2D).

14. What is array slicing?

Array slicing extracts a sub-section/range of elements from an array using the syntax [start:stop:step]. In 2D arrays, you can slice rows and columns independently: arr[row_start:row_stop, col_start:col_stop].

15. What are element-wise operations?

Element-wise operations are mathematical operations applied individually to every element in an array or corresponding pairs of elements across two equal-shaped arrays (e.g., adding two matrices together adds their matching indices directly).

16. How do you calculate the mean of an array?

Using NumPy's built-in np.mean() function:Pythonimport numpy as np

arr = np.array([10, 20, 30, 40])
mean_val = np.mean(arr)  # Output: 25.0


17. How do you find maximum and minimum values?

Using NumPy's np.max() (or arr.max()) and np.min() (or arr.min()) functions:
Python 
import numpy as np

arr = np.array([15, 88, 42, 4])
max_val = np.max(arr)  # Output: 88
min_val = np.min(arr)  # Output: 4

18. Why is NumPy faster for numerical operations?Contiguous Memory: Elements are stored right next to each other in RAM, maximizing processor cache efficiency.Compiled C Code: Operations run directly via pre-compiled, highly optimized C and Fortran binaries rather than interpreted Python loops.No Dynamic Type-Checking: Since all elements share the same dtype, NumPy skips type validation during iteration.

19. What is vectorization?

Vectorization is the process of executing mathematical operations across entire arrays simultaneously without writing explicit for loops in Python code. The looping happens internally at the C level.

20. What is the role of NumPy in Machine Learning?

Data Representation: Features, images, and tabular inputs are converted into NumPy matrices/tensors before model training.Linear Algebra Computations: Powers fundamental operations like matrix multiplication, dot products, and vector norms needed in regression, neural networks, and optimization.Integration: Frameworks like Scikit-Learn, PyTorch, and TensorFlow take NumPy arrays natively as training input.