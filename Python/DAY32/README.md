# 🚀 AI Engineer Bootcamp - Day 32

## 📅 Date
08-08-2026

## 📚 Topics Covered


- # Day 32 — Matplotlib Fundamentals

## Introduction

## Installation

## Importing Matplotlib

## Line Plot

## Bar Chart

## Horizontal Bar Chart

## Histogram

## Scatter Plot

## Figure

## Titles and Labels

## Legend

## Grid

## Saving Charts

## Pandas + Matplotlib

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run

## 📂 GitHub

Day32 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is Matplotlib?

Matplotlib is the core data visualization library in Python. It is a low-level framework designed for creating static, animated, and interactive visualizations with complete control over every element of a figure.

2. Why is Matplotlib used?

Full Control: It allows fine-grained customization of plot elements (colors, line styles, labels, ticks).Ecosystem Foundation: It serves as the underlying rendering engine for higher-level libraries like Seaborn and Pandas plotting tools.Export Flexibility: It supports exporting high-resolution charts in raster (PNG, JPEG) and vector (PDF, SVG) formats.

3. What is pyplot?

pyplot is a state-based module within Matplotlib (matplotlib.pyplot). It provides a MATLAB-like procedural interface that tracks the current active figure and axes, allowing you to build and format charts using step-by-step commands.

4. Why do we use plt?

plt is the standard community alias used when importing pyplot:Pythonimport matplotlib.pyplot as plt
Using plt keeps code concise, readable, and standard across the Python data science ecosystem.

5. What does plot() do?

plt.plot() creates a line plot by default. It connects a series of $(x, y)$ coordinate pairs with continuous straight lines.

6. Difference between line chart and bar chart?

Line Chart: Best for continuous numeric data to show trends, continuity, and change over time or sequences.Bar Chart: Best for categorical or discrete data to compare individual counts or values across distinct groups.

7. When should you use a histogram?

Use a histogram (plt.hist()) when you want to visualize the frequency distribution of a single continuous variable. It groups data into intervals ("bins") to show skewness, central tendencies, spread, and multi-peak distributions.

8. What is a scatter plot?

A scatter plot (plt.scatter()) displays individual data points on a 2D grid using Cartesian coordinates. It is used to analyze relationships, correlations, or clusters between two continuous variables.

9. What does xlabel() do?

plt.xlabel() sets the label text for the horizontal ($x$-axis) to describe the variable or metric represented.

10. What does ylabel() do?

plt.ylabel() sets the label text for the vertical ($y$-axis) to describe the dependent metric or unit of measurement.

11. What does title() do?

plt.title() adds a main header or descriptive title above the plot area.

12. What is legend()?

plt.legend() displays an explanatory key (box) on the chart that decodes colors, line styles, or markers assigned via the label parameter inside plotting functions.

13. What does grid() do?

plt.grid() overlays grid lines across the background of the plot area, making it easier to trace specific data values visually back to axis ticks.

14. What is figure()?

plt.figure() initializes a new top-level container (canvas) that holds all plot elements, axes, subplots, and titles.

15. What is figsize?

figsize is a tuple parameter—figsize=(width, height)—passed to plt.figure() that sets the dimensions of the output image in inches (e.g., figsize=(10, 6)).

16. What does savefig() do?

plt.savefig('filename.png') saves the currently rendered figure to a file on your computer.Note: Call savefig() before plt.show(), as show() clears the figure buffer.

17. Difference between bar() and barh()?

bar(): Renders vertical bars. Ideal for standard categories with concise labels.barh(): Renders horizontal bars. Ideal when category names are long or when displaying ranked lists to prevent text overlapping.

18. How do you combine Pandas and Matplotlib?

Pandas integrates directly with Matplotlib. Calling .plot() on a DataFrame or Series uses Matplotlib under the hood, allowing you to use Matplotlib functions (plt.title(), plt.grid()) for customization:Pythonimport pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Age': [22, 35, 50], 'Income': [30000, 65000, 90000]})

# Pandas syntax using Matplotlib rendering
df.plot(x='Age', y='Income', kind='scatter')

# Matplotlib formatting
plt.title('Age vs Income')
plt.grid(True)
plt.show()

19. Why is visualization important in Data Analysis?

Faster Comprehension: The human brain processes visual formats much faster than scanning raw numerical tables.Data Auditing: Uncovers data quality issues like unexpected missing segments, anomalies, or entry errors quickly.Communication: Translates technical data results into simple, compelling stories for decision-makers.

20. How can visualization help identify patterns?

Trends: Line plots reveal upward or downward trajectories over time.Correlations: Scatter plots reveal positive, negative, or non-linear relationships between variables.Distributions: Histograms show symmetric, skewed, or bimodal shapes in data spread.Outliers: Scatter plots and box plots highlight extreme data points that deviate significantly from the rest.