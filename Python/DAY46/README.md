# 🚀 AI Engineer Bootcamp - Day 46

## 📅 Date
28-08-2026

## 📚 Topics Covered


- # Day 46 — Vector Spaces, Linear Independence & Basis

## Introduction

## Vector Space

## Subspace

## Linear Combination

## Span

## Linear Independence

## Linear Dependence

## Basis

## Dimension

## Column Space

## Row Space

## Matrix Rank

## np.linalg.matrix_rank()

## Full Rank

## Rank and Determinant

## Machine Learning Applications

## PCA Connection

## Employee Feature Rank Analyzer

## Hospital Feature Rank Analyzer

## Practice Programs

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day46 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is a vector space?

A formal set of vectors closed under vector addition and scalar multiplication that satisfies eight algebraic axioms (such as associativity, commutativity, and the existence of additive identity and inverse elements).

2. What is a linear combination?

An expression formed by multiplying a set of vectors by scalar coefficients and adding the results together:$$w = c_1 v_1 + c_2 v_2 + \dots + c_n v_n$$

3. What is the span of vectors?

The set of all possible linear combinations that can be generated from a given set of vectors. Geometrically, it forms a point, line, plane, or higher-dimensional subspace.

4. What does linear independence mean?

A set of vectors is linearly independent if no vector in the set can be written as a linear combination of the others. The only solution to $c_1 v_1 + c_2 v_2 + \dots + c_n v_n = 0$ is $c_1 = c_2 = \dots = c_n = 0$.

5. What does linear dependence mean?

A set of vectors is linearly dependent if at least one vector can be expressed as a linear combination of the remaining vectors, meaning redundant directions exist in the set.Space & Dimension Foundations

6. What is a basis?

A minimal set of linearly independent vectors that spans an entire vector space. Every vector in that space can be uniquely represented as a linear combination of the basis vectors.

7. What is the dimension of a vector space?

The total number of vectors in any basis for that vector space, representing its fundamental degrees of freedom.

8. What is column space?

The subspace spanned by the column vectors of a matrix $A$, denoted as $\text{Col}(A)$. It represents all possible output vectors $b$ for which the system $Ax = b$ has a solution.

9. What is row space?

The subspace spanned by the row vectors of a matrix $A$, denoted as $\text{Row}(A)$. Its dimension is always equal to the dimension of the column space.Matrix Rank & Computation

10. What is matrix rank?

The maximum number of linearly independent column (or row) vectors in a matrix, quantifying the dimension of its column space.

11. How is rank related to linear independence?

Rank measures linear independence directly: if a matrix with $n$ columns has $\text{Rank} = k$, then exactly $k$ columns are linearly independent, and $n - k$ columns are redundant.

12. What does np.linalg.matrix_rank() do?

It computes the numerical rank of a 2D array by running a Singular Value Decomposition (SVD) and counting the number of singular values greater than a small numerical tolerance threshold.

13. What is a full-rank matrix?

A matrix whose rank equals the maximum possible given its dimensions: $\text{Rank}(A) = \min(m, n)$. A square full-rank matrix is non-singular and invertible.

14. What is the relationship between rank and determinant for a square matrix?

Full Rank ($\text{Rank} = n$): $\det(A) \neq 0$ (invertible, non-singular).Rank Deficient ($\text{Rank} < n$): $\det(A) = 0$ (singular, non-invertible, compresses space to a lower dimension).Machine Learning Context

15. Why is rank important in Machine Learning?

Detecting Multicollinearity: Rank deficiency indicates duplicate or linearly dependent attributes in a feature matrix $X$, causing $X^T X$ to be non-invertible in Ordinary Least Squares (OLS) regression.Dimensionality Reduction: Algorithms like PCA and SVD rely on matrix rank to determine the true intrinsic dimensionality of high-dimensional datasets and discard redundant features without losing information.