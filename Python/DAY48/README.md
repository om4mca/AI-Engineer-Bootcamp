# 🚀 AI Engineer Bootcamp - Day 48

## 📅 Date
31-08-2026

## 📚 Topics Covered


- # Day 48 — Least Squares & Linear Regression Mathematics

## Introduction

## Exact vs Approximate Solutions

## Overdetermined Systems

## Residuals

## Squared Errors

## RSS

## Least Squares

## Linear Regression

## Matrix Representation

## Design Matrix

## Normal Equation

## np.linalg.lstsq()

## Predictions

## MSE

## Rank

## Machine Learning Applications

## Employee Salary Least-Squares Analyzer

## Hospital Data Least-Squares Analyzer

## Practice Programs

## Interview Questions

## Key Learnings

## How to Run

## 📂 GitHub

Day48 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is an overdetermined system?

An overdetermined system is a system of linear equations with more equations than unknowns ($m > n$). In real-world data analysis, this occurs when there are more observations than features, making an exact solution impossible due to noise.

2. What is the difference between an exact and approximate solution?

Exact Solution: A parameter vector $\vec{x}$ that satisfies $A\vec{x} = \vec{b}$ perfectly with zero error, meaning $\vec{b}$ lies within the column space of $A$.Approximate Solution: A vector $\hat{x}$ that minimizes the distance $\Vert{}A\hat{x} - \vec{b}\Vert{}$ when $\vec{b}$ lies outside the column space of $A$.

3. What is Least Squares?

Least Squares is an optimization method used to estimate parameters in an overdetermined system by minimizing the sum of squared differences between observed values and predicted values.

4. What is a residual?

A residual $e_i$ is the vertical difference between an actual target value $y_i$ and the model's predicted value $\hat{y}_i$:$$e_i = y_i - \hat{y}_i$$

5. Why are residuals squared?

Eliminates Sign Cancellation: Squaring prevents positive and negative errors from canceling each other out.Penalizes Outliers: Squaring gives disproportionately higher weight to larger deviations.Calculus Optimization: Creates a smooth, convex quadratic loss surface ($\sum e_i^2$) with a single global minimum, making derivative-based optimization straightforward.

6. What is RSS?

Residual Sum of Squares (RSS) is the total aggregated squared error across all $m$ data samples:$$\text{RSS} = \sum_{i=1}^{m} (y_i - \hat{y}_i)^2 = \Vert{}\vec{y} - X\hat{w}\Vert{}^2$$

7. What is MSE?

Mean Squared Error (MSE) is the average of the squared residuals, scaling RSS by the sample size $m$:$$\text{MSE} = \frac{1}{m} \text{RSS} = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2$$

8. What is linear regression?

Linear regression is a predictive modeling algorithm that fits a linear function to establish a relationship between one or more continuous feature variables ($X$) and a continuous target variable ($y$).

9. How can linear regression be represented using matrices?

Linear regression is expressed in matrix form as $X\vec{w} \approx \vec{y}$:$$\begin{bmatrix} 1 & x_{11} & \dots & x_{1n} \\ 1 & x_{21} & \dots & x_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{m1} & \dots & x_{mn} \end{bmatrix} \begin{bmatrix} w_0 \\ w_1 \\ \vdots \\ w_n \end{bmatrix} \approx \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_m \end{bmatrix}$$

10. What is a design matrix?

A Design Matrix ($X$) is an $m \times (n+1)$ matrix where each row represents an individual sample and each column represents a feature. The first column is populated entirely with ones ($1$s) to accommodate the intercept/bias term ($w_0$).

11. What does np.linalg.lstsq() do?

np.linalg.lstsq() solves an overdetermined linear system $X\vec{w} \approx \vec{y}$ by finding the weight vector $\hat{w}$ that minimizes $\Vert{}\vec{y} - X\vec{w}\Vert{}^2$. It returns the optimal weights, total RSS, matrix rank, and singular values.

12. Why is np.linalg.lstsq() useful for overdetermined systems?

Handles Rank Deficiency: Uses Singular Value Decomposition (SVD) to compute pseudoinverses, avoiding crashes caused by collinear features (where $(X^T X)^{-1}$ fails).Guaranteed Output: Always returns a stable, minimum-norm solution regardless of matrix shape or singularity.

13. What is the normal equation?

The Normal Equation is the explicit closed-form analytical formula derived by setting the gradient of the RSS loss function to zero:$$\hat{w} = (X^T X)^{-1} X^T \vec{y}$$

14. How is Least Squares connected to Machine Learning?

Loss Function Paradigm: Serves as the foundational loss function ($\mathcal{L}(\vec{w}) = \text{MSE}$) for supervised learning regression algorithms.Regularization Base: Forms the baseline objective function extended by Ridge (L2 penalty) and Lasso (L1 penalty) models.Optimization Benchmark: Provides an exact closed-form benchmark to evaluate iterative solvers like Gradient Descent.

15. Why is Linear Algebra important for regression?

Vectorized Computation: Enables fast, parallelized operations ($X\vec{w}$) instead of slow iterative loops.Closed-Form Solutions: Enables computing model parameters analytically using matrix calculus.Geometric Framing: Models fitting as an orthogonal projection of the target vector $\vec{y}$ onto the column space spanned by the feature matrix $X$.