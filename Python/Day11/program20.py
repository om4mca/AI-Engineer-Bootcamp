#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Contact Book
# Author: Om Roy
# Date: 14-07-2026
#--------------------------------------------

import os
import re

class DuplicateContactError(Exception):
    """Raised when trying to save an email address that already exists."""
    pass

class ContactNotFoundError(Exception):
    """Raised when a searched contact name or email cannot be located."""
    pass

class InvalidContactDataError(Exception):
    """Raised when contact inputs fail standard format validation checks."""
    pass


class ContactBookManager:
    FILE_NAME = "contacts.txt"
    VALID_LABELS = ["Family", "Friends", "Work", "Other"]

    @classmethod
    def add_and_save_contact(cls, name, phone, email, label):
        # 1. Clean and normalize fields
        name = str(name).strip().title()
        phone = str(phone).strip()
        email = str(email).strip().lower()
        label = str(label).strip().title()

        # 2. Strict Input Validations
        if not name or not phone or not email or not label:
            raise InvalidContactDataError("All entries (Name, Phone, Email, Label) are mandatory.")

        # Phone validation (allow digits, spaces, hyphens, and +)
        clean_phone = re.sub(r"[\s\-\+]", "", phone)
        if not clean_phone.isdigit() or len(clean_phone) < 7 or len(clean_phone) > 15:
            raise InvalidContactDataError("Phone Error: Must contain 7 to 15 digits (plus signs or hyphens are allowed).")

        # Email validation
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, email):
            raise InvalidContactDataError("Email Error: Please supply a valid email address format.")

        # Label validation
        if label not in cls.VALID_LABELS:
            allowed = ", ".join(cls.VALID_LABELS)
            raise InvalidContactDataError(f"Label Error: Must match one of: [{allowed}].")

        # Strip pipe delimiters to protect file database alignments
        name = name.replace("|", "-")
        phone = phone.replace("|", "-")

        # 3. Prevent duplicate emails
        if cls._email_exists(email):
            raise DuplicateContactError(f"Database Conflict: A contact with email '{email}' already exists.")

        # 4. Save record (Name|Phone|Email|Label)
        record_line = f"{name}|{phone}|{email}|{label}\n"
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: Contact '{name}' added successfully under label: {label}.")
        except IOError as e:
            print(f"\n[File Access Error]: Unable to save contact to disk. Details: {e}")

    @classmethod
    def display_all_contacts(cls):
        records = cls._load_records()
        if not records:
            print("\n[Contact Directory]: Your contact book is currently empty.")
            return

        # Sort alphabetically by contact name
        records.sort(key=lambda x: x[0])

        print("\n📇 === CONTACT DIRECTORY ===")
        print(f"{'Name':<22} | {'Phone':<15} | {'Email':<25} | {'Label'}")
        print("-" * 75)
        for name, phone, email, label in records:
            print(f"{name:<22} | {phone:<15} | {email:<25} | {label}")
        print("=" * 75)

    @classmethod
    def search_contacts(cls, keyword):
        keyword = str(keyword).strip().lower()
        if not keyword:
            raise InvalidContactDataError("Search query cannot be empty.")

        records = cls._load_records()
        matches = []

        for name, phone, email, label in records:
            if keyword in name.lower() or keyword in email or keyword in phone:
                matches.append((name, phone, email, label))

        if not matches:
            raise ContactNotFoundError(f"No contacts found matching: '{keyword}'")

        print(f"\n🎯 [Search Results for: '{keyword}']")
        print(f"{'Name':<22} | {'Phone':<15} | {'Email':<25} | {'Label'}")
        print("-" * 75)
        for name, phone, email, label in matches:
            print(f"{name:<22} | {phone:<15} | {email:<25} | {label}")
        print("=" * 75)

    # --- Secure Internal Storage Helpers ---
    @classmethod
    def _load_records(cls):
        """Safely loads and parses pipe-delimited contact records."""
        if not os.path.exists(cls.FILE_NAME):
            return []

        parsed_records = []
        try:
            with open(cls.FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    cleaned = line.strip()
                    if cleaned:
                        parts = cleaned.split("|")
                        if len(parts) == 4:
                            parsed_records.append(parts)
        except IOError as e:
            print(f"[Critical System Error]: Cannot parse contacts database file. {e}")
            
        return parsed_records

    @classmethod
    def _email_exists(cls, check_email):
        records = cls._load_records()
        return any(email == check_email for _, _, email, _ in records)


def main():
    print("=== Secure Contact Book Engine ===")
    
    while True:
        print("\n" + "="*35)
        print("         CONTACT PORTAL")
        print("="*35)
        print("1. Add New Contact")
        print("2. Display All Contacts (A-Z)")
        print("3. Search Contact (by Name/Email/Phone)")
        print("4. Close Directory System")
        print("="*35)
        
        choice = input("Select operation (1-4): ").strip()

        try:
            if choice == "1":
                name = input("Enter Full Name: ")
                phone = input("Enter Phone Number: ")
                email = input("Enter Email Address: ")
                print(f"Valid Labels: {', '.join(ContactBookManager.VALID_LABELS)}")
                label = input("Enter Label: ")
                ContactBookManager.add_and_save_contact(name, phone, email, label)

            elif choice == "2":
                ContactBookManager.display_all_contacts()

            elif choice == "3":
                query = input("Enter search keyword: ")
                ContactBookManager.search_contacts(query)

            elif choice == "4":
                print("\nContact book directory shut down securely.")
                break
            else:
                print("\n[Input Error]: Please select a valid option (1-4).")

        except InvalidContactDataError as e:
            print(f"\n🚨 [Invalid Data]: {e}")
            
        except DuplicateContactError as e:
            print(f"\n🚨 [Duplicate Found]: {e}")
            
        except ContactNotFoundError as e:
            print(f"\n🚨 [No Matches]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [System Interruption]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()