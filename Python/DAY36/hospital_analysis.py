def calculate_emergency_probability(total_patients, emergency_patients):
    """Calculates the probability and percentage of selecting an emergency patient."""
    if total_patients <= 0:
        raise ValueError("Total patients must be greater than zero.")

    # Calculate probability
    probability = emergency_patients / total_patients

    # Calculate percentage
    percentage = probability * 100

    return probability, percentage


# Given Data
total_patients = 1000
emergency_patients = 150

# Run Calculation
prob, percent = calculate_emergency_probability(
    total_patients, emergency_patients
)

# Display Results
print(f"Total Patients: {total_patients}")
print(f"Emergency Patients: {emergency_patients}")
print("-" * 40)
print(f"Probability (Decimal) : {prob:.2f}")
print(f"Probability (Fraction): {emergency_patients}/{total_patients}")
print(f"Probability (Percent) : {percent:.1f}%")