import pandas as pd
import numpy as np

def analyze_regression_problem(problem_description, target_name, target_type, is_continuous):
    """
    Analyzes whether an ML problem is a Regression task.
    
    Parameters:
    - problem_description (str): Short overview of the problem.
    - target_name (str): Name of the target variable (y).
    - target_type (str): Data type or structure ('float', 'int', 'categorical').
    - is_continuous (bool): True if target can take any real numeric value in a range.
    """
    print(f"Problem        : {problem_description}")
    print(f"Target Variable: {target_name}")
    
    if is_continuous and target_type in ['float', 'int', 'continuous_numeric']:
        is_regression = True
        problem_type = "Regression"
        reason = f"The target variable '{target_name}' is continuous. The model predicts a quantity on a continuous scale."
    else:
        is_regression = False
        problem_type = "Classification"
        reason = f"The target variable '{target_name}' is discrete/categorical. The model predicts a class label."

    print(f"Is Regression? : {'YES' if is_regression else 'NO'}")
    print(f"Problem Type   : {problem_type}")
    print(f"Reason         : {reason}\n" + "-"*75)


# --- Example Test Cases ---

# 1. House Price Prediction
analyze_regression_problem(
    problem_description="Predicting home market values using square footage, location, and age.",
    target_name="Price ($)",
    target_type="float",
    is_continuous=True
)

# 2. Temperature Forecasting
analyze_regression_problem(
    problem_description="Forecasting tomorrow's maximum temperature based on atmospheric pressure and humidity.",
    target_name="Temperature (°C)",
    target_type="float",
    is_continuous=True
)

# 3. Employee Salary Estimation
analyze_regression_problem(
    problem_description="Estimating annual salary based on years of experience, education, and role.",
    target_name="Salary ($)",
    target_type="continuous_numeric",
    is_continuous=True
)

# 4. Loan Approval (Classification Counter-Example)
analyze_regression_problem(
    problem_description="Determining whether a loan applicant will be Approved or Rejected.",
    target_name="Status (Approved/Rejected)",
    target_type="categorical",
    is_continuous=False
)