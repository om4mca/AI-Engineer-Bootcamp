# 🚀 AI Engineer Bootcamp - Day 43

## 📅 Date
25-08-2026

## 📚 Topics Covered


- # Day 43 — Matrix Multiplication & Linear Algebra Operations

## Introduction

## Matrix Multiplication

## Dimension Compatibility

## Matrix Multiplication Rule

## NumPy @ Operator

## np.matmul()

## Element-wise vs Matrix Multiplication

## Matrix × Vector

## Vector × Matrix

## Identity Matrix Property

## Matrix Transpose

## Transpose of Product

## Associative Property

## Feature Matrix × Weight Vector

## Employee Prediction Score System

## Hospital Patient Score System

## Practice Programs

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day43 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is matrix multiplication?

Matrix multiplication ($A @ B$) produces a new matrix by taking the dot product of every row in the first matrix with every column in the second matrix.

2. What is the rule for matrix multiplication?

The number of columns in the first matrix must equal the number of rows in the second matrix. For $(m \times k) \times (k \times n)$, the inner dimension $k$ must match.

3. Can a 2×3 matrix multiply a 2×2 matrix?

No. The inner dimensions do not match ($3 \neq 2$). However, a $(2 \times 2)$ matrix can multiply a $(2 \times 3)$ matrix.

4. What is the result of (2×3) × (3×4)?

A $(2 \times 4)$ matrix. Outer dimensions determine the output shape.

5. Difference between A * B and A @ B?

A * B performs element-wise multiplication (Hadamard product). A @ B performs standard matrix multiplication (dot product).

6. What does np.matmul() do?

It is the NumPy function that executes matrix multiplication under the hood when using the @ operator.

7. What is matrix × vector multiplication?

Multiplying an $(m \times n)$ matrix by an $(n \times 1)$ column vector results in an $(m \times 1)$ vector. It represents transforming a vector using a linear system.

8. What is the identity matrix?

A square matrix with ones on its main diagonal and zeros everywhere else, acting as the scalar "1" for matrix operations.

9. What happens when A @ I is calculated?

The matrix remains completely unchanged ($A @ I = A$).

10. Is matrix multiplication commutative?

No. In general, $A @ B \neq B @ A$. Reversing the order changes the result or makes dimensions incompatible.

11. What does $(AB)^T$ equal?

$B^T A^T$. Transposing a product reverses the order of the matrices.

12. What is the associative property?

$(A @ B) @ C = A @ (B @ C)$. Grouping does not affect the outcome, provided the matrix sequence remains unchanged.

13. Why is matrix multiplication important in ML?

It enables parallel computations over entire datasets simultaneously, turning thousands of individual calculations into high-performance linear algebra hardware operations (GPUs/TPUs).

14. What does a feature matrix represent?

A 2D matrix $X$ where rows represent individual samples (data points) and columns represent features (attributes).

15. Why do ML models use weight vectors?

A weight vector $w$ holds learned parameters representing the relative importance of each feature. Computing $X @ w$ calculates predictions across all samples at once.