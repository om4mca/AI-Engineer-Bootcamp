# 🚀 AI Engineer Bootcamp - Day 33

## 📅 Date
10-08-2026

## 📚 Topics Covered


- # Day 33 — Advanced Matplotlib & Visualization

## Introduction

## Multiple Plots

## subplot()

## subplots()

## Line Customization

## Markers

## Bar Chart Customization

## Axis Limits

## Tick Management

## Annotation

## Histogram Bins

## Scatter Plot

## Pandas + Matplotlib

## Data Insights

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day33 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is subplot()?

plt.subplot() is a Matplotlib function used to add a single subplot to a grid inside a figure using 1-based indexing.Syntax: plt.subplot(nrows, ncols, index)Example: plt.subplot(2, 2, 1) targets the 1st plot in a 2x2 grid.

2. Difference between subplot() and subplots()?

plt.subplot(): Adds plots one at a time. You call it repeatedly before each individual chart.plt.subplots(): Creates the entire figure and grid of subplot axes (ax) all at once.Python# Creates a 2x2 grid in a single call
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y) # Top-left plot

3. What is tight_layout()?

plt.tight_layout() automatically adjusts subplot parameters, padding, and margins so that titles, axis labels, and tick marks do not overlap or get cut off.

4. How do you change line style?

Use the linestyle (or ls) parameter inside plt.plot():Pythonplt.plot(x, y, linestyle='--') # Options: '-', '--', ':', '-.'

5. What is a marker?

A marker is a symbol used to highlight individual data points on a line chart or scatter plot.Pythonplt.plot(x, y, marker='o') # Options: 'o' (circle), 's' (square), '^' (triangle), '*' (star)

6. How do you rotate X-axis labels?

You can rotate labels using plt.xticks() or by calling .tick_params() on an axis object:Pythonplt.xticks(rotation=45)
# OR using Object-Oriented Matplotlib:
ax.tick_params(axis='x', rotation=45)

7. What does xlim() do?

plt.xlim(min, max) sets or returns the minimum and maximum boundaries of the X-axis view.Pythonplt.xlim(0, 100) # Forces X-axis to display only between 0 and 100

8. What does ylim() do?

plt.ylim(min, max) sets or returns the minimum and maximum boundaries of the Y-axis view.Pythonplt.ylim(0, 500) # Useful for giving breathing room so labels above top bars aren't cut off

9. What are ticks?

Ticks are the small mark indicators and numerical/text labels placed along the X and Y axes that designate specific measurement intervals or categorical boundaries.

10. What does annotate() do?

plt.annotate() allows you to place custom text labels at a specific coordinate $(x, y)$, often with an arrow pointing directly to an important data point.Pythonplt.annotate('Peak Sales', xy=(5, 100), xytext=(6, 120),
             arrowprops=dict(facecolor='black'))

11. What are histogram bins?

Bins are the discrete intervals (or numerical buckets) into which raw continuous data is divided to count frequency in a histogram. You can pass a number of bins (bins=10) or explicit boundaries (bins=[0, 18, 35, 60]).

12. Difference between bar() and barh()?

plt.bar(): Renders vertical bar charts (X-axis contains categories, Y-axis represents values).plt.barh(): Renders horizontal bar charts (Y-axis contains categories, X-axis represents values). Best used when category names are long.

13. How do you create multiple plots?

You can create multiple plots either by using grid subplots:Pythonfig, axes = plt.subplots(1, 2)
axes[0].plot(x1, y1)
axes[1].bar(x2, y2)
Or by plotting multiple lines/elements on the same axes before calling plt.show():Pythonplt.plot(x, y1, label='Series 1')
plt.plot(x, y2, label='Series 2')
plt.legend()

14. How do you combine Pandas with Matplotlib?

Pandas DataFrames have a built-in .plot() wrapper method that uses Matplotlib under the hood. You can pass a Matplotlib subplot axis (ax) into Pandas methods or apply Matplotlib formatting directly to Pandas plots:Python# Create chart directly from DataFrame
df.plot(kind='bar', x='Department', y='Salary', ax=ax)

# Customize using standard Matplotlib functions
plt.title("Department Salaries")
plt.grid(True)
📊 Analytics, Insights & Business Concepts

15. Why is data visualization important?

Data visualization translates complex numerical datasets into visual charts and patterns. It allows stakeholders to instantly identify trends, correlations, anomalies, and operational bottlenecks that would be difficult to spot in raw tabular data.

16. What is a data insight?

A data insight is an actionable conclusions or strategic takeaways extracted from data analysis—going beyond simply stating numbers to explaining what the finding means for the business.Example: "Sales increased by 20%" is a statistic; "Engineering and Sales account for 58% of overall headcount, indicating operational focus is heavily weighted toward product build and expansion" is an insight.

17. How can visualization help identify outliers?

Visualization highlights data points that deviate significantly from expected patterns:Scatter Plots: Outliers appear as isolated dots far away from main clusters or regression trendlines.Box Plots: Outliers are displayed as individual points beyond the upper and lower whiskers ($1.5 \times \text{IQR}$).Histograms: Outliers show up as isolated bars separated by empty bins from the main distribution curve.

18. How can charts support business decisions?

Charts convert quantitative facts into strategic direction:Resource Allocation: Identifying understaffed or overburdened departments (e.g., patient volume bar charts).Pricing & Revenue: Understanding price elasticity or service costs (e.g., hospital bill distribution).Performance Tracking: Pinpointing underperforming units vs. high-value teams (e.g., performance score box plots).

19. Which chart is suitable for categorical comparison?

A Bar Chart (plt.bar() or plt.barh()) is best suited for comparing discrete categories (e.g., patient counts across departments, revenue by product region).

20. Which chart is suitable for relationship between two numerical variables?

A Scatter Plot (plt.scatter()) is the gold standard for displaying relationships, correlations, and distributions between two continuous numerical variables (e.g., Age vs. Salary, Experience vs. Pay, Stay Days vs. Hospital Bill).