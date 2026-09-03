import pandas as pd

# 1. Dataset Creation (डेटासेट तैयार करना)
data = {
    'Age': [25, 32, 47, 51, 28, 38],
    'Experience': [2, 7, 20, 22, 4, 12],
    'Education': ['Bachelor', 'Master', 'PhD', 'Master', 'Bachelor', 'PhD'],
    'Performance': ['Good', 'Excellent', 'Excellent', 'Average', 'Good', 'Excellent'],
    'Salary': [45000, 75000, 120000, 110000, 52000, 95000]
}

df = pd.DataFrame(data)

# 2. Automated Analyzer Function (विश्लेषण फ़ंक्शन)
def analyze_employee_dataset(dataframe, target_col='Salary'):
    print("=" * 55)
    print("         EMPLOYEE ML PROBLEM ANALYZER")
    print("=" * 55)
    
    # Target and Features
    target = target_col
    features = [col for col in dataframe.columns if col != target]
    
    # Dataset Dimensions
    rows, cols = dataframe.shape
    
    # Numerical and Categorical Columns
    num_cols = dataframe.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = dataframe.select_dtypes(include=['object', 'category']).columns.tolist()
    
    # Problem Type & ML Task Identification
    target_dtype = dataframe[target].dtype
    unique_target_values = dataframe[target].nunique()
    
    if target_dtype in ['int64', 'float64'] and unique_target_values > 10:
        problem_type = "Regression"
        ml_task = "Predicting continuous numeric values (e.g., Linear Regression, Random Forest Regressor)"
    else:
        problem_type = "Classification"
        ml_task = "Categorizing into discrete classes (e.g., Logistic Regression, Decision Trees)"
        
    # Output Display
    print(f"1. Dataset Dimensions   : {rows} Rows × {cols} Columns")
    print(f"2. Features (X)         : {features}")
    print(f"3. Target Variable (y)  : {target}")
    print(f"4. Numerical Columns    : {num_cols}")
    print(f"5. Categorical Columns  : {cat_cols}")
    print(f"6. Problem Type         : {problem_type}")
    print(f"7. Possible ML Task     : {ml_task}")
    print("=" * 55)

# 3. Run Analyzer
analyze_employee_dataset(df, target_col='Salary')