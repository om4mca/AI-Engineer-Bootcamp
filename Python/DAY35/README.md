# 🚀 AI Engineer Bootcamp - Day 35

## 📅 Date
12-08-2026

## 📚 Topics Covered


- # Day 35 — Statistics Fundamentals

## Introduction

## Population and Sample

## Mean

## Median

## Mode

## Range

## Variance

## Standard Deviation

## Percentiles

## Quartiles

## IQR

## Outliers

## Pandas Statistical Analysis

## Employee Salary Statistical Analysis

## Hospital Patient Age & Bill Statistics

## Practice Programs

## Key Insights

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day35 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is Statistics?

Statistics is the branch of mathematics focused on collecting, organizing, analyzing, interpreting, and presenting data to uncover patterns and make decisions under uncertainty.

2. What is Population?

A Population ($N$) is the complete set of all individuals, objects, or measurements of interest in a study (e.g., all 8 billion people on Earth or every smartphone produced by a factory in a year).

3. What is Sample?

A Sample ($n$) is a representative subset drawn from a population, used to collect data and make inferences about the larger group without having to test every single unit.

4. Difference between Population and Sample?

FeaturePopulationSampleScopeThe entire group of interestA smaller subset of the populationSymbol for Size$N$$n$Calculated ValuesParameters ($\mu$ for mean, $\sigma$ for std dev)Statistics ($\bar{x}$ for mean, $s$ for std dev)Real-world ExampleAll voters in a country1,000 voters polled in an election exit poll2. Central Tendency

5. What is Mean?

The Mean (arithmetic average) is the sum of all observations divided by the total number of observations.$$\bar{x} = \frac{\sum x_i}{n}$$

6. What is Median?

The Median is the physical midpoint of an ordered dataset, separating the top 50% from the bottom 50%.If $n$ is odd, it is the single middle value.If $n$ is even, it is the average of the two middle values.

7. What is Mode?

The Mode is the value that appears most frequently in a dataset. A dataset can have no mode, one mode (unimodal), or multiple modes (bimodal / multimodal).

8. Difference between Mean and Median?

AspectMeanMedianBasisMathematical average using all data valuesPositional middle of sorted valuesOutlier ImpactHeavily distorted by extreme valuesHighly robust against extreme valuesBest Used ForSymmetric distributions without outliersSkewed distributions (e.g., Income, House prices)3. Dispersion & Variability

9. What is an Outlier?

An Outlier is a data point that deviates significantly from the overall pattern of a dataset, resulting from measurement errors, experimental anomalies, or natural extremes.

10. What is Range?

The Range is the simplest measure of spread, calculated as the difference between the maximum and minimum values:$$\text{Range} = \text{Max} - \text{Min}$$

11. What is Variance?

Variance measures the average squared distance of individual data points from their mean:$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1}$$

12. What is Standard Deviation?

Standard Deviation ($s$) is the square root of the variance ($s = \sqrt{s^2}$). It quantifies average dispersion in the same units as the original data.

13. Difference between Variance and Standard Deviation?

Variance is expressed in squared units (e.g., $\text{USD}^2$), making it difficult to interpret directly alongside the mean.Standard Deviation is in original units (e.g., $\text{USD}$), making it intuitive for understanding data spread around the center.4. Relative Position & Quartiles

14. What is Percentile?

A Percentile indicates the relative position of a value, specifying the percentage of data points that fall at or below it (e.g., scoring in the 90th percentile means you performed better than or equal to 90% of test takers).

15. What are Quartiles?

Quartiles are three specific percentiles that slice an ordered dataset into four equal parts:$Q1$ (1st Quartile / 25th Percentile): Median of the lower half of data.$Q2$ (2nd Quartile / 50th Percentile): The overall Median.$Q3$ (3rd Quartile / 75th Percentile): Median of the upper half of data.

16. What is IQR?

IQR (Interquartile Range) measures the spread of the middle 50% of data, ignoring the top 25% and bottom 25%:$$\text{IQR} = Q3 - Q1$$

17. How can IQR help identify outliers?

IQR uses Tukey’s Fences to calculate strict upper and lower limits:$$\text{Lower Boundary} = Q1 - 1.5 \times \text{IQR}$$$$\text{Upper Boundary} = Q3 + 1.5 \times \text{IQR}$$Any data point smaller than the Lower Boundary or larger than the Upper Boundary is mathematically flagged as a possible outlier.5. Applied & Analytical Questions

18. Why can outliers affect the Mean?

Because the formula for the Mean sums every single value ($\sum x_i$), a single extreme number (e.g., adding an executive earning $\$10,000,000$ to a group earning $\$50,000$) massively inflates the sum, pulling the average far away from the true center.

19. When can Median be more useful than Mean?

The Median is preferred whenever data is heavily skewed or contains extreme outliers:Real-world Example: In real estate, if 9 houses sell for $\$300,000$ and 1 mansion sells for $\$20,000,000$, the Mean price is $\$2,270,000$ (misleading), while the Median price remains $\$300,000$ (accurately reflects the market).

20. Why is Statistics important in Machine Learning?

Statistics serves as the core foundation for Machine Learning across three main areas:Exploratory Data Analysis (EDA): Detecting missing values, assessing distribution skewness, and spotting outliers before model training.Feature Engineering & Selection: Using correlation metrics (e.g., Pearson, Chi-Square, ANOVA) to filter out redundant inputs and keep predictive features.Model Validation: Applying probability distributions and hypothesis testing (e.g., A/B testing, p-values) to confirm that model predictions represent genuine patterns rather than random noise.