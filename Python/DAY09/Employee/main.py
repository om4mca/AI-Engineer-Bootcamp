# Import the custom Employee module blueprint explicitly
from employee_mod import Employee


def main():
    print("=== HR Corporate Roster System ===")
    
    # 1. Instantiate corporate personnel entities
    staff_roster = [
        Employee(name="Om Roy", base_salary=64000.00, performance_score=5),
        Employee(name="Ramesh Kumar", base_salary=52000.00, performance_score=3),
        Employee(name="Rakesh Singh", base_salary=71000.00, performance_score=4)
    ]
    
    # 2. Iterate and print specific personnel summaries
    for emp in staff_roster:
        data = emp.get_details()
        print(f"\nProfile: {data['Name']} ({data['ID']})")
        print(f"  - Performance Rating: {data['Performance Rating']}/5")
        print(f"  - Base Allocation:    {data['Base Pay']:,.2f}")
        print(f"  - Calculated Bonus:   +{data['Bonus']:,.2f}")
        print(f"  - Disbursed Net Pay:  {data['Net Take Home']:,.2f}")
        
    print("\n==================================")

if __name__ == "__main__":
    main()