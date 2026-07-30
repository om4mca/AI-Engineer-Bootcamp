# 🚀 AI Engineer Bootcamp - Day 24

## 📅 Date
30-07-2026

## 📚 Topics Covered


- # Day 24 — NumPy Array Creation & Advanced Operations

## Introduction

## Array Creation
- zeros()
- ones()
- full()
- arange()
- linspace()

## Random Arrays

## Random Seed

## Reshaping

## Flattening
- flatten()
- ravel()

## Concatenation

## Splitting

## Boolean Indexing

## Multiple Conditions

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run





## 📂 GitHub

Day24 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is np.zeros()?

np.zeros() creates a new NumPy array of a given shape and type, where every element is initialized to 0. It is commonly used as a blank canvas or memory pre-allocation step before populating values in a loop.

2. What is np.ones()?

np.ones() creates an array of a specified shape and data type where every element is initialized to 1. It is used in mathematical transformations, scaling operations, or creating identity-like masks.

3. What is np.full()?

np.full() creates an array filled entirely with a custom constant value specified by the user.

Python
import numpy as np

arr = np.full((2, 3), fill_value=7)
# Output:
# [[7 7 7]
#  [7 7 7]]

4. Difference between np.arange() and np.linspace()?

Feature	np.arange()	np.linspace()
Control Parameter	You specify the step size between numbers.	You specify the total count of numbers you want.
Stop Value	Excludes the stop value (like standard Python range).	Includes the stop value by default (endpoint=True).
Primary Use Case	When fixed incremental leaps are needed (e.g., every 2 units).	When dividing an interval into N equal segments (e.g., plotting curves).

5. What is np.random module?

np.random is a sub-module in NumPy containing algorithms for generating pseudo-random numbers drawn from various probability distributions (e.g., Uniform, Normal/Gaussian, Binomial). It is foundational for simulations, weight initializations in ML, and data shuffling.

6. Why is np.random.seed() used?

np.random.seed() locks the random number generator to a fixed starting point. This guarantees reproducibility: anyone running the code with the exact same seed value will generate the exact same set of "random" numbers every single time.

7. What is reshape()?

reshape() changes the dimensions (number of rows, columns, or depth blocks) of an existing array without altering its underlying data or total element count.

8. What is the important rule when reshaping an array?

The Cardinal Rule: The total number of elements in the original array must exactly match the total number of elements in the reshaped array.

Original Size=New Rows×New Columns×…
Example: A 1D array of 12 elements can be reshaped into (3×4), (2×6), or (12×1), but not (3×5) because 3×5=15

=12.

9. What does -1 mean in reshape()?

Passing -1 as a dimension parameter tells NumPy to automatically compute that dimension's size based on the array's total length and the other specified dimensions.

Python
x = np.arange(12)  # Total 12 elements
y = x.reshape(3, -1)  # NumPy automatically infers columns = 12 / 3 = 4

10. Difference between flatten() and ravel()?

flatten(): Returns a deep copy of the array in 1D. Modifying the flattened array will not affect the original array.

ravel(): Returns a view (reference) of the original array in 1D whenever possible. Modifying a raveled array will modify the original array (faster and memory-efficient).

11. What is array concatenation?

Array concatenation is the process of joining two or more arrays together along an existing axis using np.concatenate().

12. What is axis in NumPy?

An axis represents a direction or dimension along which operations occur in a multi-dimensional array:

1D Arrays have 1 axis: axis=0

2D Arrays have 2 axes: axis=0 and axis=1

13. Difference between axis=0 and axis=1 in 2D arrays?

               axis=1 (Columns / Horizontal) ➔
               ┌─────────┬─────────┬─────────┐
axis=0         │ Row 0   │  (0,1)  │  (0,2)  │
(Rows /        ├─────────┼─────────┼─────────┤
Vertical)      │ Row 1   │  (1,1)  │  (1,2)  │
↓              └─────────┴─────────┴─────────┘
axis=0: Operates vertically across rows (downwards). For concatenation, it stacks rows on top of each other.

axis=1: Operates horizontally across columns (left-to-right). For concatenation, it glues columns side-by-side.

14. What is array splitting?

Array splitting (np.split()) is the inverse of concatenation. It divides a single array into multiple smaller sub-arrays along a designated axis.

15. What is Boolean indexing?

Boolean indexing (also called masking) involves using conditional logical statements on an array to produce an array of True/False values. Passing this boolean mask back into the array filters out all False entries and returns only the elements where the condition evaluated to True.

16. How do you filter values greater than a specific number?

You pass a conditional expression inside square brackets [ ]:

Python
arr = np.array([10, 50, 25, 80, 5])
filtered = arr[arr > 30]  # Returns: [50, 80]

17. How do you apply multiple conditions in NumPy?

You combine separate conditional expressions wrapped in parentheses () using bitwise logical operators (&, |, ~).

Python
arr = np.array([10, 25, 40, 60, 80])
result = arr[(arr > 20) & (arr < 70)]  # Returns: [25, 40, 60]

18. Difference between & and |?

& (Bitwise AND): Returns True only if both surrounding conditions evaluate to True.

| (Bitwise OR): Returns True if at least one of the surrounding conditions evaluates to True.

19. Why are NumPy arrays useful for data filtering?

No Loops Needed: NumPy performs vectorized filtering in C-level speed, eliminating slow Python for loops.

Memory Efficiency: Boolean masks evaluate operations directly across contiguous memory blocks.

Readable Syntax: Filtering expressions closely resemble standard algebraic and mathematical notations.

20. How is Boolean indexing useful in Machine Learning?

Outlier Removal: Instantly dropping data points outside acceptable boundaries (e.g., data[data < threshold]).

Handling Missing Data (NaNs): Filtering out missing entries using data[~np.isnan(data)].

Categorical Filtering: Extracting target sub-samples (e.g., isolating all y_train == 1 positive class instances).

Creating Binary Targets: Thresholding continuous probabilities into binary classes (e.g., predictions = probabilities > 0.5).

