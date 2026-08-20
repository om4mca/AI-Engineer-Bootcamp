# 🚀 AI Engineer Bootcamp - Day 39

## 📅 Date
20-08-2026

## 📚 Topics Covered


- # Day 39 — Normal Distribution & Z-Score

## Introduction

## Normal Distribution

## Bell Curve

## Mean, Median & Mode

## Standard Deviation

## Empirical Rule

## 68–95–99.7 Rule

## Standard Normal Distribution

## Z-Score

## Standardization

## NumPy Implementation

## SciPy Implementation

## Visualization

## Employee Salary Analysis

## Hospital Patient Age Analysis

## Practice Programs

## Key Insights

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day39 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is Normal Distribution?

A continuous probability distribution that is symmetric about its mean, showing that data near the mean are more frequent in occurrence than data far from the mean.

2. Why is it called a bell curve?

Because the graphical plot of its probability density function (PDF) forms a smooth, symmetric, bell-shaped curve that slopes downward symmetrically on both sides from the center.

3. What are the characteristics of a normal distribution?

Symmetry: Unimodal and perfectly symmetric around the center.Equality of Averages: Mean, Median, and Mode are equal and located at the exact center.Asymptotic Tails: The curve approaches the horizontal axis on both sides but never touches it.Empirical Rule: Entire shape is completely parameterized by just two values: mean ($\mu$) and standard deviation ($\sigma$).

4. In a perfectly normal distribution, what is the relationship between mean, median and mode?

They are all equal to each other: $\text{Mean} = \text{Median} = \text{Mode}$.

5. What is Standard Deviation?

A measure of the amount of variation or dispersion in a set of values relative to its mean. It quantifies how spread out the numbers are.Z-Scores & Empirical Rule

6. What is the 68–95–99.7 rule?

Also known as the Empirical Rule, it states that for a normal distribution:$\approx 68.27\%$ of the data falls within $\pm 1\sigma$ of the mean.$\approx 95.45\%$ of the data falls within $\pm 2\sigma$ of the mean.$\approx 99.73\%$ of the data falls within $\pm 3\sigma$ of the mean.

7. What is Standard Normal Distribution?

A specific case of the normal distribution where the mean ($\mu$) is $0$ and the standard deviation ($\sigma$) is $1$, written as $N(0, 1)$.

8. What is a Z-score?

A dimensionless metric that measures how many standard deviations a given raw data point ($x$) is above or below the mean ($\mu$). Formula: $z = \frac{x - \mu}{\sigma}$.

9. What does a positive Z-score mean?

The observation is above (greater than) the mean.

10. What does a negative Z-score mean?

The observation is below (less than) the mean.

11. What does Z = 0 mean?

The observation is exact equal to the mean.Standardization & Machine Learning

12. Why is standardization useful?

It rescales data with different units or scales to a common standard scale ($N(0,1)$), making comparisons direct and enabling machine learning algorithms to perform optimally.

13. How can NumPy generate normally distributed data?

Using np.random.normal(loc=mean, scale=std_dev, size=sample_size).

14. How can SciPy calculate normal distribution probabilities?

Using scipy.stats.norm(loc=mean, scale=std_dev):Point Probability Density (PDF): stats.norm.pdf(x, loc, scale)Cumulative Probability (CDF): stats.norm.cdf(x, loc, scale)Quantile / Inverse CDF: stats.norm.ppf(q, loc, scale)

15. What happens to the mean after Z-score standardization?

The mean always becomes $0$.

16. What happens to the standard deviation after standardization?

The standard deviation always becomes $1$.

17. Can every real-world dataset be assumed to be normally distributed?

No. Many real-world variables are skewed (e.g., income, house prices) or follow non-normal distributions like Poisson, Exponential, or Power-Law. Assuming normality without testing can bias conclusions.

18. What is the difference between PDF and CDF?

PDF (Probability Density Function): Shows the relative likelihood/density of a continuous variable at a specific point value $x$.CDF (Cumulative Distribution Function): Shows the cumulative probability that a random variable $X$ takes on a value less than or equal to $x$ ($P(X \le x)$).

19. How can Z-score help identify unusual observations?

By setting a threshold (typically $\vert{}Z\vert{} > 2$ or $\vert{}Z\vert{} > 3$), observations that lie beyond $2$ or $3$ standard deviations from the mean can be identified as statistical outliers.

20. Why is feature scaling important in Machine Learning?

Distance-based algorithms (like KNN, K-Means, SVM) and gradient descent optimization algorithms perform poorly or converge slowly when features have vastly different scales (e.g., age vs. annual income). Scaling ensures all features contribute equally.Python Implementation Syntax

