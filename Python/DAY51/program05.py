import pandas as pd

def analyze_classification_problem(problem_description, target_name, unique_labels):
    """
    Analyzes whether an ML problem is a Classification task.
    
    Parameters:
    - problem_description (str): Short overview of the ML problem.
    - target_name (str): Name of the target variable (y).
    - unique_labels (list): List of possible discrete outputs/classes.
    """
    print(f"Problem        : {problem_description}")
    print(f"Target Variable: {target_name}")
    print(f"Possible Classes: {unique_labels}")
    
    num_classes = len(unique_labels)
    
    if num_classes == 2:
        class_type = "Binary Classification (2 classes)"
        is_classification = True
    elif num_classes > 2:
        class_type = f"Multi-Class Classification ({num_classes} classes)"
        is_classification = True
    else:
        class_type = "Invalid / Single Output"
        is_classification = False
        
    reason = f"The target variable '{target_name}' consists of discrete labels ({', '.join(map(str, unique_labels))})."

    print(f"Is Classification? : {'YES' if is_classification else 'NO'}")
    print(f"Sub-type           : {class_type}")
    print(f"Reason             : {reason}\n" + "-"*75)


# --- Example Test Cases ---

# 1. Email Spam Detection (Binary Classification)
analyze_classification_problem(
    problem_description="Classifying incoming emails as either spam or legitimate.",
    target_name="IsSpam",
    unique_labels=["Spam", "Not Spam"]
)

# 2. Patient Risk Level (Multi-Class Classification)
analyze_classification_problem(
    problem_description="Predicting patient clinical risk categories using vital signs.",
    target_name="RiskLevel",
    unique_labels=["Low", "Medium", "High"]
)

# 3. Handwritten Digit Recognition (Multi-Class Classification)
analyze_classification_problem(
    problem_description="Identifying handwritten digits (0 through 9) from image pixel inputs.",
    target_name="DigitLabel",
    unique_labels=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
)

# 4. Customer Churn Prediction (Binary Classification)
analyze_classification_problem(
    problem_description="Predicting whether a subscription service user will cancel or renew.",
    target_name="ChurnStatus",
    unique_labels=["Renewed", "Cancelled"]
)