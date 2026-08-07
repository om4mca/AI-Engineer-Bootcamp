# 🚀 AI Engineer Bootcamp - Day 31

## 📅 Date
07-08-2026

## 📚 Topics Covered


- # Day 31 — Data Import & Export

## Introduction

## CSV Files

## Excel Files

## read_csv()

## to_csv()

## read_excel()

## to_excel()

## head()

## tail()

## info()

## describe()

## usecols

## skiprows

## nrows

## File Existence Check

## Practice Programs

## Mini Project

## Bonus Project

## Interview Questions

## Key Learnings

## How to Run

## 📂 GitHub

Day31 Completed Successfully ✅

## 🧠 Interview Preparation


1. What is CSV?

CSV stands for Comma-Separated Values. It is a plain text file format used to store tabular data (numbers and text). Each line in the file corresponds to a data record, and each field within that line is separated by a comma.Why is CSV widely used?Universal Compatibility: Supported by virtually every programming language, database, and spreadsheet software.Lightweight: Contains pure text without complex formatting or binary overhead, leading to smaller file sizes.Human-Readable: Can be opened and inspected with simple text editors like Notepad.Fast I/O: Quicker to import and export compared to complex spreadsheet formats.

3. Difference between CSV and Excel?

FeatureCSVExcel (.xlsx)File FormatPlain textZip-compressed XML / BinaryFormatting & StylingNo fonts, colors, or cell formulasSupports rich styles, formulas, and chartsMultiple SheetsSingle table/sheet onlyMultiple worksheets in one workbookFile SizeLightweight & smallLarger due to metadata & formattingProcessing SpeedExtremely fast to parseSlower to read and write

2. Reading & Writing Data in Pandas

4. What does read_csv() do?

It is a Pandas function that reads a CSV file (or URL) and parses its contents into a structured Pandas DataFrame.

5. What does to_csv() do?

It is a DataFrame method that exports the data from a Pandas DataFrame into a CSV file on your local disk.

14. How do you read Excel files?

Using the pd.read_excel() function:Pythondf = pd.read_excel("report.xlsx", sheet_name="Sheet1")

15. Why is openpyxl required?

openpyxl is a Python library that Pandas uses under the hood as an engine to read and write modern Excel files (.xlsx). Without openpyxl installed, Pandas cannot parse or format .xlsx files.

13. What is the purpose of index=False?

When running df.to_csv("file.csv", index=False), it tells Pandas not to write row numbers (0, 1, 2, ...) into the CSV file as an extra, unnamed first column.3. Reader Parameters

9. How do you read only selected columns?

By using the usecols parameter in read_csv().

10. What is usecols?

A parameter in read_csv() that lets you pass a list of column names or index positions to load into memory, skipping unneeded columns.Pythondf = pd.read_csv("data.csv", usecols=["Name", "Salary"])

11. What is skiprows?

A parameter that specifies how many lines (or which specific row indices) to skip at the top of the file before reading the header/data. Useful for skipping metadata headers.Pythondf = pd.read_csv("data.csv", skiprows=2)

12. What is nrows?

A parameter that specifies the maximum number of rows to read from the file. Ideal for inspecting massive datasets quickly without loading the full file.Pythondf = pd.read_csv("large_data.csv", nrows=100)

17. What is sep?

Short for separator (or delimiter). It tells Pandas which character separates values in the file (e.g., , for standard CSV, \t for TSV, or | for pipe-separated files).Pythondf = pd.read_csv("data.tsv", sep="\t")

16. What is encoding?

Specifies the character encoding scheme (such as 'utf-8', 'latin1', or 'cp1252') used to read special characters, symbols, or foreign language texts correctly without encountering an UnicodeDecodeError.4. Inspection & Utilities

6. Difference between head() and tail()?

head(n): Displays the first $n$ rows of a DataFrame (default is 5).tail(n): Displays the last $n$ rows of a DataFrame (default is 5).

7. What information does info() provide?

It provides a high-level concise summary of the DataFrame:Total row count and index range.Total column count.Column names and their respective non-null value counts.Data types (int64, float64, object, etc.) of each column.Total memory footprint used by the DataFrame.

8. What does describe() return?

It returns descriptive statistics for numeric columns in the DataFrame, including:Count (non-null entries)Mean and Standard Deviation (std)Min and MaxPercentiles / Quartiles (25%, 50% / Median, 75%)

18. How do you check if a file exists?

Using Python's standard os or pathlib modules:Pythonimport os

if os.path.exists("data.csv"):
    df = pd.read_csv("data.csv")
5. Industry Context

19. Why is data import important?

Data import is the crucial first step in any data analysis, data science, or engineering pipeline. If data cannot be ingested cleanly and correctly (with proper datatypes and missing value handling), downstream analytics, machine learning models, and business reports will produce flawed results.

20. Where are CSV files used in industry?

Database Backups & Migration: Exporting records from SQL/NoSQL databases for transfers between platforms.Financial Reporting: Ingesting transaction logs, bank statements, and stock price histories.E-Commerce & Retail: Managing product catalogs, bulk inventory updates, and order exports.Healthcare & Patient Records: Transporting anonymized patient, billing, and lab result logs between systems.Machine Learning & AI: Feeding structured datasets into model training pipelines (e.g., Scikit-Learn, PyTorch, TensorFlow).