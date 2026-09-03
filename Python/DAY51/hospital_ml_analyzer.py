import random

# 1. Dataset Creation (डेटासेट बनाना)
data = [
    {"Age": 45, "BloodPressure": 120, "Temperature": 98.6, "TestScore": 72, "Risk": "Low"},
    {"Age": 62, "BloodPressure": 140, "Temperature": 101.2, "TestScore": 85, "Risk": "High"},
    {"Age": 29, "BloodPressure": 115, "Temperature": 98.1, "TestScore": 60, "Risk": "Low"},
    {"Age": 58, "BloodPressure": 135, "Temperature": 99.5, "TestScore": 78, "Risk": "Medium"},
    {"Age": 71, "BloodPressure": 150, "Temperature": 102.0, "TestScore": 90, "Risk": "High"},
    {"Age": 34, "BloodPressure": 122, "Temperature": 98.4, "TestScore": 65, "Risk": "Low"},
    {"Age": 50, "BloodPressure": 130, "Temperature": 100.1, "TestScore": 80, "Risk": "Medium"},
    {"Age": 23, "BloodPressure": 110, "Temperature": 97.9, "TestScore": 55, "Risk": "Low"},
    {"Age": 65, "BloodPressure": 145, "Temperature": 101.5, "TestScore": 88, "Risk": "High"},
    {"Age": 40, "BloodPressure": 125, "Temperature": 98.8, "TestScore": 70, "Risk": "Low"}
]

# 2. Problem Analysis Details
features = ["Age", "BloodPressure", "Temperature", "TestScore"]
target = "Risk"

print("=" * 45)
print("ML PROBLEM ANALYSIS (PURE PYTHON)")
print("=" * 45)
print(f"Features (X): {features}")
print(f"Target (y): {target}")
print("Problem Type: Classification (क्योंकि Target Categorical है)")
print("Learning Type: Supervised Learning (क्योंकि Target/Label दिया गया है)")
print("=" * 45)

# 3. Train-Test Split (80% Train, 20% Test)
random.seed(42)  # Consistency के लिए
shuffled_data = data.copy()
random.shuffle(shuffled_data)

split_index = int(len(shuffled_data) * 0.8)
train_data = shuffled_data[:split_index]
test_data = shuffled_data[split_index:]

print(f"\nTraining Data Count: {len(train_data)}")
print(f"Testing Data Count: {len(test_data)}")

# 4. Simple Rule-Based Classifier (Manual Logic)
def predict_risk(age, bp, temp, score):
    # Rule-based logic built on feature patterns
    if temp >= 101.0 or bp >= 140:
        return "High"
    elif temp >= 99.5 or bp >= 130 or score >= 75:
        return "Medium"
    else:
        return "Low"

# 5. Model Evaluation (Testing Data पर Predict करना)
print("\n--- TESTING DATA & PREDICTIONS ---")
for sample in test_data:
    actual = sample["Risk"]
    predicted = predict_risk(
        sample["Age"], 
        sample["BloodPressure"], 
        sample["Temperature"], 
        sample["TestScore"]
    )
    
    inputs = {k: sample[k] for k in features}
    print(f"Input: {inputs}")
    print(f"Actual Risk: {actual} | Predicted Risk: {predicted}\n")