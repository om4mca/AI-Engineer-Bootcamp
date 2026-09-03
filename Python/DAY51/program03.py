def analyze_unsupervised_problem(problem_description, has_target_labels, is_reinforcement, task_type):
    """
    Analyzes whether an ML problem belongs to Unsupervised Learning.
    
    Parameters:
    - problem_description (str): Overview of the problem.
    - has_target_labels (bool): True if target variable (y) exists.
    - is_reinforcement (bool): True if environmental rewards/penalties drive learning.
    - task_type (str): 'clustering', 'anomaly_detection', 'dimensionality_reduction', 'association'.
    """
    print(f"Problem: {problem_description}")
    
    if is_reinforcement:
        category = "Reinforcement Learning"
        is_unsupervised = False
        reason = "Learns via trial-and-error using environment rewards/penalties."
        sub_category = "N/A"
    elif has_target_labels:
        category = "Supervised Learning"
        is_unsupervised = False
        reason = "Data contains explicit target labels (y)."
        sub_category = "Regression / Classification"
    else:
        category = "Unsupervised Learning"
        is_unsupervised = True
        reason = "Data contains NO target labels (y). Patterns must be discovered autonomously."
        
        mapping = {
            'clustering': "Clustering (Grouping similar data points without prior labels)",
            'anomaly_detection': "Anomaly Detection (Identifying rare patterns or outliers)",
            'dimensionality_reduction': "Dimensionality Reduction (Compressing features while keeping variance)",
            'association': "Association Rule Mining (Finding relationships between co-occurring items)"
        }
        sub_category = mapping.get(task_type, "General Pattern Discovery")

    print(f"Is Unsupervised? : {'YES' if is_unsupervised else 'NO'}")
    print(f"Main Category   : {category}")
    print(f"Sub-category    : {sub_category}")
    print(f"Reason          : {reason}\n" + "-"*70)


# --- Example Use Cases ---

# 1. Customer Segmentation (Clustering)
analyze_unsupervised_problem(
    problem_description="Grouping shoppers into distinct personas based on purchase frequency and average spending.",
    has_target_labels=False,
    is_reinforcement=False,
    task_type='clustering'
)

# 2. Fraud & Intrusion Detection (Anomaly Detection)
analyze_unsupervised_problem(
    problem_description="Flagging unexpected server network traffic that deviates from standard historical baseline logs.",
    has_target_labels=False,
    is_reinforcement=False,
    task_type='anomaly_detection'
)

# 3. Market Basket Analysis (Association Rules)
analyze_unsupervised_problem(
    problem_description="Identifying products frequently purchased together in grocery checkout carts (e.g., Diapers & Beer).",
    has_target_labels=False,
    is_reinforcement=False,
    task_type='association'
)

# 4. High-Dimensional Data Compression (Dimensionality Reduction)
analyze_unsupervised_problem(
    problem_description="Reducing 50 genomic features down to 2 principal components for visual plotting.",
    has_target_labels=False,
    is_reinforcement=False,
    task_type='dimensionality_reduction'
)

# 5. Email Spam Classification (Supervised Counter-Example)
analyze_unsupervised_problem(
    problem_description="Classifying incoming emails as 'Spam' or 'Not Spam' using labeled past email archives.",
    has_target_labels=True,
    is_reinforcement=False,
    task_type='classification'
)