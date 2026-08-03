# 🚀 AI Engineer Bootcamp - Day 27

## 📅 Date
03-08-2026

## 📚 Topics Covered


- # Day 27 — Pandas DataFrame Fundamentals

## Introduction

## What is a DataFrame?

## Series vs DataFrame

## Creating DataFrames

## DataFrame from Dictionary

## DataFrame from List

## DataFrame from List of Dictionaries

## DataFrame Index

## DataFrame Columns

## DataFrame Properties

- shape
- size
- dtypes

## DataFrame Methods

- info()
- head()
- tail()
- describe()

## Column Access

## Multiple Column Access

## Row Access

## iloc

## loc

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run


## 📂 GitHub

Day27 Completed Successfully ✅

## 🧠 Interview Preparation


1. Core Concepts & StructureWhat is a Pandas DataFrame?

A Pandas DataFrame is a 2-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). Think of it like a spreadsheet, a SQL table, or a dictionary of Pandas Series objects. It is the core data structure in the Pandas library.Series vs. DataFrameFeatureSeriesDataFrameDimensions1D (One-dimensional array)2D (Two-dimensional table)StructureA single column with an indexMultiple columns and rows with both row and column labelsAnalogyA single list/column with labelsAn entire Excel spreadsheetData TypesHolds a single data typeCan hold multiple data types across different columnsPythonimport pandas as pd

# Series (1D)
s = pd.Series([25, 30, 35], name="Age")

# DataFrame (2D - made of multiple Series)
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
2. Creating a DataFrameBasic SyntaxPythondf = pd.DataFrame(data, index=row_labels, columns=column_labels)
From a DictionaryDictionaries where values are lists convert naturally into columns:Pythondata = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
From a List of ListsWhen creating from a 2D list, define explicit column names using the columns parameter:Pythondata = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Paris']
]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
From a List of DictionariesWhen using a list of dictionaries, each dictionary represents a row, and keys map to column names:Pythondata = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'London'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Paris'}
]
df = pd.DataFrame(data)
3. IndexingWhat is a DataFrame Index?The index refers to the row labels of a DataFrame. By default, Pandas assigns an integer sequence starting from 0 up to N-1 (RangeIndex(0, N)). The index allows fast row lookups and aligns data across operations.Creating a Custom IndexSet custom row labels using the index parameter or by setting an existing column as the index:Python# Approach 1: Pass custom labels on creation
df = pd.DataFrame(data, index=['Emp_1', 'Emp_2', 'Emp_3'])

# Approach 2: Set an existing column as the index
df = df.set_index('Name')
4. Attributes & Inspection ToolsAssuming df is an initialized DataFrame:Columns (df.columns): Returns an Index object containing all column headers.Pythonprint(df.columns.tolist())  # ['Name', 'Age', 'City']
Shape (df.shape): Returns a tuple representing the dimensions (number_of_rows, number_of_columns).Pythonprint(df.shape)  # (3, 3)
Size (df.size): Returns an integer equal to the total cell count ($\text{rows} \times \text{columns}$).Pythonprint(df.size)  # 9
Data Types (df.dtypes): Returns a Series displaying the data type of each column (int64, float64, object, etc.).Pythonprint(df.dtypes)
Purpose of df.info(): Prints a summary including the DataFrame class, row/column count, non-null counts per column (for spotting missing values), data types, and total memory usage.head() vs. tail():df.head(n) returns the first $n$ rows (default $n=5$).df.tail(n) returns the last $n$ rows (default $n=5$).What df.describe() does: Generates summary statistics for numerical columns, including count, mean, std, min, 25%, 50% (median), 75%, and max.5. Accessing Data (Selecting & Slicing)Single ColumnReturns a 1D Pandas Series:Pythonages = df['Age']
# or df.Age (dot notation works if there are no spaces in the name)
Multiple ColumnsPass a list of column names inside double square brackets to return a subsetted DataFrame:Pythonsubset = df[['Name', 'City']]
Accessing Rows with .iloc vs. .loc.iloc (Integer Position-Based): Used to access rows and columns by numerical index position (0-indexed). Slicing endpoints are excluded.Python# Get first row
row_0 = df.iloc[0]

# Slice first two rows, first two columns
sub_iloc = df.iloc[0:2, 0:2]
.loc (Label-Based): Used to access rows and columns by explicit custom index labels or boolean arrays. Slicing endpoints are included.Python# Get row with label 'Emp_1'
row_emp1 = df.loc['Emp_1']

# Slice rows 'Emp_1' to 'Emp_2' for columns 'Age' and 'City'
sub_loc = df.loc['Emp_1':'Emp_2', ['Age', 'City']]
6. Importance in Data Analysis and AIDataFrames serve as the backbone of modern data science, machine learning, and AI workflows for several key reasons:Tabular Standard: Machine learning algorithms expect input as tabular matrices where rows are samples and columns are features. DataFrames provide this native structure.Data Wrangling: Offers fast, built-in tools for data cleaning, handling missing data (NaN), merging/joining tables, filtering rows, and grouping aggregation (groupby).High Performance: Built on top of NumPy and written in optimized C/Cython, enabling vectorized operations on millions of rows without standard Python for loops.Ecosystem Integration: Integrates seamlessly with visualization packages (matplotlib, seaborn) and machine learning pipelines (scikit-learn, PyTorch, TensorFlow).