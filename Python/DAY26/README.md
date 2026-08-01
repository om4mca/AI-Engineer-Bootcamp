# 🚀 AI Engineer Bootcamp - Day 26

## 📅 Date
01-08-2026

## 📚 Topics Covered


- #  Day 26 — Pandas Introduction & Series Fundamentals

## Introduction

## What is Pandas?

## Why Pandas?

## NumPy vs Pandas

## Pandas Installation

## Importing Pandas

## Pandas Series

## Creating Series

## Series Index

## Custom Index

## iloc

## loc

## Series Slicing

## Series Filtering

## Series Operations

## Series Methods

## Series Properties

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day25 Completed Successfully ✅

## 🧠 Interview Preparation


1. Core Concepts & Fundamentals What is Pandas?

Pandas is an open-source Python library designed for data manipulation, cleaning, and analysis. Built on top of NumPy, it introduces high-level data structures like Series (1D) and DataFrames (2D) that make working with tabular, relational, and time-series data intuitive and efficient.

2. Why is Pandas used in Data Analysis?

Handles Tabular Data: Naturally mirrors spreadsheets and SQL databases.Data Cleaning: Simplifies handling missing values (NaN), duplicates, and inconsistent data types.Flexible Wrangling: Offers built-in tools for filtering, grouping (groupby), merging, joining, and pivoting datasets.I/O Integration: Reads and writes seamlessly across file formats including CSV, Excel, SQL databases, JSON, and Parquet.

3. Difference between NumPy and Pandas?

FeatureNumPyPandasPrimary Structurendarray (n-dimensional array)Series (1D) and DataFrame (2D)Data TypesHomogeneous (all elements must be the same data type)Heterogeneous (columns can store different data types)IndexingDefault integer-position indexing (0, 1, 2...)Explicit, customizable row/column labelsBest Used ForFast vector operations, matrix algebra, scientific computingData manipulation, exploratory data analysis, and data cleaningData Structures & Creation

4. What is a Pandas Series?

A Series is a one-dimensional labeled array capable of holding any data type (integers, floats, strings, objects). It consists of two linked components: an array of values and a corresponding array of index labels.

5. What is the difference between Series and DataFrame?

PropertyPandas SeriesPandas DataFrameDimensions1D (Single column)2D (Tabular grid with rows and columns)StructureContains values and a single indexContains values, a row index, and column headersAnalogyA single column in an Excel sheetAn entire Excel spreadsheet or SQL table

6. How do you create a Series?

You can create a Series using pd.Series() from lists, NumPy arrays, or dictionaries:Pythonimport pandas as pd
import numpy as np

# From a list
s_list = pd.Series([10, 20, 30])

# From a NumPy array
s_arr = pd.Series(np.array([1.5, 2.5, 3.5]))

# From a dictionary (keys automatically become the index)
s_dict = pd.Series({'a': 100, 'b': 200})

7. What is an index in Pandas?

An index is an explicit sequence of labels assigned to data rows (and columns in DataFrames). It acts as an address system for data alignment, allowing fast lookup, indexing, slicing, and automatic data alignment during binary operations.

8. How do you create a Series with custom indexes?

Pass a list of labels to the index parameter in pd.Series():Pythonmarks = pd.Series([85, 90, 78], index=['Math', 'Science', 'English'])
Indexing, Access, & Operations

9. Difference between loc and iloc?

loc (Label-Based): Selects data using explicit custom index labels. Slicing with loc includes the stop label.iloc (Integer-Position Based): Selects data using zero-based integer positions ($0$ to $N-1$). Slicing with iloc excludes the stop position.Pythons = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

print(s.loc['b'])    # Returns 20 (Using label)
print(s.iloc[1])    # Returns 20 (Using zero-based position)

print(s.loc['a':'c']) # Includes 'c' -> ['a', 'b', 'c']
print(s.iloc[0:2])    # Excludes index 2 -> positions 0, 1

10. How do you access a Series value?

You can access values by label, integer position, or directly using bracket notation:Pythons = pd.Series([100, 200, 300], index=['x', 'y', 'z'])

val1 = s['x']       # Direct label lookup -> 100
val2 = s.loc['y']   # Explicit label lookup -> 200
val3 = s.iloc[2]    # Position-based lookup -> 300

11. How do you slice a Series?

Using label ranges (.loc) or positional ranges (.iloc or bracket notation):Pythons = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

pos_slice = s.iloc[1:4]     # Positions 1, 2, 3 -> b, c, d
label_slice = s.loc['b':'d'] # Labels 'b', 'c', 'd'

12. How do you filter a Series?

Pass a boolean conditional statement inside brackets (boolean indexing):Pythonscores = pd.Series([45, 88, 92, 60, 73])

# Filter scores above 70
high_scores = scores[scores > 70]

13. How do you calculate the mean of a Series?

Use the .mean() method:Pythons = pd.Series([10, 20, 30, 40])
avg = s.mean()  # Returns 25.0

14. How do you find unique values?

Use s.unique() for an array of distinct values, or s.value_counts() to include their frequencies:Pythons = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'])

distinct_values = s.unique()        # Returns array(['A', 'B', 'C'])
value_counts = s.value_counts()    # Returns frequency count of each value
Key PropertiesPythons = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

15. Series.values:

 Returns the underlying data as a NumPy ndarray (array([10, 20, 30])).
 
 16. Series.index: 
 
 Returns the index object containing row labels (Index(['a', 'b', 'c'], dtype='object')).
 
 17. Series.dtype: 
 
 Returns the data type of the underlying values (dtype('int64')).
 
 18. Series.shape: 
 
 Returns a tuple indicating dimensions ((3,)).
 
 19. Series.size:
 
  Returns the total number of elements as an integer (3).Importance in Machine Learning
  
  20. Why is Pandas important for AI and Machine Learning?
  
  Feature Engineering & Preprocessing: AI/ML models require clean numerical matrices. Pandas simplifies encoding categorical variables (one-hot encoding), scaling, and transforming features.Handling Missing Data: Real-world ML datasets contain missing values. Pandas provides efficient methods like .fillna() and .dropna() to address them.Data Splitting & Selection: Makes isolating target labels ($y$) from input features ($X$) straightforward using label and column selection.Model Evaluation Integration: Converts effortlessly between structured datasets, NumPy arrays, PyTorch Tensors, and Scikit-Learn pipelines