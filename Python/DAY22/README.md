# 🚀 AI Engineer Bootcamp - Day 22

## 📅 Date
28-07-2026

## 📚 Topics Covered


- Python for Data Processing ✅
- Structured Data ✅
- Unstructured Data ✅
- Data Cleaning ✅
- Data Transformation ✅
- Data Analysis ✅
- Data Pipeline ✅
- NumPy Introduction ✅
- Pandas Introduction ✅
- NumPy vs Pandas ✅
 - 15 Practice Programs — Completed ✅
- Hospital Data Analysis — Completed ✅
- Employee Data Analysis System — Completed ✅
- Notebook — Completed ✅
- Interview Questions — Completed ✅
- Interview Questions






## 📂 GitHub

Day22 Completed Successfully ✅

## 🧠 Interview Preparation


1. Why is Python popular in AI and Data Science?

Simple Syntax: Python reads like plain English, allowing developers to focus on solving complex algorithms rather than struggling with complex code structures.Rich Library Ecosystem: It offers specialized, mature libraries for every stage of the pipeline: NumPy and Pandas (Data Handling), Scikit-Learn (Machine Learning), PyTorch and TensorFlow (Deep Learning), and LangChain/Hugging Face (Generative AI).High Performance via C-Extensions: Key Python libraries use underlying C and C++ code for fast mathematical computations while keeping a user-friendly Python interface.Strong Community Support: A massive global community means constant updates, extensive documentation, and easy troubleshooting.

2. What is structured data?

Structured data is highly organized data that follows a strict, predefined model and easily fits into tabular formats (rows and columns).Examples: SQL database tables, CSV files, and Excel spreadsheets.Common Uses: Financial records, sales transactions, patient records.

3. What is unstructured data?

Unstructured data lacks a predefined structure or data model, making it qualitative and harder to search or process directly without AI.Examples: PDF documents, text messages, images, video recordings, audio files, and social media posts.Common Uses: Computer Vision, Natural Language Processing (NLP), and Large Language Models (LLMs).

4. What is data cleaning?

Data cleaning (or data wrangling) is the process of identifying and correcting errors, missing values, duplicates, and inconsistencies within a dataset to ensure high data quality before analysis or model training.

5. What is data transformation?

Data transformation involves converting data from its raw structure or format into a standardized format required by machine learning models or downstream applications.Common Techniques: Scaling/Normalization (bringing numbers into a 0–1 range), Encoding (converting text labels into numbers), and Type Conversion.

6. What is data analysis?

Data analysis is the systematic process of inspecting, cleaning, transforming, and modeling data to uncover patterns, extract meaningful insights, and support data-driven decision-making.

7. What is the difference between NumPy and Pandas?

FeatureNumPyPandasPrimary FocusHigh-performance numerical and linear algebra operations.Tabular data manipulation and analysis.Core Structurendarray (N-Dimensional Array).DataFrame (2D Table) and Series (1D Column).Data TypesHomogeneous (all elements must be the exact same data type).Heterogeneous (different columns can hold strings, numbers, dates, etc.).IndexingNumerical indexing ($0, 1, 2, \dots$).Labeled indexing (column names and custom row indexes).

8. What is a NumPy array?

A NumPy array (ndarray) is a grid of values, all of the same type, indexed by a tuple of non-negative integers. Unlike standard Python lists, NumPy arrays store data in contiguous memory blocks, making mathematical operations significantly faster.

9. What is a Pandas DataFrame?

A Pandas DataFrame is a 2-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). You can think of it as a programmable Excel spreadsheet or a SQL table inside Python.

10. Why are Python Lists not always ideal for numerical computing?

Slower Execution: Python lists store pointers to objects scattered across memory, requiring dynamic type checking for every element during operations.No Built-In Vectorization: You cannot directly perform mathematical operations on an entire list (e.g., list * 2 duplicates the list instead of multiplying its values).High Memory Overhead: Each element in a standard Python list is a full-fledged Python object, consuming significantly more memory than a raw C array.

11. What is vectorization?

Vectorization is the process of performing element-wise mathematical operations on an entire array or dataset all at once without writing explicit for loops in Python. NumPy executes vectorized operations internally in compiled C code, achieving massive speed improvements.Pythonimport numpy as np

# Vectorized operation (No loops needed)
arr = np.array([1, 2, 3, 4])
result = arr * 2  # [2, 4, 6, 8]
12. What is a data pipeline?A data pipeline is an automated workflow that extracts raw data from multiple sources, processes and transforms it (ETL: Extract, Transform, Load), and delivers it to a target destination (such as a database, dashboard, or machine learning model).
13. What are missing values?

Missing values occur when no data value is stored for a specific variable or feature in an observation. In Python, these are typically represented as None or NaN (Not a Number). They must be handled by dropping them or imputing them (filling them using mean, median, or predictive models).

14. What are duplicate records?
Duplicate records are identical or nearly identical rows in a dataset that represent the same entity or transaction multiple times. Failing to remove duplicates can unfairly bias Machine Learning models and skew statistical results.

15. What is the role of data preprocessing in Machine Learning?

Data preprocessing bridges the gap between raw data and machine learning algorithms. Its core roles are:Ensuring Model Quality: Garbage in, garbage out—models trained on dirty data produce inaccurate predictions.Algorithm Compatibility: Algorithms require purely numeric inputs, scaled values, and fixed formats to compute mathematical formulas efficiently.Preventing Overfitting & Bias: Proper scaling and cleaning help models generalize better to new, unseen data.