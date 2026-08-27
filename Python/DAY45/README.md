# 🚀 AI Engineer Bootcamp - Day 45

## 📅 Date
27-08-2026

## 📚 Topics Covered


- # Day 45 — Eigenvalues & Eigenvectors

## Introduction

## Eigenvalues

## Eigenvectors

## Av = λv

## Matrix Transformation

## Characteristic Equation

## det(A − λI) = 0

## Calculating Eigenvalues

## Calculating Eigenvectors

## NumPy np.linalg.eig()

## Eigenpair Verification

## np.allclose()

## PCA Connection

## AI/ML Applications

## Employee Eigen Analysis System

## Hospital Feature Eigen Analysis

## Practice Programs

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day45 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is an eigenvalue?

An eigenvalue ($\lambda$) is a scalar that represents the factor by which an eigenvector is stretched, compressed, or flipped when multiplied by a square matrix $A$.

2. What is an eigenvector?

An eigenvector ($v$) is a non-zero vector whose direction remains unchanged when a linear transformation represented by a matrix $A$ is applied to it. It only changes in magnitude.

3. What does $Av = \lambda v$ mean?

It states that applying a matrix transformation $A$ to vector $v$ yields the exact same result as simply scaling vector $v$ by scalar $\lambda$.

4. What is the relationship between an eigenvalue and its eigenvector?

They form a paired unit called an eigenpair. The eigenvector defines the invariant directional axis of the transformation, while the eigenvalue quantifies the scaling magnitude along that specific axis.

5. What is the characteristic equation?

It is the polynomial equation $\det(A - \lambda I) = 0$ used to find the eigenvalues of a matrix $A$. Solving for $\lambda$ yields the characteristic roots of the matrix.

6. What does $\det(A - \lambda I) = 0$ represent?

It represents the condition under which the matrix $(A - \lambda I)$ becomes singular (non-invertible), ensuring that non-zero vectors $v$ exist such that $(A - \lambda I)v = 0$.

7. How do you calculate eigenvalues in NumPy?

Using the built-in linear algebra function np.linalg.eig(A) or np.linalg.eigvals(A).

8. What does np.linalg.eig() return?

It returns a tuple of two NumPy arrays: (eigenvalues, eigenvectors).

9. How are eigenvectors stored in NumPy's output?

They are stored as column vectors in a 2D array. The eigenvector corresponding to eigenvalues[i] is located at column index eigenvectors[:, i].

10. How can you verify an eigenpair?

By evaluating both sides of $A v = \lambda v$ independently and checking if the resulting vectors are equal element-wise.

11. What does np.allclose() do?

It checks whether two arrays are element-wise equal within a specified floating-point numerical tolerance (atol and rtol), preventing false negatives caused by computer rounding artifacts.

12. What happens to an eigenvector after matrix transformation?

Its direction remains along the exact same line (or directly opposite if $\lambda < 0$). Only its magnitude scales by $\vert{}\lambda\vert{}$.

13. Why are eigenvalues/eigenvectors important in ML?

They allow models to identify major variance directions, compress high-dimensional feature spaces, compute matrix powers/exponentials efficiently, and evaluate stability in second-order optimization methods (Hessians).

14. What is their connection to PCA?

In Principal Component Analysis (PCA), the eigenvectors of the dataset's covariance matrix represent the principal components (axes of maximum variance), while the corresponding eigenvalues indicate how much variance is explained along each axis.

15. What is the difference between an eigenvalue and an eigenvector?

FeatureEigenvalue (λ)Eigenvector (v)Data TypeScalar (single number)Vector (array of numbers)RoleQuantifies magnitude of scalingDefines direction of invariant axisZero ConstraintCan be zero ($\lambda = 0$)Must be non-zero ($v \neq 0$)