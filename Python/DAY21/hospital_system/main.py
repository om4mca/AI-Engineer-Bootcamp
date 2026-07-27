from service import PatientService

def show_menu():
    print("\n" + "🏥 HOSPITAL MANAGEMENT SYSTEM v2")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Save Patients to File")
    print("7. Load Patients from File")
    print("8. Exit")

def main():
    service = PatientService()
    # Auto-load data at start
    service.load_from_file()

    while True:
        show_menu()
        choice = input("\nEnter choice (1-8): ").strip()

        if choice == "1":
            p_id = input("Enter Patient ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            disease = input("Enter Disease: ")
            contact = input("Enter 10-digit Phone: ")
            service.add_patient(p_id, name, age, disease, contact)

        elif choice == "2":
            service.view_all_patients()

        elif choice == "3":
            p_id = input("Enter Patient ID to Search: ")
            service.search_patient(p_id)

        elif choice == "4":
            p_id = input("Enter Patient ID to Update: ")
            print("(Leave blank to keep existing value)")
            name = input("New Name: ")
            age = input("New Age: ")
            disease = input("New Disease: ")
            contact = input("New Phone: ")
            
            service.update_patient(
                patient_id=p_id,
                name=name if name else None,
                age=int(age) if age.isdigit() else None,
                disease=disease if disease else None,
                contact=contact if contact else None
            )

        elif choice == "5":
            p_id = input("Enter Patient ID to Delete: ")
            service.delete_patient(p_id)

        elif choice == "6":
            service.save_to_file()

        elif choice == "7":
            service.load_from_file()

        elif choice == "8":
            # Auto-save before exit
            service.save_to_file()
            print("👋 Thank you for using Hospital Management System!")
            break
        else:
            print("⚠️ Invalid choice. Please select from 1 to 8.")

if __name__ == "__main__":
    main()