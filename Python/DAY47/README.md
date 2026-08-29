# 🚀 AI Engineer Bootcamp - Day 47

## 📅 Date
29-08-2026

## 📚 Topics Covered


- # Day 47 — Systems of Linear Equations

## Introduction

## Linear Equations

## Systems of Linear Equations

## Matrix Representation

## A x = b

## Coefficient Matrix

## Constant Vector

## Augmented Matrix

## np.linalg.solve()

## Solution Verification

## Unique Solution

## No Solution

## Infinite Solutions

## Rank and Linear Systems

## Singular Systems

## Machine Learning Applications

## Employee Parameter Solver

## Hospital Parameter Equation System

## Practice Programs

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day47 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is a linear equation?

An algebraic equation where every term is either a constant or the product of a constant and a single variable raised to the power of 1 (no exponents, square roots, or products like $xy$).Algebraic Form: $a_1 x_1 + a_2 x_2 + \dots + a_n x_n = b$Geometric Form: Represents a straight line in 2D, a plane in 3D, and a hyperplane in $n$-dimensional space.

2. What is a system of linear equations?

A collection of two or more linear equations involving the same set of variables:$$\begin{aligned}    2x_1 + 3x_2 &= 8 \\    4x_1 - 1x_2 &= 2    \end{aligned}$$Solving the system means finding values for $(x_1, x_2, \dots, x_n)$ that simultaneously satisfy every equation.

3. How can a system of equations be represented using matrices?

A system of linear equations can be written compactly as a single matrix-vector equation:$$A \vec{x} = \vec{b}$$For example, the 2D system above is represented as:$$\begin{bmatrix} 2 & 3 \\ 4 & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 8 \\ 2 \end{bmatrix}$$

4. What does $A \vec{x} = \vec{b}$ mean?

$A \vec{x} = \vec{b}$ expresses linear systems under two distinct viewpoints:Row View: The dot product of each row of $A$ with vector $\vec{x}$ equals the corresponding scalar entry in $\vec{b}$.Column View (Linear Combination): Vector $\vec{b}$ is represented as a linear combination of the column vectors of matrix $A$, scaled by the components of vector $\vec{x}$:$$x_1 \vec{a}_1 + x_2 \vec{a}_2 + \dots + x_n \vec{a}_n = \vec{b}$$

5. What is a coefficient matrix?

The coefficient matrix (denoted as $A$) is an $m \times n$ matrix containing only the numerical coefficients of the variables, where rows correspond to equations and columns correspond to variables.

6. What is a constant vector?

The constant vector (denoted as $\vec{b}$) is an $m \times 1$ column vector containing the right-hand side constant values from each equation in the system.

7. What is an augmented matrix?

An augmented matrix (denoted as $[A \mid \vec{b}]$) is formed by attaching the constant vector $\vec{b}$ as an extra column to the right side of the coefficient matrix $A$:$$[A \mid \vec{b}] = \left[\begin{array}{cc\|c} 2 & 3 & 8 \\ 4 & -1 & 2 \end{array}\right]$$It is used during Gaussian Elimination to track operations on coefficients and constants simultaneously.

8. What does np.linalg.solve() do?

In NumPy, np.linalg.solve(A, b) computes the exact solution vector $\vec{x}$ for the system $A \vec{x} = \vec{b}$.
Rather than computing $A^{-1} \vec{b}$ directly (which is computationally inefficient), it uses LAPACK routines (specifically LU decomposition with partial pivoting) to calculate $\vec{x}$ efficiently.

9. How can you verify a solution?

Algebraically: Substitute $\vec{x}_{\text{calc}}$ back into $A \vec{x}_{\text{calc}}$ and check if it produces vector $\vec{b}$.In Code: Use np.allclose(A @ x_calc, b) to verify equality within floating-point tolerance.Pythonimport numpy as np

A = np.array([[2, 3], [4, -1]])
b = np.array([8, 2])

x = np.linalg.solve(A, b)
is_valid = np.allclose(A @ x, b)
print("Solution x:", x)          # Output: [1.4, 1.7333...]
print("Valid Solution?", is_valid) # Output: True

10. What is a unique solution?

A system has a unique solution when exactly one specific vector $\vec{x}$ satisfies $A \vec{x} = \vec{b}$.Geometric View: The hyperplanes represented by the equations intersect at a single point.Algebraic View: Matrix $A$ is square and full-rank ($\text{Rank}(A) = n$), meaning $\det(A) \neq 0$.

11. What does it mean when a system has no solution?

A system has no solution (an inconsistent system) when no vector $\vec{x}$ satisfies all equations simultaneously.Geometric View: The lines/planes are parallel and never intersect at a common point.Algebraic View: Vector $\vec{b}$ lies outside the column space of $A$, meaning $\text{Rank}(A) < \text{Rank}([A \mid \vec{b}])$.

12. What does infinitely many solutions mean?

A system has infinitely many solutions when an infinite number of vectors $\vec{x}$ satisfy the system.Geometric View: The equations represent redundant/overlapping lines or planes that intersect along an entire line or plane.Algebraic View: Matrix $A$ has free variables and is rank deficient ($\text{Rank}(A) = \text{Rank}([A \mid \vec{b}]) < n$).

13. Why can np.linalg.solve() fail?

np.linalg.solve() throws a LinAlgError: Singular matrix under these conditions:Singular Matrix: Matrix $A$ is square but rank-deficient ($\det(A) = 0$).Non-Square Matrix: Matrix $A$ does not have equal rows and columns ($m \neq n$). (Use np.linalg.lstsq() instead for non-square systems).Severe Ill-Conditioning: Matrix $A$ has an extremely high condition number, causing numerical floating-point errors during decomposition.

14. How is rank related to solving linear systems?

The Rouché–Capelli Theorem governs system solvability using matrix rank:Rank ConditionSolvability StatusNumber of Solutions$\text{Rank}(A) < \text{Rank}([A \mid \vec{b}])$Inconsistent0 Solutions$\text{Rank}(A) = \text{Rank}([A \mid \vec{b}]) = n$Consistent1 Unique Solution$\text{Rank}(A) = \text{Rank}([A \mid \vec{b}]) < n$ConsistentInfinitely Many Solutions

15. Why are systems of linear equations important in Machine Learning?

Ordinary Least Squares (OLS) Regression: Finding optimal model parameters $\hat{\theta}$ requires solving the Normal Equations system:$$(X^T X) \hat{\theta} = X^T y$$Neural Networks: Every dense neural network layer performs matrix-vector linear transformations ($\vec{z} = W \vec{x} + \vec{b}$) and linear backpropagation updates.Principal Component Analysis (PCA): Finding principal axes involves solving the characteristic linear system $(A - \lambda I)\vec{v} = \vec{0}$ for eigenvalues and eigenvectors.Optimization Algorithms: Optimization algorithms (e.g., Newton's method) solve linear systems involving Hessian matrices ($H \Delta \theta = -\nabla L$).