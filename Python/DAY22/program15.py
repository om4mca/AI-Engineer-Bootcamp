#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:   complete Hospital Data Analysis Program
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

from collections import defaultdict
import math

class PurePythonHospitalAnalyzer:
    def __init__(self, data):
        """
        Input data: List of Dictionaries
        """
        self.data = data

    def clean_data(self):
        """
        1. Duplicate Records हटाना
        2. Missing Values (None, '', 'NaN') को Fill करना
        """
        print("\n🧹 1. Cleaning Data...")
        
        
        seen = set()
        unique_data = []
        for record in self.data:
            # Hashable tuple for tracking duplicates
            record_tuple = tuple(sorted(record.items()))
            if record_tuple not in seen:
                seen.add(record_tuple)
                unique_data.append(record.copy())
        
        removed_duplicates = len(self.data) - len(unique_data)
        print(f"   - Removed {removed_duplicates} duplicate record(s).")
        self.data = unique_data

        
        
        
        valid_ages = [r["age"] for r in self.data if r.get("age") is not None and isinstance(r["age"], (int, float))]
        avg_age = round(sum(valid_ages) / len(valid_ages)) if valid_ages else 0

        
        valid_bills = sorted([r["bill_amount"] for r in self.data if r.get("bill_amount") is not None and isinstance(r["bill_amount"], (int, float))])
        n = len(valid_bills)
        if n % 2 == 1:
            median_bill = valid_bills[n // 2]
        else:
            median_bill = (valid_bills[(n // 2) - 1] + valid_bills[n // 2]) / 2 if n > 0 else 0.0

        # Imputation Application
        for record in self.data:
            # Fill missing Age
            if record.get("age") is None:
                record["age"] = avg_age
            
            # Fill missing Disease
            if not record.get("disease") or str(record["disease"]).strip() == "":
                record["disease"] = "Unknown"
            
            # Fill missing Bill Amount
            if record.get("bill_amount") is None:
                record["bill_amount"] = median_bill

        print(f"   - Filled missing 'age' values with mean age: {avg_age}")
        print(f"   - Filled missing 'bill_amount' values with median bill: ₹{median_bill:,.2f}")
        return self.data

    def get_summary_stats(self):
        """Overall Summary Statistics (Total Patients, Revenue, Avg/Min/Max Bills)"""
        print("\n📊 2. Overall Summary Statistics:")
        print("-" * 45)
        
        total_patients = len(self.data)
        if total_patients == 0:
            print("No patient records available.")
            return

        ages = [r["age"] for r in self.data]
        bills = [r["bill_amount"] for r in self.data]

        avg_age = sum(ages) / total_patients
        total_revenue = sum(bills)
        avg_bill = total_revenue / total_patients
        max_bill = max(bills)
        min_bill = min(bills)

        print(f"• Total Patients      : {total_patients}")
        print(f"• Average Patient Age : {avg_age:.1f} years")
        print(f"• Total Revenue       : ₹{total_revenue:,.2f}")
        print(f"• Average Bill Amount : ₹{avg_bill:,.2f}")
        print(f"• Highest Bill        : ₹{max_bill:,.2f}")
        print(f"• Lowest Bill         : ₹{min_bill:,.2f}")

    def filter_by_disease(self, disease_name):
        
        print(f"\n🔍 3. Filtering Patients with Disease: '{disease_name}'")
        print("-" * 45)
        
        filtered = [
            r for r in self.data 
            if r["disease"].strip().lower() == disease_name.strip().lower()
        ]

        if not filtered:
            print("No records found.")
            return []

        # Custom Tabular Display
        print(f"{'Patient ID':<12} | {'Name':<12} | {'Age':<5} | {'Bill Amount (₹)':<15}")
        print("-" * 52)
        for r in filtered:
            print(f"{r['patient_id']:<12} | {r['name']:<12} | {r['age']:<5} | ₹{r['bill_amount']:<14,.2f}")
        
        return filtered

    def disease_breakdown(self):
        """Disease-wise Grouping and Aggregation"""
        print("\n🏥 4. Disease-wise Patient Count & Total Revenue:")
        print("-" * 55)
        
        disease_map = defaultdict(lambda: {"count": 0, "total_age": 0, "total_bill": 0.0})

        for r in self.data:
            d = r["disease"]
            disease_map[d]["count"] += 1
            disease_map[d]["total_age"] += r["age"]
            disease_map[d]["total_bill"] += r["bill_amount"]

        print(f"{'Disease':<15} | {'Count':<8} | {'Avg Age':<10} | {'Total Revenue (₹)':<18}")
        print("-" * 60)
        for disease, stats in disease_map.items():
            avg_age = stats["total_age"] / stats["count"]
            print(f"{disease:<15} | {stats['count']:<8} | {avg_age:<10.1f} | ₹{stats['total_bill']:<17,.2f}")

    def age_group_analysis(self):
        
        print("\n👥 5. Age Group Analysis:")
        print("-" * 45)

        age_groups = {
            "Youth (<18)": {"count": 0, "total_bill": 0.0},
            "Adult (18-50)": {"count": 0, "total_bill": 0.0},
            "Senior Citizen (>50)": {"count": 0, "total_bill": 0.0}
        }

        for r in self.data:
            age = r["age"]
            bill = r["bill_amount"]

            if age < 18:
                group = "Youth (<18)"
            elif 18 <= age <= 50:
                group = "Adult (18-50)"
            else:
                group = "Senior Citizen (>50)"

            age_groups[group]["count"] += 1
            age_groups[group]["total_bill"] += bill

        print(f"{'Age Group':<22} | {'Patient Count':<13} | {'Total Bill (₹)':<15}")
        print("-" * 57)
        for group, stats in age_groups.items():
            print(f"{group:<22} | {stats['count']:<13} | ₹{stats['total_bill']:<14,.2f}")


# ==========================================
# 🚀 Execution
# ==========================================

if __name__ == "__main__":
    # Raw Sample Dataset without Pandas/Numpy
    raw_hospital_data = [
        {"patient_id": "P101", "name": "Rajesh", "age": 45, "disease": "Diabetes", "bill_amount": 45000.0},
        {"patient_id": "P102", "name": "Suresh", "age": 62, "disease": "Hypertension", "bill_amount": 60000.0},
        {"patient_id": "P103", "name": "Priya", "age": None, "disease": "Diabetes", "bill_amount": 52000.0},  # Missing Age
        {"patient_id": "P104", "name": "Amit", "age": 29, "disease": "Asthma", "bill_amount": 15000.0},
        {"patient_id": "P105", "name": "Neha", "age": 58, "disease": "Diabetes", "bill_amount": None},       # Missing Bill
        {"patient_id": "P106", "name": "Vikas", "age": 12, "disease": "Asthma", "bill_amount": 12000.0},
        {"patient_id": "P101", "name": "Rajesh", "age": 45, "disease": "Diabetes", "bill_amount": 45000.0}, # Duplicate Record
        {"patient_id": "P107", "name": "Kavita", "age": 68, "disease": None, "bill_amount": 80000.0}          # Missing Disease
    ]

    print("==================================================")
    print(" 🏥 PURE PYTHON HOSPITAL DATA ANALYZER 🏥 ")
    print("==================================================")

    # Initialize Analyzer
    analyzer = PurePythonHospitalAnalyzer(raw_hospital_data)

    # 1. Clean Data (Duplicates & Missing Values)
    analyzer.clean_data()

    # 2. Display Overall Stats
    analyzer.get_summary_stats()

    # 3. Disease Breakdown Analysis
    analyzer.disease_breakdown()

    # 4. Search/Filter Disease
    analyzer.filter_by_disease("Diabetes")

    # 5. Age Group Analysis
    analyzer.age_group_analysis()