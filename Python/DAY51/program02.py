def analyze_supervised_problem(problem_description, has_labels, is_trial_error, target_type):
    """
    Identifies if a given ML problem is Supervised Learning and categorizes it.
    
    Parameters:
    - problem_description (str): Description of the ML task.
    - has_labels (bool): True if training data contains ground-truth targets (y).
    - is_trial_error (bool): True if learning relies on rewards/penalties in an environment.
    - target_type (str): 'continuous', 'categorical', or 'none'.
    """
    print(f"Problem: {problem_description}")
    
    if is_trial_error:
        learning_type = "Reinforcement Learning"
        reason = "यह समस्या एक वातावरण (Environment) में ट्रायल-एंड-एरर और रिवॉर्ड के जरिए सीखी जाती है।"
        subtype = "N/A"
    elif has_labels:
        learning_type = "Supervised Learning"
        reason = "डेटासेट में स्पष्ट इनपुट (X) और ग्राउंड-ट्रुथ आउटपुट लेबल्स (y) मौजूद हैं।"
        if target_type == 'continuous':
            subtype = "Regression (निरंतर संख्या जैसे मूल्य/तापमान का अनुमान)"
        elif target_type == 'categorical':
            subtype = "Classification (श्रेणी जैसे Spam/Ham, High/Low का अनुमान)"
        else:
            subtype = "Unknown Target Structure"
    else:
        learning_type = "Unsupervised Learning"
        reason = "डेटासेट में कोई आउटपुट लेबल (y) नहीं है; केवल बिना लेबल वाला डेटा मौजूद है।"
        subtype = "Clustering / Dimensionality Reduction"

    print(f"Is Supervised? : {'YES' if learning_type == 'Supervised Learning' else 'NO'}")
    print(f"Learning Type  : {learning_type}")
    print(f"Subtype        : {subtype}")
    print(f"Reason         : {reason}\n" + "-"*65)

# --- Test Cases ---

# Example 1: Email Spam Filter
analyze_supervised_problem(
    problem_description="Classifying emails as Spam or Not Spam using past labeled emails.",
    has_labels=True,
    is_trial_error=False,
    target_type='categorical'
)

# Example 2: House Price Prediction
analyze_supervised_problem(
    problem_description="Predicting home prices based on historical sales data (Square Feet, Bedrooms).",
    has_labels=True,
    is_trial_error=False,
    target_type='continuous'
)

# Example 3: Customer Clustering
analyze_supervised_problem(
    problem_description="Grouping online shoppers into segments based on purchase patterns without labels.",
    has_labels=False,
    is_trial_error=False,
    target_type='none'
)

# Example 4: Autonomous Driving Control
analyze_supervised_problem(
    problem_description="Training a self-driving car using penalties for crashes and rewards for safe lane-keeping.",
    has_labels=False,
    is_trial_error=True,
    target_type='none'
)