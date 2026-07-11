# Import the custom Patient class explicitly from our hospital module
from hospital_mod import Patient


def main():
    print("=== Emergency Triage & Check-In Portal ===")
    
    # 1. Admit incoming emergency floor cases
    admissions_desk = [
        Patient(name="Om Roy", age=45, triage_symptom="Severe chest pain", base_fee=1250.00),
        Patient(name="Ranjan Kumar", age=29, triage_symptom="Sprained wrist from fall", base_fee=300.00),
        Patient(name="Sachin", age=68, triage_symptom="High fever and chills", base_fee=620.00)
    ]
    
    # 2. Process clinical flow and billing allocations
    # Assuming insurance coverage variables (e.g., Marcus has 80% coverage plan)
    insurance_plans = [0.80, 0.00, 0.50]
    
    for idx, patient in enumerate(admissions_desk):
        coverage = insurance_plans[idx]
        profile = patient.export_medical_profile(discount_pct=coverage)
        
        print(f"\n[ADMISSION RECORD: {profile['Patient ID']}]")
        print(f"  Name:       {profile['Full Name']} ({profile['Age']})")
        print(f"  Timestamp:  {profile['Admitted']}")
        print(f"  Triage:     {profile['Triage Status']}")
        print(f"  Coverage:   {int(coverage * 100)}% Co-Pay Discount Applied")
        print(f"  Invoice:    {profile['Total Balance Due']:,.2f}")
        
    print("\n==========================================")

if __name__ == "__main__":
    main()