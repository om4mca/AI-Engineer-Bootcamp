def classify_ai_vs_ml_problem(description, uses_data, relies_on_rules):
    """
    Identifies whether a given problem belongs to AI (Rule-Based) or ML (Data-Driven).
    
    Parameters:
    - description (str): Short summary of the problem.
    - uses_data (bool): True if learning requires dataset/historical records.
    - relies_on_rules (bool): True if logic can be hardcoded with fixed rules/if-else.
    """
    print(f"Problem Description: '{description}'")
    
    if uses_data and not relies_on_rules:
        category = "Machine Learning (ML)"
        reason = "यह problem ऐतिहासिक डेटा में से पैटर्न सीखती है। इसे hardcode नियमों द्वारा हल नहीं किया जा सकता।"
    elif relies_on_rules and not uses_data:
        category = "Traditional AI (Rule-Based)"
        reason = "यह problem मानव-निर्मित निश्चित नियमों (if-else logic) पर चलती है। इसे सीखने के लिए डेटा की आवश्यकता नहीं है।"
    elif uses_data and relies_on_rules:
        category = "Hybrid AI/ML System"
        reason = "यह सिस्टम डेटा-संचालित मॉडल और पूर्व-निर्धारित नियमों दोनों का उपयोग करता है।"
    else:
        category = "General Automation"
        reason = "यह एक साधारण ऑटोमेशन या बेसिक कम्प्यूटेशनल समस्या है।"

    print(f"Category : {category}")
    print(f"Reason   : {reason}\n" + "-"*60)

# --- Test Problems ---

# Example 1: Chess Engine (Rule-based Minimax)
classify_ai_vs_ml_problem(
    description="Chess engine using minimax algorithm and fixed rules to determine valid moves.",
    uses_data=False,
    relies_on_rules=True
)

# Example 2: Spam Detection (Data-driven)
classify_ai_vs_ml_problem(
    description="Classifying incoming emails as Spam or Not Spam based on past email history.",
    uses_data=True,
    relies_on_rules=False
)

# Example 3: House Price Prediction
classify_ai_vs_ml_problem(
    description="Predicting house prices using past sales data, size, and location features.",
    uses_data=True,
    relies_on_rules=False
)

# Example 4: Simple Tax Calculator
classify_ai_vs_ml_problem(
    description="Calculating income tax based on fixed government tax slab rules.",
    uses_data=False,
    relies_on_rules=True
)