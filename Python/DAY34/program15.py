import pandas as pd
import numpy as np

def generate_eda_summary(df):
    print("=" * 60)
    print("                 📊 COMPLETE EDA SUMMARY REPORT             ")
    print("=" * 60)
    
    # 1. Dataset Dimensions & Memory Footprint
    rows, cols = df.shape
    memory_mb = df.memory_usage(deep=True).sum() / (1024 ** 2)
    print("\n1. DATASET OVERVIEW")
    print(f"   • Total Records (Rows)   : {rows:,}")
    print(f"   • Total Features (Cols)  : {cols:,}")
    print(f"   • Memory Consumption     : {memory_mb:.2f} MB")
    
    # 2. Data Types Breakdown
    print("\n2. DATA TYPES BREAKDOWN")
    print(df.dtypes.value_counts().to_string())
    
    # 3. Data Quality & Hygiene Check
    null_counts = df.isnull().sum()
    null_pct = (null_counts / rows) * 100
    null_summary = pd.DataFrame({'Missing_Count': null_counts, 'Missing_%': null_pct})
    cols_with_nulls = null_summary[null_summary['Missing_Count'] > 0]
    
    duplicate_rows = df.duplicated().sum()
    
    print("\n3. DATA QUALITY & HYGIENE")
    print(f"   • Duplicate Rows Count   : {duplicate_rows} ({duplicate_rows/rows*100:.2f}%)")
    print(f"   • Columns with Missing   : {len(cols_with_nulls)} / {cols}")
    if not cols_with_nulls.empty:
        print("\n   Missing Value Summary:")
        print(cols_with_nulls.round(2).to_string())
        
    # 4. Cardinality & Constant Features Check
    constant_cols = [col for col in df.columns if df[col].nunique() == 1]
    high_cardinality_cols = [col for col in df.columns if df[col].dtype == 'object' and df[col].nunique() > 50]
    
    print("\n4. FEATURE CARDINALITY AUDIT")
    print(f"   • Zero-Variance / Constant Columns : {constant_cols if constant_cols else 'None'}")
    print(f"   • High-Cardinality String Columns   : {high_cardinality_cols if high_cardinality_cols else 'None'}")
    
    # 5. Numerical Summary Statistics
    num_df = df.select_dtypes(include=[np.number])
    if not num_df.empty:
        print("\n5. NUMERICAL FEATURE STATISTICAL SUMMARY")
        num_summary = num_df.describe().T[['mean', 'std', 'min', '50%', 'max']]
        num_summary['skewness'] = num_df.skew()
        num_summary.rename(columns={'50%': 'median'}, inplace=True)
        print(num_summary.round(2).to_string())
        
    # 6. Categorical Summary Statistics
    cat_df = df.select_dtypes(include=['object', 'category'])
    if not cat_df.empty:
        print("\n6. CATEGORICAL FEATURE SUMMARY")
        cat_summary = cat_df.describe().T[['count', 'unique', 'top', 'freq']]
        print(cat_summary.to_string())
        
    print("\n" + "=" * 60)

# --- Test Script on Synthetic Dataset ---
np.random.seed(42)
sample_df = pd.DataFrame({
    'ID': range(1001, 1101),
    'Age': np.random.choice([22, 28, 35, 42, np.nan, 55], size=100),
    'Salary': np.random.lognormal(mean=11, sigma=0.5, size=100),
    'Department': np.random.choice(['IT', 'HR', 'Sales'], size=100),
    'Company_Branch': 'Headquarters'  # Constant column
})

generate_eda_summary(sample_df)